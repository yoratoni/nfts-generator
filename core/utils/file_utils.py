from core import Logger

import random
import xxhash
import json
import os


class NFTsUtils:
    '''This class contains file-related functions
    for the final preparation of NFTs for OpenSea.
    '''

    @staticmethod
    def __verify_metadata_attributes(metadata_path: os.path, filenames: list[str]) -> bool:
        '''This function is used to verify that every metadata file is unique
        (By checking the "attributes" key and doing an hash comparison).
        
        Args:
            directory_name (str, optional): The name of the directory where all the final NFTs are.
            
        Returns:
            bool: True if all the metadata files contains unique metadata attributes.
        '''
        
        comparison_hashlib = []
        verified = True
        
        for filename in filenames:
            curr_path = os.path.join(metadata_path, filename)
            
            with open(curr_path, 'r') as file:
                data = json.load(file)
                attributes = data['attributes']
                
                # Comparison hash generation
                digest = f'::{attributes}::'
                final_hash = xxhash.xxh128_hexdigest(digest).upper()
                
                if final_hash not in comparison_hashlib:
                    comparison_hashlib.append(final_hash)
                else:
                    verified = False
                    err = f'Duplicate of an "attributes" dict found [{filename}]'
                    Logger.pyprint('ERRO', '', err, True)
        
        return verified


    @staticmethod
    def __compare_listdir(listdir_1: list[str], listdir_2: list[str]) -> bool:
        '''Allows the comparison between two directory lists of files,
        it removes the files extension and verify them.
        
        Args:
            - listdir_1 (list[str]): The first 'os.listdir()' to check.
            - listdir_2 (list[str]): The second 'os.listdir()' to check.

        Returns:
            bool: The comparison result.
        '''
        
        driver = len(listdir_1)

        if driver == len(listdir_2):
            for i in range(driver):
                
                # Get the filenames without the extensions
                filename_1 = os.path.splitext(listdir_1[i])[0]
                filename_2 = os.path.splitext(listdir_2[i])[0]
                
                if filename_1 != filename_2:
                    err = f'Not corresponding files found [{listdir_1[i]} / {listdir_2[i]}]'
                    Logger.pyprint('ERRO', '', err, True)
                    
                    return False
                
            return True
        else:
            err = 'Quantity of metadata files does not corresponds with the quantity of NFTs'
            Logger.pyprint('ERRO', '', err, True)
            
        return False
    

    @staticmethod
    def mix_nfts(directory_name: str = 'dist', comparison_check: bool = True):
        '''Mix all the NFTs/metadata from the dist directory.
        
        WARNING: This function overwrites the original NFTs inside the 'dist/' directory.
        
        This function renames all the NFTs/metadata with a number from 0 to xxx
        in a random order, so all the NFTs/metadata are ready for OpenSea.
        
        The 'dist' directory contains two dirs:
            - The first directory contains the NFTs
            - The second one contains the JSON metadata files
            
        These two dirs contains the same amount of files, named 
        
        Args:
            directory_name (str, optional): The name of the directory where all the final NFTs are.
            comparison_check (bool, optional): Verifies the uniqueness of the metadata "attributes".
        '''
        
        # Main paths
        cwd = os.getcwd()
        dist_path = os.path.join(cwd, directory_name)
        nfts_path = os.path.join(dist_path, 'NFTs')
        metadata_path = os.path.join(dist_path, 'metadata')
        
        # Verify that the metadata corresponds to the NFTs (Names and number)
        nfts_names = os.listdir(nfts_path)
        metadata_names = os.listdir(metadata_path)
        
        if len(nfts_names) == 0:
            Logger.pyprint('ERRO', '', 'The "dist" directory is empty')
            return
        
        # If the arg is set to True,
        # verifies that every metadata file 'attributes' key is unique
        if comparison_check:
            comparison_verified = NFTsUtils.__verify_metadata_attributes(metadata_path, metadata_names)
        else:
            comparison_verified = True
        
        if comparison_verified:
            listdir_comparison = NFTsUtils.__compare_listdir(nfts_names, metadata_names)
            
            if listdir_comparison:
                # Apply a shuffle on the two lists to create a random mirrored order
                lists_zip = list(zip(nfts_names, metadata_names))
                random.shuffle(lists_zip)
                nfts_names, metadata_names = zip(*lists_zip)
                nfts_names, metadata_names = list(nfts_names), list(metadata_names)

            driver = len(nfts_names)

            # Renaming (path modification) loop
            for i, nft_name in enumerate(nfts_names):
                metadata_name = metadata_names[i]

                nft_orig_path = os.path.join(nfts_path, nft_name)
                metadata_orig_path = os.path.join(metadata_path, metadata_name)
                
                nft_new_path = os.path.join(nfts_path, f'{i+1}.png')
                metadata_new_path = os.path.join(metadata_path, f'{i+1}.json')
                
                os.rename(nft_orig_path, nft_new_path)
                os.rename(metadata_orig_path, metadata_new_path)

                Logger.pyprint('SUCCESS', '', f'{i+1}/{driver} NFTs renamed', same_line=True)
        else:
            Logger.pyprint('ERRO', '', 'NFTs could not be mixed, verify your metadata files', True)
