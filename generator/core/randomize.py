from settings import CharacterSettings
from pyostra import pyprint, LogTypes
from core import GeneralPaths

from copy import deepcopy
from pathlib import Path
from typing import Union

import random


class Randomize:
    """Handles all the random NFT generation (list of paths).
    """
    
    @staticmethod
    def random_path_from_layer(character_layers: dict, layer_name: str) -> Union[Path, None]:
        """Returns a random path of a certain layer from a dict of paths, this dict can be obtained
        with the "LayerPaths.scan_character_layers()" function.

        Args:
            character_layers (dict): Dictionary of paths where the keys are the layer names.
            layer_name (str): The name of the layer used to get a random path.

        Returns:
            Union[Path, None]: Random path from one layer or None if invalid layer name.
        """
        
        if layer_name in character_layers.keys():
            paths = character_layers[layer_name]
            return paths[random.randrange(0, len(paths))]

        pyprint(LogTypes.ERROR, "Layer name not found inside character layers")


    @staticmethod
    def duplicate(layer_traits: list[Path], settings: CharacterSettings) -> list[Path]:
        """Allows to modify the chances to use a specific trait inside a list of trait paths.
        It works by duplicating the trait multiple times inside the list of traits.
            
        Example:
            ["path_2_filename.png", 3] -> [path_0, path_1, path_2, path_2, path_2].

        Args:
            layer_traits (list[Path]): List of all the traits in one layer.
            settings (CharacterSettings): Link to the settings ("trait_chances").

        Returns:
            list[Path]: The modified list of paths (or not if the trait is not found).
        """
        
        for trait in settings.trait_chances.keys():
            chance = settings.trait_chances[trait]

            # If the trait is duplicated more than once
            # "trait_chances" is the final amount of traits
            if chance > 1:
                index = GeneralPaths.get_filename_index_in_paths(layer_traits, trait)
                
                # If the trait exists, insert it inside the existing list
                if index is not None:
                    for _ in range(chance - 1):
                        layer_traits.insert(index, layer_traits[index])
                        
        return layer_traits


    @staticmethod
    def accessories(accessories: list[Path], settings: CharacterSettings) -> list[Path]:
        """Generates a random list of accessories based on the max amount and the rarity.
        
        Note:
            As the NFT comparison system uses hashes, the accessories needs to be sorted,
            that's why indexes are generated then linked with the paths.

        Args:
            accessories (list[Path]): List of all the accessories.
            settings (CharacterSettings): Link to the settings.

        Returns:
            list[Path]: Generated list of random accessories.
        """

        indexes = []
        random_accessories = []

        # Depending on the main accessories rarity
        if random.randrange(0, settings.accessories_rarity) == 0:
            amount = random.randrange(0, settings.max_accessories_amount)
            accessories_len = len(accessories)
            
            while len(indexes) < amount:
                index = random.randrange(0, accessories_len)
                
                if index not in indexes:
                    indexes.append(index)
            
            # Sorted for comparison with hashes    
            indexes.sort()
            
            # Link indexes with paths
            for index in indexes:
                random_accessories.append(accessories[index])
                
            pyprint(LogTypes.INFO, f"Random accessories generated ({amount})")
        
        return random_accessories
                


    @staticmethod
    def character(character_layers: dict, settings: CharacterSettings) -> list[Path]:
        """Generates a random list containing all the traits used to generate an NFT.

        Args:
            character_layers (dict): Scanned dict of all the character's directory layers.
            settings (CharacterSettings): Link to the settings.

        Returns:
            list[Path]: List of all the traits (absolute paths) randomly generated.
        """
        
        character_traits = []
        
        # Ensure that the dict used by this function is independent
        deep_layers = deepcopy(character_layers)
        
        for layer_name in deep_layers.keys():
            # Background is added under the generated character at the end
            if layer_name != settings.background_dir:
                if layer_name != settings.accessories_dir:
                    raw_traits = deep_layers[layer_name]
                    
                    # Add duplicated traits to the list (settings.trait_chances)
                    traits = Randomize.duplicate(raw_traits, settings)
                    
                    # Optional layers system
                    # If the randrange returns 0, include the optional layer
                    include_optional_layer = True
                    if layer_name in settings.optional_layers.keys():
                        if random.randrange(0, settings.optional_layers[layer_name]) != 0:
                            include_optional_layer = False
                        
                    # If the optional layer is included, add a random optional trait
                    if include_optional_layer:
                        character_traits.append(traits[random.randrange(0, len(traits))])
                else:
                    # If it is the accessories layer,
                    # Generates a list of accessories and add them to the character traits
                    if settings.max_accessories_amount > 0:
                        character_traits += Randomize.accessories(deep_layers[layer_name], settings)
                
        pyprint(LogTypes.INFO, "Random character traits generated")
        return character_traits
