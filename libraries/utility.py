from pathlib import WindowsPath
from pathlib import Path
from PIL import Image
import random
import os


class NFT:    
    @staticmethod
    def get_structure(input_path: WindowsPath, is_path: bool = False) -> list:
        '''Get the file / folder structure of a folder

        Args:
            input_path: Checked folder
            is_path: If True, returns WindowsPath-type full path

        Returns:
            res: List of WindowsPath / str
        '''
        
        data = os.listdir(input_path)
        drv = len(data)
        res = []
        
        for i in range(drv):
            if is_path:
                curr_name = (input_path / data[i]).resolve()
            else:
                curr_name = data[i]
                
            res.append(curr_name)
            
        return res
    
    
    @staticmethod
    def get_character_layers(character_path: WindowsPath) -> dict:
        '''Returns a dict that contains all the layers of a character

        Args:
            character_path: Absolute path to the character

        Returns:
            character_dict: Keys: layers, values: Dictionary of files (absolute path)
        '''
        
        folders = NFT.get_structure(character_path, True)
        drv = len(folders)
        character_dict = {}
        
        for i in range(drv):
            folder_name = os.path.basename(folders[i])
            character_dict[folder_name] = NFT.get_structure(folders[i], True)
            
        return character_dict
    
    
    @staticmethod
    def character_from_list(character_list: list) -> Image.Image:
        '''Returns an image containing all the layers from 'character_list'

        Args:
            character_list: List of absolute path layers

        Returns:
            img: Final character
        '''
        
        img = Image.open(character_list[0])
        drv = len(character_list)
        
        for i in range(1, drv):
            layer = Image.open(character_list[i])
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
    def generate_unique_nft(settings, nft_type: int, output_name: str):
        # Main paths
        cwd = Path(__file__).parent
        input_path = (cwd / settings.main_input_dir_path).resolve()
        output_path = (cwd / settings.main_output_dir_path).resolve()
        
        # Path to the background
        background_path = (input_path / settings.background_folder).resolve()
        
        # Path to the character
        directory = settings.character_folders[nft_type]
        character_path = (input_path / directory).resolve()
        
        # Get all the layers of the character
        layers = NFT.get_character_layers(character_path)
        
        # Generate a random background
        background = Randomize.background(background_path)
        
        # Generate a random character (List of random layers)
        character = Randomize.character(
            layers,
            settings.accessories_folder,
            settings.optional_layers,
            settings.optional_rarity,
            settings.max_accessories_amount
        )
        
        # Generate the image of the character 
        character_image = NFT.character_from_list(character)
        
        # Merge the background and the character image
        final_nft = NFT.merge_character_to_background(character_image, background)
        
        # Save the image
        output_full_path = (output_path / output_name).resolve()
        final_nft.save(output_full_path)


class Randomize:
    @staticmethod
    def accessories(accessories_list: list[WindowsPath], max_accessories_amount: int) -> list[WindowsPath]:
        '''Generate a random list of accessories based on the max amount

        Args:
            accessories_list: [description]
            max_accessories_amount: Max amount of accessories

        Returns:
            res: List of random accessories absolute path
        '''
        
        res = []
        indexes = []
        
        drv = len(accessories_list)
        randomizer = random.randrange(0, max_accessories_amount)
        
        while len(res) < randomizer:
            index = random.randrange(0, drv)
            
            if index not in indexes:
                res.append(accessories_list[index])
                indexes.append(index)

        return res
    
    
    @staticmethod
    def character(
        character_dict: dict,
        accessories: str,
        optional_layers: list,
        optional_rarity: int,
        max_accessories_amount: int
    ) -> list[WindowsPath]:
        '''Generate a random list of all tha layers for one NFT

        Args:
            character_dict: Dictionary generated with NFT.get_character_layers()
            accessories: Ignored accessories folder
            optional_layers: List of optional layers
            optional_rarity: Rarity of optional layers
            max_accessories_amount: Max amount of accessories

        Returns:
            character_list: List of layers absolute path
        '''
        
        keys = list(character_dict.keys())
        drv_list = [len(character_dict[name]) for name in keys]
        drv_len = len(drv_list)
        
        character_list = []
        
        # All layers dict
        for i in range(drv_len):
            if keys[i] != accessories:
                curr_list = character_dict[keys[i]]
                include = True
                
                # Rarity System
                if keys[i] in optional_layers:
                    rnd_optional = random.randrange(0, optional_rarity)
                    if rnd_optional != 0:
                        include = False
                
                if include:
                    rnd = random.randrange(0, drv_list[i])
                    character_list.append(curr_list[rnd])
            else:
                if max_accessories_amount > 0:
                    character_list += Randomize.accessories(character_dict[keys[i]], max_accessories_amount)

        return character_list


    @staticmethod
    def background(backgrounds_path: list[WindowsPath]) -> WindowsPath:
        '''Randomize a background and returns a WindowsPath of the background

        Args:
            backgrounds_path: list of all the backgrounds (full absolute path)

        Returns:
            bcks[drv]: Random background full absolute path 
        '''
        
        bcks = NFT.get_structure(backgrounds_path, True)
        drv = random.randrange(0, len(bcks))
        return bcks[drv]
