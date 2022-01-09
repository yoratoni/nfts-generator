from colorama import Style, Fore
from pathlib import WindowsPath
from hashlib import sha1
from PIL import Image
import random
import time
import os


class Printer:
    DEBUG_MODE = True
    DEBUG_TYPE = ['INFO', 'DATA', 'WARN', 'ERRO']

    @staticmethod
    def pyprint(msg: str, title: str, forced: bool = False):
        '''Debug Mode formatted print statements 
        Supported colors: 'INFO', 'DATA', 'WARN', 'ERRO'
        '''
        
        if Printer.DEBUG_MODE or forced:
            color = Fore.WHITE
            
            if title == Printer.DEBUG_TYPE[0]:
                color = Fore.GREEN
            elif title == Printer.DEBUG_TYPE[1]:
                color = Fore.LIGHTBLUE_EX
            elif title == Printer.DEBUG_TYPE[2]:
                color = Fore.YELLOW
            elif title == Printer.DEBUG_TYPE[3]:
                color = Fore.RED

            output_title = f'{color}__{title}__{Style.RESET_ALL}'
            output_msg = f'{color}{msg}{Style.RESET_ALL}'
            
            print(f'{output_title} >>> {output_msg}')


    @staticmethod
    def extime(timer: int):
        '''Automatic timer format (ns, µs, ms and s units)'''

        timer = (time.time_ns() - timer)
        units = ['ns', 'µs', 'ms', 's']
        powers = [10**3, 10**6, 10**9]
        res = 0
        i = 0
        
        if timer < powers[0]:
            res = timer
        elif powers[0] <= timer < powers[1]:
            res = timer / powers[0]
            i = 1
        elif powers[1] <= timer < powers[2]:
            res = timer / powers[1]
            i = 2
        elif powers[2] <= timer:
            res = timer / powers[2]
            i = 3
        
        Printer.pyprint(f'Execution Time: {res}{units[i]}', 'WARN', True)
        

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
        
        Printer.pyprint(f'Structure scanned [{folder_path}]', 'DATA')
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
        
        Printer.pyprint('Scanned character layers', 'INFO')
        return character_layers_dict
    
    
    @staticmethod
    def character_from_list(random_character_paths: list) -> Image.Image:
        '''Returns an image containing all the images from 'random_character_paths'
        added to the first image of the list

        Args:
            random_character_paths: List of absolute path images randomly generated

        Returns:
            img: Final character
        '''
        
        img = Image.open(random_character_paths[0])
        drv = len(random_character_paths)
        
        for i in range(1, drv):
            layer = Image.open(random_character_paths[i])
            img.paste(layer, (0, 0), layer)
            
        Printer.pyprint('Merged images into character', 'INFO')
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
        
        Printer.pyprint('Character merged to the background', 'INFO')
        return bck


    @staticmethod
    def get_index_in_paths_from_filename(paths: list, filename: str) -> int:
        '''Get the index of a filename inside a WindowsPath list

        Args:
            paths: List of WindowsPath
            filename: Name of the file to check

        Returns:
            i: Index of the file in the list or None if not found
        '''
        
        drv = len(paths)
        
        for i in range(drv):
            curr_name = os.path.basename(paths[i])
            if curr_name == filename:
                return i


    @staticmethod
    def exception_handling(exceptions_list: list, paths: list) -> list:
        '''Handle multiple exceptions / incompatibilites between layers

        Args:
            exceptions_list: List of all the exceptions (Check parameters.py)
            paths: Original character paths list

        Returns:
            paths: Modified paths list
        '''
        
        drv = len(exceptions_list)
        
        for i in range(drv):
            curr_exception = exceptions_list[i]
            
            # Change the order between two layers
            if curr_exception[0] == 'ORDER_CHANGE':
                first_path_i = NFT.get_index_in_paths_from_filename(paths, curr_exception[1])
                second_path_i = NFT.get_index_in_paths_from_filename(paths, curr_exception[2])
                
                if first_path_i is not None and second_path_i is not None:
                    saved_path = paths[first_path_i]
                    paths.pop(first_path_i)
                    paths.insert(second_path_i, saved_path)
            
            # Incompatible layers
            elif curr_exception[0] == 'INCOMPATIBLE':
                incomp_list = curr_exception[1:]
                incomp_number = len(incomp_list)
                incomp_paths = []
            
                for i in range(incomp_number):
                    curr_path_i = NFT.get_index_in_paths_from_filename(paths, incomp_list[i])
                    incomp_paths.append(curr_path_i)
                
                # Regenerate the NFT is the images are all used
                if None not in incomp_paths:
                    return None

        Printer.pyprint('Exceptions handled successfully', 'INFO')
        return paths


    @staticmethod
    def generate_unique_nft(
        settings,
        character_layers: dict,
        backgrounds_folder_path: WindowsPath,
        output_and_name_path: WindowsPath
    ):
        '''Generate an unique NFT (compared to others with a SHA1 hash)

        Args:
            settings: Settings class
            character_layers: All the layers of this character using get_character_layers()
            backgrounds_folder_path: Absolute path of the background folder
            output_and_name_path: Full path (Path + Name + '.png') where to save the NFT
        '''

        # Multiple NFTs comparison system
        while True:
            # Generate a random background path
            background = Randomize.random_path_from_folder(backgrounds_folder_path)
            
            # Generate a random character (List of random paths)
            character = Randomize.character(
                character_layers,
                settings.accessories_folder,
                settings.optional_layers,
                settings.optional_rarity,
                settings.max_accessories_amount
            )

            # Exception Handling
            character = NFT.exception_handling(settings.exceptions, character)

            # Comparison hash generation
            bytecode = bytes(f'{background}__{character}', encoding = 'utf-8')
            str_hash = sha1(bytecode).hexdigest()
            
            # If character is valid and the hash is unique, save it and break the while
            if character is not None and str_hash not in NFT.NFT_COMPARISON_HASHES:
                NFT.NFT_COMPARISON_HASHES.append(str_hash)
                break
            
            Printer.pyprint(f'Duplicata of an NFT found [{str_hash}]', 'WARN')

        # # Generate the image of the character 
        character_image = NFT.character_from_list(character)
        
        # # Merge the background and the character image
        final_nft = NFT.merge_character_to_background(character_image, background)
        
        # # Save the image
        Printer.pyprint(f'Saved NFT [{output_and_name_path}]', 'DATA', True)
        final_nft.save(output_and_name_path)


    @staticmethod
    def generate_nfts(
        number_of_nfts: int,
        nft_names: str,
        settings,
        character_path: WindowsPath,
        backgrounds_folder_path: WindowsPath,
        output_folder_path: WindowsPath
    ):
        '''Generate all the NFTs for a character

        Args:
            number_of_nfts: Total number of NFTs for this character
            nft_names: Default name (coupled to a number)
            settings: Link to the settings in parameters.py
            character_path: Path to the character layers folder
            backgrounds_folder_path: Path to the backgrounds folder
            output_folder_path: Path to the output folder
        '''
        
        # Save the time where it starts
        time_start = time.time_ns()
        
        # Get the number of zeros for zfill()
        zeros = len(str(number_of_nfts))
        
        # Get all the images and the layers
        layers = NFT.get_character_layers(character_path)
        
        # Generate every NFT with a name based on 'i' and zfill()
        for i in range(number_of_nfts):
            curr_name = f'{nft_names}{str(i).zfill(zeros)}.png'
            nft_path = (output_folder_path / curr_name).resolve()
            NFT.generate_unique_nft(settings, layers, backgrounds_folder_path, nft_path)
        
        # Print the total time that it took
        Printer.extime(time_start)
        

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

        Printer.pyprint('Random accessories generated', 'INFO')
        return accessories_paths_list

    
    @staticmethod
    def character(
        character_layers: dict,
        accessories_folder: str,
        optional_layers: list,
        optional_rarity: int,
        max_accessories_amount: int
    ) -> list[WindowsPath]:
        '''Generate a random list of all tha layers for one NFT

        Args:
            character_layers: Dictionary generated with NFT.get_character_layers()
            accessories_folder: Ignored accessories folder
            optional_layers: List of optional layers
            optional_rarity: Rarity of optional layers
            max_accessories_amount: Max amount of accessories

        Returns:
            character_paths: List of layers absolute path
        '''
        
        keys = list(character_layers.keys())
        layers_lens = [len(character_layers[name]) for name in keys]
        number_of_layers = len(layers_lens)
        character_paths_list = []
        
        # All layers dict
        for i in range(number_of_layers):
            if keys[i] != accessories_folder:
                curr_list = character_layers[keys[i]]
                
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
                    character_paths_list += Randomize.accessories(character_layers[keys[i]], max_accessories_amount)

        Printer.pyprint('Random character generated', 'INFO')
        return character_paths_list


    @staticmethod
    def random_path_from_folder(folder: list[WindowsPath]) -> WindowsPath:
        '''Returns a random path between all the files found inside the folder

        Args:
            folder: list of all the files (full absolute path)

        Returns:
            random_file[drv]: Returns a random path
        '''
        
        random_file = NFT.get_structure(folder, True)
        drv = random.randrange(0, len(random_file))
        
        Printer.pyprint(f'Random path generated [{random_file[drv]}]', 'DATA')
        return random_file[drv]
