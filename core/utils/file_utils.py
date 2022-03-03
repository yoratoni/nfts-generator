from core import Logger

import textwrap
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
                try:
                    data = json.load(file)
                    attributes = data['attributes']
                    
                    # Comparison hash generation
                    digest = f'::{attributes}::'
                    final_hash = xxhash.xxh128_hexdigest(digest).upper()
                    
                    if final_hash not in comparison_hashlib:
                        comparison_hashlib.append(final_hash)
                        
                    # Two metadata files have the same attributes
                    else:
                        verified = False
                        err = f'Duplicate of an "attributes" dict found [{filename}]'
                        Logger.pyprint('ERRO', err)
                      
                # Error during the decoding of the file  
                except json.decoder.JSONDecodeError as err:
                    Logger.pyprint('ERRO', f'JSON decoding error [{err} - {file.name}]')
                                
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
                
                # Error during the filenames comparison
                if filename_1 != filename_2:
                    err = f'Not corresponding files found [{listdir_1[i]} / {listdir_2[i]}]'
                    Logger.pyprint('ERRO', err)
                    
                    return False
                
            return True
        
        # The number of files between NFTs and metadata does not corresponds
        else:
            err = 'Quantity of metadata files does not corresponds with the quantity of NFTs'
            Logger.pyprint('ERRO', err)
            
        return False
    
    
    @staticmethod
    def modify_format():
        '''This function is only used to modify some data inside the NFTs metadata,
        in case there's a wrong key etc..
        '''
        
        # Path of the directory
        cwd = os.getcwd()
        main_path = os.path.join(cwd, 'NFTs', 'metadata', 'elon')
        
        filenames = os.listdir(main_path)

        for filename in filenames:
            curr_path = os.path.join(main_path, filename)
            data = {}
            
            try:
                with open(curr_path, 'r') as file:
                    data = json.load(file)
                    
                    # Modify the 'data' dict here
                    # ---------------------------
            
            # Error during the decoding of the file 
            except json.decoder.JSONDecodeError as err:
                Logger.pyprint('ERRO', f'JSON decoding error [{err} - {file.name}]')
            
            # If the data are not empty/invalid, save the data
            if len(data) != 0  and data is not None: 
                with open(curr_path, 'w') as file:
                    json.dump(data, file, indent=4)


    @staticmethod
    def __mix_nfts(directory_path: os.path, comparison_check: bool = True):
        '''Mix all the NFTs/metadata from the dist directory.

        Args:
            directory_name (str, optional): The name of the directory where all the final NFTs are.
            comparison_check (bool, optional): Verifies the uniqueness of the metadata "attributes".
        '''
        
        # Main paths
        nfts_path = os.path.join(directory_path, 'NFTs')
        metadata_path = os.path.join(directory_path, 'metadata')
        
        # Verify that the metadata corresponds to the NFTs (Names and number)
        nfts_names = os.listdir(nfts_path)
        metadata_names = os.listdir(metadata_path)
        
        # Verify that the directories are not empty
        if len(nfts_names) == 0:
            Logger.pyprint('ERRO', 'The "dist" directory is empty')
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
                
                nft_new_path = os.path.join(nfts_path, f'{i}.png')
                metadata_new_path = os.path.join(metadata_path, f'{i}.json')
                
                os.rename(nft_orig_path, nft_new_path)
                os.rename(metadata_orig_path, metadata_new_path)
                
                # Success log
                Logger.pyprint('SUCCESS', f'{i+1}/{driver} NFTs renamed', True)
        
        # Wrong comparison between NFts and metadata
        else:
            Logger.pyprint('ERRO', 'NFTs could not be mixed, verify your metadata files')


    @staticmethod
    def mix_nfts(
        directory_name: str = 'dist',
        comparison_check: bool = True
    ):
        '''This is the main wrapper for the NFT mixing function,
        check the "__mix_nfts()" private function for more info.

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
        
        # Main path
        cwd = os.getcwd()
        directory_path = os.path.join(cwd, directory_name)
        
        # Existing directory checking
        if not os.path.exists(directory_path):
            err = textwrap.dedent('''\
            Wrong directory structure!
            Check the documentation: https://github.com/ostra-project/Advanced-NFTs-Generator
            
            ERROR: "dist" directory missing.
            ''')
            Logger.pyprint('ERRO', err)
            return
        
        # Structure checking
        struct_check = os.listdir(directory_path)
        if 'metadata' not in struct_check or 'NFTs' not in struct_check:
            err = textwrap.dedent('''\
            Wrong directory structure!
            Check the documentation: https://github.com/ostra-project/Advanced-NFTs-Generator

            Here's the correct structure:
            
            project_dir/
                |--dist/
                    |-- NFTs/
                    |-- metadata/
                
            - The NFTs directory contains all of the previously generated NFTs (project_dir/NFTs/output)
            - Same thing for the metadata directory (project_dir/NFTs/metadata)
            
            You can copy them from these directories after generating all the characters NFTs.
            ''')

            Logger.pyprint('ERRO', err)
            return
        
        NFTsUtils.__mix_nfts(directory_path, comparison_check)


    @staticmethod
    def prepare_nfts_for_opensea(
        ipfs: str,
        name: str,
        include_number_sign_in_number: bool,
        directory_path: os.path
        
    ):
        '''Prepare the NFTs for OpenSea by adding the name/ipfs inside the metadata.
        
        Note:
            If 'name' is an empty string or == None, the NFTs will be named '#01' or '01',
            if include_number_sign_in_number is set to False.
            
        Args:
            ipfs (str): The IPFS URI of the images.
            name (str): The name before the number of the NFT (Can be set to '' or None).
            include_number_sign_in_number (bool): Includes the '#' character before the number.
            directory_path (os.path): The path to the distribution directory.
        '''
        
        # Main paths
        nfts_path = os.path.join(directory_path, 'NFTs')
        metadata_path = os.path.join(directory_path, 'metadata')
        
        # Get a list of all the metadata files
        metadata_names = os.listdir(metadata_path)
    
        # Verify that the metadata directory is not empty     
        if len(metadata_names) == 0:
            Logger.pyprint('ERRO', 'The "dist" directory is empty')
            return

        # Opening every file and modify them
        # for i, metadata_name in enumerate(metadata_names):
        
        i = 0   
        metadata_name = metadata_names[i]
        
        # Get the whole path to the metadata file
        metadata_path = os.path.join(metadata_path, metadata_name)
        
        if os.path.exists(metadata_path):
            data = None
            
            with open(metadata_path, 'r') as metadata_file:
                metadata = json.load(metadata_file)
                
            if metadata is not None:
                with open(metadata_path, 'w') as metadata_file:
                    json.dump(metadata, metadata_file, indent=4)
                    
            # Error, empty metadata
            else:
                Logger.pyprint('ERRO', f'This metadata file cannot be loaded [{metadata_path}]')
            
        # Error, file not found
        else:
            Logger.pyprint('ERRO', f'This metadata file does not exists [{metadata_path}]')
