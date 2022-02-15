from pathlib import Path
from core import Logger

import os


class PathsHandling:
    '''Handles all the path operations for the NFTs.
    '''
    
    @staticmethod
    def get_structure(main_dir_path: Path, returns_full_path: bool = False) -> list:
        '''Get the files / sub-directories structure of a main directory.

        Args:
            main_dir_path (Path): Absolute path of the main directory that needs to be scanned.
            returns_full_path (bool, optional): If True, returns Path-type absolute path(s).

        Returns:
            list: List of Path / str.
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
            
        Logger.pyprint('DATA', '', f'Structure scanned [{main_dir_path}]')
        return scanned_structure
        
        
    @staticmethod
    def get_character_layers(character_dir_path: Path) -> dict:
        '''Returns a dict that contains all the layers of a character.

        Args:
            character_dir_path (Path): Absolute path to the character directory.

        Returns:
            dict: (Keys: layers) values: Dictionary of files (absolute path).
        '''
        
        directories = PathsHandling.get_structure(character_dir_path, True)
        layers_dict = {}
        driver = len(directories)
        
        for i in range(driver):
            dir_name = os.path.basename(directories[i])
            layers_dict[dir_name] = PathsHandling.get_structure(directories[i], True)
            
        Logger.pyprint('INFO', '', 'Character layers scanned')
        return layers_dict
        
        
    @staticmethod
    def get_index_in_paths_list_from_filename(paths: list[Path], filename: str) -> int:
        '''Get the index of a filename inside a Path list.

        Args:
            paths (list[Path]): List of Path.
            filename (str): Name of the file to check.
            
        Returns:
            int: Index of the file in the list or None if not found.
        '''
        
        drv = len(paths)
        
        for i in range(drv):
            current_name = os.path.basename(paths[i])
            if current_name == filename:
                return i
            
            
    @staticmethod
    def get_layer_names_from_paths(paths: list[Path]) -> list[str]:
        '''Get a list of all the layers name used by 'paths'.

        Args:
            paths (list[Path]): List of Path.

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
    def get_paths_from_layer_name(paths: list[Path], layer_name: str) -> list[Path]:
        '''Get a list of all the paths that are in specific layer
        from the list of all the character paths.

        Args:
            paths (list[Path]): List of Path.
            layer_name (str): Name of one of the character layers.

        Returns:
            list[Path]: Every path used in the paths list that is inside the layer.
        '''
        
        layer_paths = []
        driver = len(paths)
        
        for i in range(driver):
            current_path_layer_name = os.path.basename(paths[i].parent)
            
            if current_path_layer_name == layer_name:
                layer_paths.append(paths[i])
                
        return layer_paths
    
    
    @staticmethod
    def delete_paths_from_layer_name(paths: list[Path], layer_name: str) -> list[Path]:
        '''Deletes all the paths of a specific layer inside the paths list.

        Args:
            paths (list[Path]): List of Path.
            layer_name (str): Name of one of the character layers.

        Returns:
            list[Path]: Original paths list without all the paths of the specific layer.
        '''
        
        layer_paths = PathsHandling.get_paths_from_layer_name(paths, layer_name)
        driver = len(layer_paths)
        
        for i in range(driver):
            if layer_paths[i] in paths:
                path_index = paths.index(layer_paths[i])
                paths.pop(path_index)

        return paths


    @staticmethod
    def get_filename_from_paths(paths: list[Path]) -> str:
        '''Just a better wrapper to get multiple filenames
        from multiple paths (STRING FORMATTED)
        
        Args:
            paths (list): The paths list.
            
        Returns:
            str: The formatted list of all the filenames into a string with commas.
        '''
        
        driver = len(paths)
        filenames = ''
        
        for path in paths:
            # Get the filename & remove the '.png' extension
            name = os.path.basename(path)[:-4]
            
            # Format for only one name
            if driver == 1:
                filenames = name
            else:
                filenames += f'{name}, '
                
        # Fallback if the list is empty
        if driver == 0:
            filenames = 'Nothing'
            
        return filenames
