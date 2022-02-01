from libs import CharacterPathsHandling, Logger
from settings import GlobalSettings, CharacterSettings
from pathlib import WindowsPath

import os


class ExceptionsHandling:
    @staticmethod
    def order_change(paths: list[WindowsPath], current_exception: list[str]) -> list[WindowsPath]:
        '''Change the order between two images or one image and layers.
        
        Examples:
            - ["ORDER_CHANGE", "name", "put_before_this_layer"]
            - ["ORDER_CHANGE", "name", "put_before_this_image"]

        Args:
            paths (list[WindowsPath]): List of all the paths used for one NFT.
            current_exception (list[str]): Current exception handled in the loop.

        Returns:
            list[WindowsPath]: Modified list of paths.
        '''
        
        layers_list = CharacterPathsHandling.get_layer_names_from_paths(paths)
        logger_message = False
        
        # Check if it's a layer order change
        if current_exception[2] in layers_list:
            is_layer_order_change = True
        else:
            is_layer_order_change = False
            
        # Change the order between two images
        if not is_layer_order_change:
            first_path_index = CharacterPathsHandling.get_index_in_paths_list_from_filename(paths, current_exception[1])
            second_path_index = CharacterPathsHandling.get_index_in_paths_list_from_filename(paths, current_exception[2])
            
            # If these two images are detected, change the order
            if first_path_index is not None and second_path_index is not None:
                saved_path = paths[first_path_index]
                paths.pop(first_path_index)
                paths.insert(second_path_index, saved_path)
                logger_message = True
            
        # Change order between an image and a layer (Uses current_exception[2] as the layer name)
        # Note that it supports only one path, as the paths list is sorted,
        # It will use the first path in the list.  
        else:
            image_path_index = CharacterPathsHandling.get_index_in_paths_list_from_filename(paths, current_exception[1])
            paths_from_layer = CharacterPathsHandling.get_paths_from_layer_name(paths, current_exception[2])
            
            # Check if there's at least one path in the list
            if len(paths_from_layer) > 0:
                order_change_path_index = paths.index(paths_from_layer[0])  # First path index in 'paths_from_layer'
            else:
                order_change_path_index = None
            
            # If the image is detected, then change the order
            if image_path_index is not None and order_change_path_index is not None:
                saved_path = paths[image_path_index]
                paths.pop(image_path_index)
                paths.insert(order_change_path_index, saved_path)
                logger_message = True
                
        if logger_message:
            Logger.pyprint(f'Order changed: [{current_exception[1]}] is now before [{current_exception[2]}]', 'DATA')
            
        return paths

    
    @staticmethod
    def incompatibilities(paths: list[WindowsPath], current_exception: list[str]):
        '''Check incompatibilities with one image and one layer or multiple images.
        
        Examples:
            - ["INCOMPATIBLE", "image_1.png", "image_2.png", "image_3.png"]
            - ["INCOMPATIBLE", "image.png", "layer"]

        Args:
            paths (list[WindowsPath]): List of all the paths used for one NFT.
            current_exception (list[str]): Current exception handled in the loop.

        Returns:
            list[WindowsPath] OR None: Valid list of path or None if an incompatibility is found.
        '''
        
        paths_driver = len(paths)
        incompatibles = current_exception[1:]
        incompatibility_driver = len(incompatibles)
        
        # Check if it's a layer incompatibility
        is_layer_incompatibility = False
        layers_list = CharacterPathsHandling.get_layer_names_from_paths(paths)
        for i in range(incompatibility_driver):
            if incompatibles[i] in layers_list:
                is_layer_incompatibility = True
                break
        
        # Handles Incompatibilities between multiple images
        if not is_layer_incompatibility:
            incompatible_paths = []
            
            # Add all the images index in path to a list
            for i in range(incompatibility_driver):
                current_path_index = CharacterPathsHandling.get_index_in_paths_list_from_filename(
                                        paths,
                                        incompatibles[i]
                                     )
                incompatible_paths.append(current_path_index)
            
            # Regenerate the NFT is the images are all found
            if None not in incompatible_paths:
                Logger.pyprint('Incompatible images found', 'WARN')
                return None  # Regenerate the NFT
        
        # Handles incompatibilities with a whole layer
        else:
            if incompatibility_driver > 2:
                Logger.pyprint('Incompatibility in layer mode only supports one image and one layer', 'WARN')
                
            # Check if the image is used (Returns None if not)
            image_path = CharacterPathsHandling.get_index_in_paths_list_from_filename(paths, incompatibles[0])
            
            # If the image is used, check the incompatibility
            if image_path is not None:
                for i in range(paths_driver):
                    # Get the layer name of every image
                    current_layer = os.path.basename(paths[i].parent)
                    
                    # Check if the layer name is the incompatible one
                    if current_layer == incompatibles[1]:
                        Logger.pyprint('Incompatibility with a layer found', 'WARN')
                        return None  # Regenerate the NFT

        Logger.pyprint('Exceptions handled successfully', 'INFO')
        return paths


    @staticmethod
    def exceptions_handling(paths: list[WindowsPath], settings: CharacterSettings):
        '''Handle multiple exceptions / incompatibilities between layers.
        
        - 'ORDER_CHANGE' -> Change the order between two layers / images.
        - 'INCOMPATIBLE' -> NFT is regenerated if the test is not passed.

        Args:
            paths: Randomized character paths list.
            settings: Link to the settings (Character settings).
            
        Returns:
            list[WindowsPath] OR None: Modified paths list. (Or None if the NFT needs to be regenerated)
        '''
    
        exceptions = settings.exceptions
        exceptions_driver = len(exceptions)
        
        for i in range(exceptions_driver):
            current_exception = exceptions[i]
            
            # Order change exception (Returns the default 'paths' var if unavailable)
            if current_exception[0] == GlobalSettings.exceptions_list[0]:
                paths = ExceptionsHandling.order_change(paths, current_exception)
                
            # Incompatibility exception (Returns None to regenerate the NFT)
            elif current_exception[0] == GlobalSettings.exceptions_list[1]:
                paths = ExceptionsHandling.incompatibilities(paths, current_exception)
                
                # If it's incompatible, it's not necessary to continue the exceptions handling
                if paths is None:
                    break
                
            # Error
            else:
                Logger.pyprint(f'Invalid exception instruction at {current_exception}', 'ERRO')
        
        Logger.pyprint('Exceptions handled successfully', 'INFO')
        return paths
