from pathlib import WindowsPath
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
            list: List of WindowsPath / str
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
            character_dict: Keys: layers, values: List of files (absolute path)
        '''
        
        folders = NFT.get_structure(character_path, True)
        drv = len(folders)
        character_dict = {}
        
        for i in range(drv):
            folder_name = os.path.basename(folders[i])
            character_dict[folder_name] = NFT.get_structure(folders[i], True)
            
        return character_dict


class Randomize:
    @staticmethod
    def accessories(accessories_list: list[WindowsPath], tendency: float) -> list[WindowsPath]:
        '''Generate a random list of accessories based on the tendency

        Args:
            accessories_list: [description]
            tendency: Reduce the random number of accessories (Between 1 & 2)

        Returns:
            list: [description]
        '''
        
        res = []
        indexes = []
        
        drv = len(accessories_list)
        rounder = round((drv + 1) / tendency)
        randomizer = random.randrange(1, rounder)
        
        while len(res) < randomizer:
            index = random.randrange(0, drv)
            
            if index not in indexes:
                res.append(accessories_list[index])
                indexes.append(index)

        return res
    
    
    @staticmethod
    def character(character_dict: dict) -> list[WindowsPath]:
        keys = list(character_dict.keys())
        drv_list = [len(character_dict[name]) for name in keys]
        
        print(drv_list)


class Testing:
    IMG_SIZE = 1024
    SQUARE_SIZE = 64
    
    @staticmethod
    def generate_colored_square(img: Image.Image, size: int):
        '''Generate a colored square randomly place on the image'''
        
        random_color = tuple([random.randrange(0, 255) for _ in range(3)] + [255])

        rand_x_start = random.randrange(0, Testing.IMG_SIZE - size)
        rand_y_start = random.randrange(0, Testing.IMG_SIZE - size)
        rand_x_end = rand_x_start + size
        rand_y_end = rand_y_start + size
        
        for x in range(rand_x_start, rand_x_end):
            for y in range(rand_y_start, rand_y_end):
                img.putpixel((x, y), random_color)
    

    @staticmethod
    def generate_random_images(relative_path: str, n: int, start_name_index: int = 0):
        '''Generate an image of 1024x1024 with a colorized square in it'''
        
        for i in range(n):
            zfilled = str(i + start_name_index).zfill(3)
            full_path = f'{relative_path}/IMG_{zfilled}.png'
            
            img = Image.new('RGBA', (Testing.IMG_SIZE, Testing.IMG_SIZE), 0)
            Testing.generate_colored_square(img, Testing.SQUARE_SIZE)
            img.save(full_path, 'PNG')
