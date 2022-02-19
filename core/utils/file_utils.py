from core import Logger

import random
import os


class NFTsUtils:
    '''This class contains file-related methods
    for the final preparation of NFTs for OpenSea.
    '''

    @staticmethod
    def compare_listdir(listdir_1: list[str], listdir_2: list[str]) -> bool:
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
    def mix_nfts(directory_name: str = 'dist'):
        '''Mix all the NFTs/metadata from the dist directory.
        
        WARNING: This method overwrites the original NFTs inside the 'dist/' directory.
        
        This method renames all the NFTs/metadata with a number from 0 to xxx
        in a random order, so all the NFTs/metadata are ready for OpenSea.
        
        The 'dist' directory contains two dirs:
            - The first directory contains the NFTs
            - The second one contains the JSON metadata files
            
        These two dirs contains the same amount of files, named 
        
        Args:
            directory_name (str, optional) The name of the directory where all the final NFTs are.
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
        
        listdir_comparison = NFTsUtils.compare_listdir(nfts_names, metadata_names)
        
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
