from pathlib import WindowsPath
from hashlib import sha1
from PIL import Image
import random
import os


class NFT:
    # Save an hash of all the paths of an NFT
    # Used to compare multiple NFTs
    NFT_COMPARISON_HASHES = []
    
    
    @staticmethod
    def get_structure(folder_path: WindowsPath, returns_full_path: bool = False) -> list:
        '''Get the file / folder structure of a folder

        Args:
            folder_path: Absolute path of the folder that needs to be scanned
            returns_full_path: If True, returns WindowsPath-type absolute path(s)

        Returns:
            scanned: List of WindowsPath / str
        '''
        
        data = os.listdir(folder_path)
        drv = len(data)
        scanned = []
        
        for i in range(drv):
            if returns_full_path:
                curr_name = (folder_path / data[i]).resolve()
            else:
                curr_name = data[i]
                
            scanned.append(curr_name)
            
        return scanned
    
    
    @staticmethod
    def get_character_layers(character_main_folder_path: WindowsPath) -> dict:
        '''Returns a dict that contains all the layers of a character

        Args:
            character_main_folder_path: Absolute path to the character

        Returns:
            character_layers_dict: Keys: layers, values: Dictionary of files (absolute path)
        '''
        
        folders = NFT.get_structure(character_main_folder_path, True)
        drv = len(folders)
        character_layers_dict = {}
        
        for i in range(drv):
            folder_name = os.path.basename(folders[i])
            character_layers_dict[folder_name] = NFT.get_structure(folders[i], True)
            
        return character_layers_dict
    
    
    @staticmethod
    def character_from_list(list_of_character_layers: list) -> Image.Image:
        '''Returns an image containing all the layers from 'list_of_character_layers'

        Args:
            list_of_character_layers: List of absolute path layers

        Returns:
            img: Final character
        '''
        
        img = Image.open(list_of_character_layers[0])
        drv = len(list_of_character_layers)
        
        for i in range(1, drv):
            layer = Image.open(list_of_character_layers[i])
            img.paste(layer, (0, 0), layer)
            
        return img
    
    
    @staticmethod
    def merge_character_to_background(character_image: Image.Image, background_path: WindowsPath) -> Image.Image:
        '''Merge the randomly generated character to a background

        Args:
            character_image: Image of the generated character
            background_path: Full absolute path of the background

        Returns:
            bck: Image of the full NFT
        '''
        
        bck = Image.open(background_path)
        bck.paste(character_image, (0, 0), character_image)
        return bck


    @staticmethod
    def generate_unique_nft(
        settings,
        backgrounds_folder_path: WindowsPath,
        character_folder_path: WindowsPath,
        output_full_path: WindowsPath
    ):
        '''Generate an unique NFT (compared to others with a SHA1 hash)

        Args:
            settings: Settings class
            backgrounds_folder_path: Absolute path of the background folder
            character_folder_path: Absolute path of the choosed character folder
            output_full_path: Full path (Path + Name + '.png') where to save the NFT
        '''
        
        # Get all the layers of the character
        layers = NFT.get_character_layers(character_folder_path)
        
        # Multiple NFTs comparison system
        while True: 
            # Generate a random background path
            background = Randomize.background(backgrounds_folder_path)
            
            # Generate a random character (List of random paths)
            character = Randomize.character(
                layers,
                settings.accessories_folder,
                settings.optional_layers,
                settings.optional_rarity,
                settings.max_accessories_amount
            )
            
            # Comparison hash generation
            bytecode = bytes(f'{background}__{character}', encoding = 'utf-8')
            str_hash = sha1(bytecode).hexdigest()
            
            # If the hash is unique, save it and break
            if str_hash not in NFT.NFT_COMPARISON_HASHES:
                NFT.NFT_COMPARISON_HASHES.append(str_hash)
                break

        # Generate the image of the character 
        character_image = NFT.character_from_list(character)
        
        # Merge the background and the character image
        final_nft = NFT.merge_character_to_background(character_image, background)
        
        # Save the image
        final_nft.save(output_full_path)


class Randomize:
    @staticmethod
    def accessories(list_of_accessories: list[WindowsPath], max_accessories_amount: int) -> list[WindowsPath]:
        '''Generate a random list of accessories based on the max amount

        Args:
            list_of_accessories: List of all the accessories
            max_accessories_amount: Max amount of accessories

        Returns:
            accessories_paths_list: List of random accessories absolute path
        '''
        
        added_indexes = []
        accessories_paths_list = []
        drv = len(list_of_accessories)
        randomizer = random.randrange(0, max_accessories_amount)
        
        while len(added_indexes) < randomizer:
            random_accessory_index = random.randrange(0, drv)
            
            # Checked if the index is not already inside of the list
            if random_accessory_index not in added_indexes:
                added_indexes.append(random_accessory_index)
                
        # For comparison hashing
        # Every list should be in the same order
        added_indexes.sort()

        # Add accessories path to the list
        for i in range(randomizer):
            curr_path = list_of_accessories[added_indexes[i]]
            accessories_paths_list.append(curr_path)

        return accessories_paths_list
    
    
    @staticmethod
    def character(
        randomized_character: dict,
        accessories_folder: str,
        optional_layers: list,
        optional_rarity: int,
        max_accessories_amount: int
    ) -> list[WindowsPath]:
        '''Generate a random list of all tha layers for one NFT

        Args:
            randomized_character: Dictionary generated with NFT.get_character_layers()
            accessories_folder: Ignored accessories folder
            optional_layers: List of optional layers
            optional_rarity: Rarity of optional layers
            max_accessories_amount: Max amount of accessories

        Returns:
            character_paths: List of layers absolute path
        '''
        
        keys = list(randomized_character.keys())
        layers_lens = [len(randomized_character[name]) for name in keys]
        number_of_layers = len(layers_lens)
        character_paths_list = []
        
        # All layers dict
        for i in range(number_of_layers):
            if keys[i] != accessories_folder:
                curr_list = randomized_character[keys[i]]
                
                # Rarity System
                include = True
                if keys[i] in optional_layers:
                    rnd_optional = random.randrange(0, optional_rarity)
                    if rnd_optional != 0:
                        include = False
                
                # Add random image path if included
                if include:
                    rnd = random.randrange(0, layers_lens[i])
                    character_paths_list.append(curr_list[rnd])
            else:
                # Add accessories separately
                if max_accessories_amount > 0:
                    character_paths_list += Randomize.accessories(randomized_character[keys[i]], max_accessories_amount)

        return character_paths_list


    @staticmethod
    def background(backgrounds_list: list[WindowsPath]) -> WindowsPath:
        '''Randomize a background and returns a WindowsPath of the background

        Args:
            backgrounds_list: list of all the backgrounds (full absolute path)

        Returns:
            backgrounds[drv]: Random background full absolute path 
        '''
        
        backgrounds = NFT.get_structure(backgrounds_list, True)
        drv = random.randrange(0, len(backgrounds))
        return backgrounds[drv]
