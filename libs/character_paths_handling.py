from pathlib import WindowsPath
from libs import Logger

import os


class CharacterPathsHandling:
    '''Handles all the path operations for the NFTs.
    '''
    
    @staticmethod
    def get_structure(main_dir_path: WindowsPath, returns_full_path: bool = False) -> list:
        '''Get the files / sub-directories structure of a main directory.

        Args:
            main_dir_path: Absolute path of the main directory that needs to be scanned.
            returns_full_path: If True, returns WindowsPath-type absolute path(s).

        Returns:
            list: List of WindowsPath / str.
        '''
        
        data = os.listdir(main_dir_path)
        data_driver = len(data)
        scanned_structure = []
        
        for i in range(data_driver):
            if returns_full_path:
                current_name = (main_dir_path / data[i]).resolve()
            else:
                current_name = data[i]
                
            scanned_structure.append(current_name)
            
        Logger.pyprint(f'Structure scanned [{main_dir_path}]', 'DATA')
        return scanned_structure
        
        
    @staticmethod
    def get_character_layers(character_dir_path: WindowsPath) -> dict:
        '''Returns a dict that contains all the layers of a character.

        Args:
            character_dir_path: Absolute path to the character directory.

        Returns:
            dict: (Keys: layers) values: Dictionary of files (absolute path).
        '''
        
        directories = CharacterPathsHandling.get_structure(character_dir_path, True)
        layers_dict = {}
        driver = len(directories)
        
        for i in range(driver):
            dir_name = os.path.basename(directories[i])
            layers_dict[dir_name] = CharacterPathsHandling(directories[i], True)
            
        Logger.pyprint('Character layers scanned', 'INFO')
        return layers_dict
        
        
    @staticmethod
    def get_index_in_paths_list_from_filename(paths: list[WindowsPath], filename: str) -> int:
        '''Get the index of a filename inside a WindowsPath list.

        Args:
            paths: List of WindowsPath.
            filename: Name of the file to check.
            
        Returns:
            int: Index of the file in the list or None if not found.
        '''
        
        drv = len(paths)
        
        for i in range(drv):
            current_name = os.path.basename(paths[i])
            if current_name == filename:
                return i
            
            
    @staticmethod
    def get_layer_names_from_paths(paths: list[WindowsPath]) -> list[str]:
        '''Get a list of all the layers name used by 'paths'.

        Args:
            paths: List of WindowsPath.

        Returns:
            list[str]: Name of all the layers used in 'paths'.
        '''
        
        layers = []
        driver = len(paths)
        
        for i in range(driver):
            current_layer = os.path.basename(paths[i].parent)
            if current_layer not in layers:
                layers.append(current_layer)
        
        return layers


    @staticmethod
    def get_paths_from_layer_name(paths: list[WindowsPath], layer_name: str) -> list[WindowsPath]:
        '''Get a list of all the paths that are in specific layer
        from the list of all the character paths.

        Args:
            paths: List of WindowsPath.
            layer_name: Name of one of the character layers.

        Returns:
            list[WindowsPath]: Every path used in the paths list that is inside the layer.
        '''
        
        layer_paths = []
        driver = len(paths)
        
        for i in range(driver):
            current_path_layer_name = os.path.basename(paths[i].parent)
            
            if current_path_layer_name == layer_name:
                layer_paths.append(paths[i])
                
        return layer_paths
