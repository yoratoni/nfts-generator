from pyostra import pyprint, LogTypes
from libs import PathsHandling
from pathlib import Path
from typing import Union

import os


class LayerPaths:
    '''Handles all the path operations related to the full path list used in an NFT.
    '''
    
    @staticmethod
    def scan_character_layers(character_dir_path: Path) -> dict:
        '''Returns a dict that contains all the layers of a character,
        it also includes all the filenames as the values of the dict.

        Args:
            character_dir_path (Path): The path of the character directory.

        Returns:
            dict: [Key: layer name][Value: List of files]
        '''
        
        final_dict = {}
        layers = PathsHandling.get_structure(character_dir_path, True)
        
        for layer in layers:
            curr_layer = os.path.basename(layer)
            final_dict[curr_layer] = PathsHandling.get_structure(layer, True)
            
        return final_dict
    
  
    @staticmethod
    def get_layer_names_from_paths(paths: list[Path]) -> list[str]:
        '''Returns a list of all the layers used by this list of paths.
        
        Note:
            The returned values are just the names of the layers.

        Args:
            paths (list[Path]): The main list of paths.

        Returns:
            list[str]: List of all the layers.
        '''
        
        layers = []
        
        for path in paths:
            curr_layer = os.path.basename(path.parent)
            
            if curr_layer not in layers:
                layers.append(curr_layer)
                
        return layers
    
    
    @staticmethod
    def get_paths_from_layer_name(paths: list[Path], layer_name: str) -> list[Path]:
        '''Returns a list of all the paths that are in a specific layer
        by scanning the main paths list.

        Args:
            paths (list[Path]): The main list of paths.
            layer_name (str): The name of the layer.

        Returns:
            list[Path]: A list of all the paths that are in this layer.
        '''
        
        layer_paths = []
        
        for path in paths:
            curr_layer = os.path.basename(path.parent)
            
            if curr_layer == layer_name:
                layer_paths.append(path)
                
        return layer_paths
    
    
    @staticmethod
    def delete_paths_from_layer_name(paths: list[Path], layer_name: str) -> list[Path]:
        '''Deletes all the paths of a specific layer inside the paths list/

        Args:
            paths (list[Path]): The main list of paths.
            layer_name (str): The name of the layer.

        Returns:
            list[Path]: Original paths list without all the paths of the specific layer.
        '''
    
        layer_paths = LayerPaths.get_paths_from_layer_name(paths, layer_name)
        
        for layer_path in layer_paths:
            if layer_path in paths:
                paths.pop(paths.index(layer_path))
                
        return paths
