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

from pathlib import Path
from PIL import Image


import contextlib
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
    def final_nft_from_paths(paths: list[Path], background_path: Path) -> Image.Image:
        '''Returns an image containing all the layers in the paths list.
        
        Note:
            All the images are added to the first image of the paths list.

        Args:
            paths (list[Path]): List of all the paths used for one NFT.

        Returns:
            Image.Image: Final character.
        '''
        
        img = Image.open(background_path).convert('RGBA')
        paths_driver = len(paths)
        
        for i in range(paths_driver):
            layer = Image.open(paths[i]).convert('RGBA')
            
            try:
                img = Image.alpha_composite(img, layer)
            except ValueError as err:
                Logger.pyprint('ERRO', '', f'Alpha Composite error: {err}', True)
                Logger.pyprint('ERRO', '', f'Between [{paths[0]}] and [{paths[i]}]', True)
                
        Logger.pyprint('INFO', '', 'Merged background and character images')
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
        
        # Multiple NFTs comparison system
        while True:
            # Generate a random background path
            background = Randomization.random_path_from_layer_name(
                            character_layers,
                            settings.backgrounds_dir
                         )
            
            # Generate a random list of layers path for the character image
            character = Randomization.character(character_layers, settings)
            
            # Exception Handling
            character = ExceptionsHandling.exceptions_handling(character, settings)
            
            # Comparison hash generation
            digest = f'{background}::{character}'
            final_hash = xxhash.xxh128_hexdigest(digest)
            
            # If the character exception handling is valid, break the while loop
            if character is not None:
                Logger.pyprint('INFO', '', 'Exceptions handled successfully')
                if final_hash not in Generator.nft_comparator_hashlib:
                    Generator.nft_comparator_hashlib.append(final_hash)
                    break
                
                Logger.pyprint('WARN', '', f'Duplicata of an NFT found [{final_hash}]', True)
            else:
                Logger.pyprint('ERRO', '', f'Invalid character, the NFT will be regenerated..', True)
            
            # Measure the number of iterations per NFT
            iterations += 1
        statistics.append(iterations)
                
        if is_saving_system_enabled:
            # Generate the image of the character from the list (merged to the background)
            generated_nft = Generator.final_nft_from_paths(character, background)
            generated_nft.save(output_path_and_name)
            
        # Print saved NFT path
        Logger.pyprint('SUCCESS', '', f'Saved NFT [{output_path_and_name}]', True)
        
        # Used for the metadata generation (Metadata bus)
        character.append(background)
        return [character, statistics]
    
    
    @staticmethod
    def estimate_generation_time(
        iterations: int,
        character_name: str,
        settings: CharacterSettings,
        character_layers: dict
    ):
        '''Generates one random NFT and estimates the time
        that it would take to generate x number of NFTs.
        
        WARNING: This method is not accurate because the calculations are based on only one NFT,
        where the complexity of the layers makes the generation time
        pretty different between two NFTs.
        '''
        
        timer_start = time.perf_counter_ns()
        
        # Estimation path
        cwd = os.path.dirname(__file__)
        character_path = Path(os.path.join(cwd, os.pardir, 'core', 'demo', 'LATENCY_CHECK_NFT.png'))
        
        # Block any call to the print function
        with contextlib.redirect_stdout(io.StringIO()):
            Generator.generate_unique_nft(settings, character_layers, character_path, True)
        
        timer_name = f'Estimated generation time for {iterations} NFTs of "{character_name}"'
        
        print('')
        Logger.extime(timer_name, timer_start, iterations, True)
        print('')
        
        time.sleep(2)
    
    
    @staticmethod
    def generate_nfts(
        iterations: int,
        character_name: str,
        debug_mode_latency: int = 0,
        is_saving_system_enabled: bool = True
    ):
        '''Generates a number of unique NFTs for a specified character.

        Args:
            iterations (int): Total number of NFTs for this character.
            character_name (str): Current generated character name. 
            debug_mode_latency (int): If == 0, debug mode is disabled (Value exprimed in milliseconds).
            is_saving_system_enabled (bool, optional): (FOR TESTING ONLY) Remove the saving system.
        '''
        
        # Stats
        final_iterations = 0
        
        # Save the time where it starts
        timer_start = time.perf_counter_ns()
        
        # Main paths
        cwd = os.path.dirname(__file__)
        main_path = os.path.join(cwd, os.pardir, 'NFTs')
        metadata_path = os.path.join(main_path, 'metadata', character_name)
        character_path = Path(os.path.join(main_path, 'input', character_name))
        output_path = Path(os.path.join(main_path, 'output', character_name))
        
        if os.path.exists(character_path) and os.path.exists(output_path) and os.path.exists(metadata_path):
            # Debugging mode handling
            if debug_mode_latency == 0:
                zeros = len(str(iterations))  # Get the number of zeros for zfill()
            else:
                debug_mode_latency /= 1000  # The latency is in ms
                zeros = 0  # Undeclared fallback variable

            # Character parameters obtained from the name
            if character_name == GlobalSettings.character_dirs[0]:
                settings = ElonSettings
            elif character_name == GlobalSettings.character_dirs[1]:
                settings = JeffSettings
            elif character_name == GlobalSettings.character_dirs[2]:
                settings = RichardSettings
            else:
                Logger.pyprint('ERRO', '', 'Invalid character name', True)
                sys.exit()
            
            # Get all the images and the layers
            layers = PathsHandling.get_character_layers(character_path)
            
            # Estimated generation time
            if debug_mode_latency == 0 and is_saving_system_enabled:
                Generator.estimate_generation_time(iterations, character_name, settings, layers)
            
            # Generate every NFT with a name based on 'i' and zfill()
            for i in range(iterations):
                if debug_mode_latency == 0:
                    nft_number = str(i).zfill(zeros)
                    current_name = f'{character_name.upper()}_{nft_number}.png'
                    nft_path = os.path.abspath(os.path.join(output_path, current_name))
                else:
                    # (FOR TESTING ONLY) Erase the previous NFT by saving with the same name
                    current_name = 'DEBUG_NFT.png'
                    nft_path = os.path.abspath(os.path.join(output_path, current_name))
                    time.sleep(debug_mode_latency)

                # Generates an unique NFT and get the metadata from it (background / character dict)
                unique_nft_data = Generator.generate_unique_nft(
                                      settings,
                                      layers,
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
                
            # Print the total time that it took
            Logger.extime('NFTs generation time', timer_start)
            
            # Statistics
            generation_complexity = round((iterations / final_iterations) * 100, 2)
            comparison_haslib_size = sys.getsizeof(Generator.nft_comparator_hashlib)
            Logger.pyprint('DATA', '', f'Comparison hashlib: {comparison_haslib_size} bytes')
            Logger.pyprint('DATA', '', f'Total iterations: {final_iterations}')
            Logger.pyprint('DATA', '', f'General complexity: {generation_complexity}%')
            
            # Returns True (for multiprocessing purpose)
            return True
        
        else:
            Logger.pyprint('ERRO', '', 'Invalid character path / output path', True)
            return False
        