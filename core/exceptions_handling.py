from settings import GlobalSettings, CharacterSettings
from core import PathsHandling, Logger
from pathlib import Path

import textwrap


class ExceptionsHandling:
    @staticmethod
    def order_change_mode(current_exception: list[str], layers_list: list[str]) -> str:
        '''Returns the mode of the order change.
        
        Args:
            current_exception (list[str]): Current exception handled in the loop.
            layers_list (list[str]): The list of all the layers found inside the 'paths' var.
            
        Returns:
            str: The mode of the order change.
        '''
        
        order_mode = GlobalSettings.order_change_modes[0]
    
        # Layer before image check
        if current_exception[1] in layers_list:
            order_mode = GlobalSettings.order_change_modes[1]
        # Image before layer check
        if current_exception[2] in layers_list:
            order_mode = GlobalSettings.order_change_modes[2]
        # Layer before layer check
        if current_exception[1] in layers_list and order_mode == GlobalSettings.order_change_modes[2]:
            order_mode = GlobalSettings.order_change_modes[3]
            
        if order_mode != GlobalSettings.order_change_modes[0] and len(current_exception) > 3:
            err = f'In this mode, "ORDER_CHANGE" only supports two images/layers [{current_exception}]'
            Logger.pyprint('WARN', '', err, True)
            
        return order_mode
    
    
    @staticmethod
    def order_change(paths: list[Path], current_exception: list[str]) -> list[Path]:
        '''Change the order between images / layers.
        
        Args:
            paths (list[Path]): List of all the paths used for one NFT.
            current_exception (list[str]): Current exception handled in the loop.

        Returns:
            list[Path]: Modified list of paths.
        '''
        
        layers_list = PathsHandling.get_layer_names_from_paths(paths)
        order_change_mode = ExceptionsHandling.order_change_mode(current_exception, layers_list)

        # IMAGE BEFORE IMAGE
        if order_change_mode == GlobalSettings.order_change_modes[0]:
            first_path_index = PathsHandling.get_index_in_paths_list_from_filename(paths, current_exception[1])
            second_path_index = PathsHandling.get_index_in_paths_list_from_filename(paths, current_exception[2])

            # If these two images are detected, change the order
            if first_path_index is not None and second_path_index is not None:
                saved_path = paths[first_path_index]
                paths.pop(first_path_index)
                paths.insert(second_path_index, saved_path)

        # LAYER BEFORE IMAGE
        elif order_change_mode == GlobalSettings.order_change_modes[1]:
            paths_from_layer = PathsHandling.get_paths_from_layer_name(paths, current_exception[1])
            image_path_index = PathsHandling.get_index_in_paths_list_from_filename(paths, current_exception[2])
            
            # If the image is detected and one of the path is used, change the order
            if len(paths_from_layer) > 0 and image_path_index is not None:
                for path in paths_from_layer:
                    try:
                        paths.remove(path)
                        paths.insert(image_path_index, path)
                    except ValueError as err:
                        Logger.pyprint('ERRO', '', f'Order change path error [{err}]', True)
                        
        # IMAGE BEFORE LAYER
        elif order_change_mode == GlobalSettings.order_change_modes[2]:
            image_path_index = PathsHandling.get_index_in_paths_list_from_filename(paths, current_exception[1])
            paths_from_layer = PathsHandling.get_paths_from_layer_name(paths, current_exception[2])
            
            # Check if there's at least one path in the list
            if len(paths_from_layer) > 0:
                # First path index in 'paths_from_layer'
                order_change_path_index = paths.index(paths_from_layer[0])
            else:
                order_change_path_index = None
            
            # If the image is detected and one of the path is used, change the order
            if image_path_index is not None and order_change_path_index is not None:
                saved_path = paths[image_path_index]
                paths.pop(image_path_index)
                paths.insert(order_change_path_index, saved_path)

        # LAYER BEFORE LAYER
        elif order_change_mode == GlobalSettings.order_change_modes[3]:
            paths_from_layer_1 = PathsHandling.get_paths_from_layer_name(paths, current_exception[1])
            paths_from_layer_2 = PathsHandling.get_paths_from_layer_name(paths, current_exception[2])
            
            # Check if there's at least one path in the lists
            if len(paths_from_layer_1) > 0 and len(paths_from_layer_2) > 0:
                # First path index in 'paths_from_layer_2'
                order_change_path_index = paths.index(paths_from_layer_2[0])
            else:
                order_change_path_index = None
                
            if order_change_path_index is not None:
                for path in paths_from_layer_1:
                    try:
                        paths.remove(path)
                        paths.insert(order_change_path_index, path)
                    except ValueError as err:
                        Logger.pyprint('ERRO', '', f'Order change path error [{err}]', True)
                        
            print(current_exception)

        return paths

    
    @staticmethod
    def incompatibles(paths: list[Path], current_exception: list[str]):
        '''Check incompatibilities with multiple images/layers,
        This function supports images and layers in any order.

        Args:
            paths (list[Path]): List of all the paths used for one NFT.
            current_exception (list[str]): Current exception handled in the loop.

        Returns:
            list[Path] OR None: Valid list of path or None if an incompatibility is found.
        '''

        check_used_images = []
        incompatibles = current_exception[1:]
        layers = PathsHandling.get_layer_names_from_paths(paths)
        incomp_driver = len(incompatibles)
        
        # Error catching
        if incomp_driver < 2:
            Logger.pyprint('ERRO', '', f'Wrong incompatible arguments: {current_exception}', True)
            return None
        
        for incompatible in incompatibles:
            if incompatible in layers:
                images = PathsHandling.get_paths_from_layer_name(paths, incompatible)
                images = PathsHandling.get_filenames_from_paths(images)
            else:
                images = [incompatible]
                
            for image in images:
                is_used = PathsHandling.get_index_in_paths_list_from_filename(paths, image)
                
                if is_used is not None:
                    check_used_images.append(True)
                else:
                    check_used_images.append(False)
        
        # Mark the image as invalid by erasing the paths list
        if len(check_used_images) == incomp_driver and (False not in check_used_images):
            return None
                
        return paths
    
    
    @staticmethod
    def delete(paths: list[Path], current_exception: list[str]) -> list[Path]:
        '''Delete all the layers listed (for a full suit etc..)
        if the image (first argument) is used.

        Args:
            paths (list[Path]): List of all the paths used for one NFT.
            current_exception (list[str]): Current exception handled in the loop.

        Returns:
            list[Path]: Modified list of paths.
        '''
        
        image_path_index = PathsHandling.get_index_in_paths_list_from_filename(paths, current_exception[1])
        
        if image_path_index is not None:
            layers_to_delete = current_exception[2:]
            driver = len(layers_to_delete)
            
            for i in range(driver):
                paths = PathsHandling.delete_paths_from_layer_name(paths, layers_to_delete[i])
        
            Logger.pyprint('INFO', '', 'Layer(s) successfully deleted')
        
        return paths
            
            
    @staticmethod
    def delete_accessory(paths: list[Path], current_exception: list[str]) -> list[Path]:
        '''Works exactly like the 'delete' function, excepts that it destroys
        the image (first argument) instead of the layer(s) (Specially used for accessories).
        
        Args:
            paths (list[Path]): List of all the paths used for one NFT.
            current_exception (list[str]): Current exception handled in the loop.
        
        Returns:
            list[Path]: Modified list of paths.
        '''
        
        image_path_index = PathsHandling.get_index_in_paths_list_from_filename(paths, current_exception[1])
        
        if image_path_index is not None:
            layers_to_check = current_exception[2:]
            driver = len(layers_to_check)
            
            for i in range(driver):
                paths_from_layer = PathsHandling.get_paths_from_layer_name(paths, layers_to_check[i])
                
                if len(paths_from_layer) > 0:
                    del paths[image_path_index]
                    break
        
        return paths


    @staticmethod
    def exceptions_handling(background: Path, paths: list[Path], settings: CharacterSettings):
        '''Handle multiple exceptions/incompatibilities between images/layers.
        This main function ensure that the paths list is valid.
        
        Check the documentation: https://github.com/ostra-project/Advanced-NFTs-Generator
        - 'ORDER_CHANGE' -> Change the order between two layers/images.
        - 'INCOMPATIBLE' -> NFT is regenerated if the test is not passed.
        - 'DELETE' -> Deletes all the images of specific layers if the specified image is used.
        - 'DELETE_ACCESSORY' -> Deletes the image if all the layers are used.

        Args:
            background (Path): The path of the background
            paths (list[Path]): Randomized character paths list.
            settings (CharacterSettings): Link to the settings.
            
        Returns:
            list[Path] OR None: Modified paths list. (Or None if the NFT needs to be regenerated)
        '''

        # Add the background to the paths list (POS 0)
        # So the background is included into the exceptions handling
        paths.insert(0, background)
    
        exceptions = settings.exceptions
        exceptions_driver = len(exceptions)
        
        for i in range(exceptions_driver):
            current_exception = exceptions[i]
            
            # Error catching
            if len(current_exception) < 3:
                if not GlobalSettings.dist_mode:
                    print('')
                    
                err = textwrap.dedent(f'''\
                Wrong number of arguments for {current_exception}.
                Check the documentation: https://github.com/ostra-project/Advanced-NFTs-Generator
                
                NOTE: THIS EXCEPTION WILL BE IGNORED.
                ''')
                
                Logger.pyprint('WARN', '"ORDER_CHANGE"', err, True)
                
            else:
                # Order change exception (Returns the default 'paths' var if unavailable)
                if current_exception[0] == GlobalSettings.exceptions_list[0]:
                    # Error catching
                    paths = ExceptionsHandling.order_change(paths, current_exception)
                    
                # Incompatibility exception (Returns None to regenerate the NFT)
                elif current_exception[0] == GlobalSettings.exceptions_list[1]:
                    paths = ExceptionsHandling.incompatibles(paths, current_exception)
                    
                    # If it's incompatible, it's not necessary to continue the exceptions handling
                    if paths is None:
                        break
                
                # Delete exception (Deletes multiple layers)
                elif current_exception[0] == GlobalSettings.exceptions_list[2]:
                    paths = ExceptionsHandling.delete(paths, current_exception)
                
                # Delete accessory exception (Exactly like 'delete' but it removes the image)
                elif current_exception[0] == GlobalSettings.exceptions_list[3]:
                    paths = ExceptionsHandling.delete_accessory(paths, current_exception)
                
                # Error
                else:
                    Logger.pyprint('ERRO', '', f'Invalid exception name in {current_exception}', True)
        
        return paths
