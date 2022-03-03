from settings import (
    GlobalSettings,
    CharacterSettings,
    ElonSettings,
    JeffSettings,
    RichardSettings
)

from core import (
    Logger,
    PathsHandling,
    Randomization,
    ExceptionsHandling,
    MetadataHandling
)

from typing import Union
from copy import deepcopy
from pathlib import Path
from PIL import Image

import contextlib
import textwrap
import xxhash
import time
import sys
import os
import io


class Generator:
    # Hashlib containing xxHash hashes
    # Every hash is made with all the paths used in one image
    # Allows comparison between images without generating them
    nft_comparator_hashlib = []
    

    @staticmethod
    def final_nft_from_paths(paths: list[Path]) -> Image.Image:
        '''Returns an image containing all the layers in the paths list.
        
        Note:
            All the images are added to the first image of the paths list.

        Args:
            paths (list[Path]): List of all the paths used for one NFT
            (The first of the list is the background).

        Returns:
            Image.Image: Final character.
        '''
        
        img = Image.open(paths[0]).convert('RGBA')
        paths_driver = len(paths)
        
        for i in range(1, paths_driver):
            layer = Image.open(paths[i]).convert('RGBA')
            
            try:
                img = Image.alpha_composite(img, layer)
            except ValueError as err:
                # Error during the superposition of the images
                err_format = textwrap.dedent(f'''\
                Alpha Composite error: {err},
                Between [{paths[0]}] and [{paths[i]}].
                Check the documentation: https://github.com/ostra-project/Advanced-NFTs-Generator
                
                NOTE: THIS EXCEPTION WILL BE IGNORED.
                ''')

                Logger.pyprint('ERRO', err_format, disable_function_name=True)

        # Info log
        Logger.pyprint('INFO', 'Merged background and character images')
        return img

    
    @staticmethod
    def generate_unique_nft(
        settings: CharacterSettings,
        character_layers: dict,
        output_path_and_name: Path,
        is_saving_system_enabled: bool
    ) -> list:
        '''Generate an unique NFT (compared to others with a xxHash128 hash).

        Args:
            settings (CharacterSettings): Link to the settings.
            character_layers (dict): All the layers of this character using get_character_layers().
            output_and_name_path (Path): Full path (Path + Name + '.png') where to save the NFT.
            is_saving_system_enabled (bool): (FOR TESTING ONLY) Remove the saving system.
            
        Returns:
            list (Position 0): Contains the metadata of the NFT (Mix of background & character).
            list (Position 1): Statistics about the generation
        '''
        
        # Measure some stats about the generation
        statistics = []
        iterations = 1
        
        # Deep copy of the character layers, ensure that this dict is independent everytime
        deep_character_layers = deepcopy(character_layers)
        
        # Multiple NFTs comparison system
        while True:
            # Generate a random background path
            background = Randomization.random_path_from_layer_name(
                            deep_character_layers,
                            settings.backgrounds_dir
                         )
            
            # Generate a random list of layers path for the character image
            character = Randomization.character(deep_character_layers, settings)
            
            # Exception Handling
            # Also handles the merging of the background and the character
            # So any background related exception is handled too
            final_paths = ExceptionsHandling.exceptions_handling(background, character, settings)
            
            # Comparison hash generation
            digest = f'::{final_paths}::'
            final_hash = xxhash.xxh128_hexdigest(digest).upper()
            
            # If the character exception handling is valid, break the while loop
            if final_paths is not None:
                # Info log
                Logger.pyprint('INFO', 'Exceptions handled successfully')
                
                if final_hash not in Generator.nft_comparator_hashlib:
                    Generator.nft_comparator_hashlib.append(final_hash)
                    
                    # Info log
                    Logger.pyprint('INFO', f'Hashlib comparison address generated')
                    break
                
                # Warning, duplicates found
                Logger.pyprint('WARN', f'Duplicate of an NFT found [0x{final_hash}]', disable_function_name=True)
            else:
                # The character paths will now be regenerated
                Logger.pyprint('ERRO', f'Invalid character, the NFT will be regenerated..', disable_function_name=True)
            
            # Measure the number of iterations per NFT
            iterations += 1
        statistics.append(iterations)
                
        if is_saving_system_enabled:
            # Generate the image of the character from the list (merged to the background)
            generated_nft = Generator.final_nft_from_paths(final_paths)
            generated_nft.save(output_path_and_name)
            
        # Print saved NFT path
        Logger.pyprint('SUCCESS', f'Saved NFT [{output_path_and_name}]')
        
        # Used for the metadata generation (Metadata bus)
        return [final_paths, statistics]
    
    
    @staticmethod
    def estimate_generation_time(
        iterations: int,
        character_name: str,
        settings: CharacterSettings,
        character_layers: dict
    ):
        '''Generates one random NFT and estimates the time
        that it would take to generate x number of NFTs.
        
        WARNING: This function is not accurate because the calculations are based on only one NFT,
        where the complexity of the layers makes the generation time
        pretty different between two NFTs.
        '''
        
        # Estimation path
        cwd = os.path.dirname(__file__)
        character_path = Path(os.path.join(cwd, os.pardir, 'core', 'demo', 'LATENCY_CHECK_NFT.png'))

        precision = 4
        timer_start = time.perf_counter_ns()

        for _ in range(precision):
            # Block any call to the print function
            with contextlib.redirect_stdout(io.StringIO()):
                Generator.generate_unique_nft(settings, character_layers, character_path, True)
        
        timer_name = f'Estimated generation time for {iterations} NFTs of "{character_name}"'
        iterations = iterations // precision
        
        if not GlobalSettings.dist_mode:
            print('')
            Logger.extime(timer_name, timer_start, iterations, True, True)
            print('')
            
        time.sleep(2)
    
    
    @staticmethod
    def get_character_settings(character_name: str) -> CharacterSettings:
        '''Obtains the character settings based on the string arg.

        Args:
            character_name (str): Name of the character (based on GlobalSettings).

        Returns:
            CharacterSettings: The settings class of the character.
        '''
        
        if character_name == GlobalSettings.character_dirs[0]:
            settings = ElonSettings
        elif character_name == GlobalSettings.character_dirs[1]:
            settings = JeffSettings
        elif character_name == GlobalSettings.character_dirs[2]:
            settings = RichardSettings
        else:
            # The name of the character is not included in the settings
            Logger.pyprint('ERRO', 'Invalid character name', disable_function_name=True)
            sys.exit()
        
        return settings
    
    
    @staticmethod
    def __multiple_nft_generation(
        iterations: int,
        character_name: str,
        debug_mode_latency: int = 0,
        is_saving_system_enabled: bool = True
    ) -> Union[list[int], None]:
        '''Generates a number of unique NFTs for a specified character.

        Args:
            iterations (int): Total number of NFTs for this character.
            character_name (str): Current generated character name.
            debug_mode_latency (int): If == 0, debug mode is disabled (Value exprimed in milliseconds).
            is_saving_system_enabled (bool, optional): (FOR TESTING ONLY) Remove the saving system.
            
        Returns:
            list[int]/None: The first value is the real number of iterations,
                            the second one is the value of the starting timer.
        '''
        
        # Main paths
        cwd = os.path.dirname(__file__)
        main_path = os.path.join(cwd, os.pardir, 'NFTs')
        metadata_path = os.path.join(main_path, 'metadata', character_name)
        character_path = Path(os.path.join(main_path, 'input', character_name))
        output_path = Path(os.path.join(main_path, 'output', character_name))
        
        settings = Generator.get_character_settings(character_name)
        final_iterations = 0
        timer_start = 0
        
        if os.path.exists(character_path) and os.path.exists(output_path) and os.path.exists(metadata_path):
            # Debugging mode handling
            if debug_mode_latency == 0:
                zeros = len(str(iterations))  # Get the number of zeros for zfill()
            else:
                debug_mode_latency /= 1000  # The latency is in ms
                zeros = 0  # Undeclared fallback variable
                
            # Get all the images and the layers
            character_layers = PathsHandling.get_character_layers(character_path)
            
            # Estimated generation time
            if debug_mode_latency == 0 and is_saving_system_enabled:
                Generator.estimate_generation_time(iterations, character_name, settings, character_layers)

            # Save the time where it starts
            timer_start = time.perf_counter_ns()
            
            # Generate every NFT with a name based on 'i' and zfill()
            for i in range(iterations):
                # Return to line for new NFT logs
                print('')
                
                if debug_mode_latency == 0:
                    nft_number = str(i).zfill(zeros)
                    current_name = f'{character_name.upper()}_{nft_number}.png'
                    nft_path = os.path.abspath(os.path.join(output_path, current_name))
                else:
                    # (FOR TESTING ONLY) Erase the previous NFT by saving with the same name
                    current_name = 'DEBUG_NFT.png'
                    nft_path = os.path.abspath(os.path.join(output_path, current_name))
                    
                    if i != 0:
                        time.sleep(debug_mode_latency)
                        
                # Generates an unique NFT and get the metadata from it (background/character dict)
                unique_nft_data = Generator.generate_unique_nft(
                                      settings,
                                      character_layers,
                                      nft_path,
                                      is_saving_system_enabled
                                  )

                # Generates the metadata as a JSON file
                MetadataHandling.generate_meta(
                    metadata_path,
                    unique_nft_data[0],
                    current_name,
                    settings
                )

                # Final number of iterations (Get the iterations var at pos 1/0)
                final_iterations += unique_nft_data[1][0]

            return [final_iterations, timer_start]
        else:
            # One of the path does not exists
            Logger.pyprint('ERRO', 'Invalid character path/output path', disable_function_name=True)

    
    @staticmethod
    def generate_nfts(
        iterations: int,
        character_name: str,
        debug_mode_latency: int = 0,
        is_saving_system_enabled: bool = True
    ) -> bool:
        '''This is the main wrapper for the NFT generation function,
        check the "__multiple_nft_generation()" private function for more info.

        Args:
            iterations (int): Total number of NFTs for this character.
            character_name (str): Current generated character name.
            debug_mode_latency (int, optional): If 0, debug mode disabled (Value in milliseconds).
            is_saving_system_enabled (bool, optional): (FOR TESTING ONLY) Remove the saving system.
            
        Returns:
            bool: only for multiprocessing purpose.
        '''

        # Args validity issue catcher
        if iterations <= 0:
            err = 'Invalid number of iterations'
            Logger.pyprint('ERRO', err)
            return False
        if character_name not in GlobalSettings.character_dirs:
            err = 'Invalid character name, check the class GlobalSettings inside the "settings.py" file'
            Logger.pyprint('ERRO', err)
            return False
        if debug_mode_latency < 0:
            err = 'Invalid debug mode latency (Value should be superior or equal to 0)'
            Logger.pyprint('ERRO', err)
            return False
        if type(is_saving_system_enabled) != bool:
            err = 'Invalid arg: "is_saving_system_enabled" should be a boolean'
            Logger.pyprint('ERRO', err)
            return False
                
        # Call the main private function
        try:
            generation_res = Generator.__multiple_nft_generation(
                iterations,
                character_name,
                debug_mode_latency,
                is_saving_system_enabled
            )
            
        # Multiple NFTs generation failed
        except Exception as err:
            err_format = f'Invalid nft generation: {err}'
            Logger.pyprint('ERRO', err_format, disable_function_name=True)
            return False
        
        if generation_res is not None:
            print('')
            
            # Print the total time that it took
            Logger.extime('NFTs generation time', generation_res[1])

            # Statistic logs
            generation_complexity = round(((generation_res[0] / iterations) - 1) * 100, 1)
            comparison_haslib_size = sys.getsizeof(Generator.nft_comparator_hashlib)
            Logger.pyprint('DATA', f'Comparison hashlib: {comparison_haslib_size} bytes')
            Logger.pyprint('DATA', f'Total iterations: {generation_res[0]}')
            Logger.pyprint('DATA', f'Additional complexity: {generation_complexity}%')
            
            # Returns True (for multiprocessing purpose)
            return True

        return False
