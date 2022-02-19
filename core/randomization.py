from core import PathsHandling, Logger
from settings import CharacterSettings
from pathlib import Path

import random


class Randomization:
    '''All the necessary functions used for the randomization of the paths.
    '''
    
    @staticmethod
    def random_path_from_layer_name(character_layers: dict, layer_name: str) -> Path:
        '''Returns a random path between all the files found inside one layer.

        Args:
            character_layers (dict): Dictionary that contains all the paths inside the character directory.
            layer_name (str): Name of one of the character layers where to get a random path.

        Returns:
            Path: Returns a random path from the list of paths inside one layer.
        '''
        
        paths = character_layers[layer_name]
        random_path = paths[random.randrange(0, len(paths))]
        
        return random_path
        
    
    @staticmethod
    def accessories(accessories: list[Path], settings: CharacterSettings) -> list[Path]:
        '''Generate a random list of accessories based on the max amount.

        Args:
            accessories (list[Path]): List of all the accessories path.
            settings (CharacterSettings): Link to the settings.

        Returns:
            list[Path]: List of random accessories absolute path.
        '''

        indexes = []
        random_accessories = []
        accessories_list_len = len(accessories)
        rarity_zero_driver = random.randrange(0, settings.accessories_rarity)
        
        if rarity_zero_driver == 0:
            rarity_driver = random.randrange(0, settings.max_accessories_amount)
            
            # Working with indexes instead of paths, to allow sorting (for the comparison hashlib)
            while len(indexes) < rarity_driver:
                random_accessory_index = random.randrange(0, accessories_list_len)
                
                # Check if the index is not already inside the list
                if random_accessory_index not in indexes:
                    indexes.append(random_accessory_index)
                    
            # Same order for comparison hashlib
            indexes.sort()
            
            # Add accessories path to the final list
            for i in range(rarity_driver):
                random_accessories.append(accessories[indexes[i]])
                
            Logger.pyprint('INFO', '', 'Random accessories generated')
            
        return random_accessories


    @staticmethod
    def duplicate(layer_images: list[Path], settings: CharacterSettings) -> list[Path]:
        '''Allows to modify the chances to use a specific image inside a list,
        it works by duplicating the element from it's filename and insert it multiple times.
        
        Example:
            ['path_2_filename.png', 3] -> [path_0, path_1, path_2, path_2, path_2].

        Args:
            layer_images (list[Path]): List of all the images path for one layer.
            settings (CharacterSettings): Link to the settings.

        Returns:
            list[Path]: Modified or not by this function.
        '''
        
        rarifier_driver = len(settings.image_rarifier)
        
        for i in range(rarifier_driver):
            current_instruction = settings.image_rarifier[i]
            
            # If the image is duplicated more than once
            # image_rarifier is the final amount of images
            if current_instruction[1] > 1:
                index = PathsHandling.get_index_in_paths_list_from_filename(
                            layer_images,
                            current_instruction[0]
                        )
                
                # If the image exists, insert it inside the existing list
                if index is not None:
                    for _ in range(current_instruction[1] - 1):
                        layer_images.insert(index, layer_images[index])

        return layer_images
    
    
    @staticmethod
    def character(character_layers: dict,  settings: CharacterSettings) -> list[Path]:
        '''Generate a random list of all the layers for one NFT.

        Args:
            character_layers (dict): Dictionary that contains all the paths inside the character directory.
            settings (CharacterSettings): Link to the settings.

        Returns:
            list[Path]: List of layers absolute path.
        '''

        keys = list(character_layers.keys())
        layers_driver = len(keys)
        character_paths = []
        
        for i in range(layers_driver):
            if keys[i] != settings.backgrounds_dir:
                if keys[i] != settings.accessories_dir:
                    raw_list = character_layers[keys[i]]
                    
                    # Add duplicated image paths to modify the chances to use one specific image
                    current_list = Randomization.duplicate(raw_list, settings)

                    # Rarity System: Add a randomization
                    # If the randomizer is equal to 0, include the optional layer
                    include_optional_layer = True
                    if keys[i] in settings.optional_layers:
                        index_of_rarity = settings.optional_layers.index(keys[i])
                        random_zero_driver = random.randrange(0, settings.optional_rarity[index_of_rarity])
                        
                        # Handles the randomization by checking is it's not equal to 0
                        if random_zero_driver != 0:
                            include_optional_layer = False
                    
                    # If included, add the optional image
                    if include_optional_layer:
                        random_driver = random.randrange(0, len(current_list))
                        character_paths.append(current_list[random_driver])
                else:
                    # Handles accessories separately inside the accessories() method
                    if settings.max_accessories_amount > 0:
                        character_paths += Randomization.accessories(character_layers[keys[i]], settings)
                    
        Logger.pyprint('INFO', '', 'Random character generated')
        return character_paths
    