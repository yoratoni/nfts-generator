from pyostra import pyprint, LogTypes
from settings import CharacterSettings
from libs import PathsHandling

from copy import deepcopy
from pathlib import Path
from typing import Union

import random


class Randomization:
    '''Handles all the random NFT generation (list of paths).
    '''
    
    @staticmethod
    def path_from_layer(character_layers: dict, layer_name: str) -> Union[Path, None]:
        '''Returns a random path of a certain layer from a dict of paths, this dict can be obtained
        with the "LayerPaths.scan_character_layers()" function.

        Args:
            character_layers (dict): Dictionary of paths where the keys are the layer names.
            layer_name (str): The name of the layer used to get a random path.

        Returns:
            Union[Path, None]: Random path from one layer or None if invalid layer name.
        '''
        
        if layer_name in character_layers.keys():
            paths = character_layers[layer_name]
            return paths[random.randrange(0, len(paths))]

        pyprint(LogTypes.ERROR, "Layer name not found inside character layers")


    @staticmethod
    def character(character_layers: dict, settings: CharacterSettings) -> list[Path]:
        '''Generate a random list containing all the traits used to generate an NFT.

        Args:
            character_layers (dict): Scanned dict of all the character's directory layers.
            settings (CharacterSettings): Link to the settings.

        Returns:
            list[Path]: List of all the traits (absolute paths) randomly generated.
        '''
        
        # Ensure that the dict used by this function is independent
        deep_layers = deepcopy(character_layers)
        