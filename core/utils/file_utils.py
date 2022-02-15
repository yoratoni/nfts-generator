from pathlib import Path
from core import Logger

import random
import os

# NOTES:
#   CHANGE THE 'name' VALUE FOR EVERY NFT METADATA JSON FILE

class NFTsUtils:
    '''This class contains file-related methods
    for the final preparation of NFTs for OpenSea.
    '''

    @staticmethod
    def mix_nfts(directory_name: str = 'dist'):
        '''Mix all the NFTs from the dist directory.
        
        WARNING: This method overwrites the original NFTs inside the 'dist/' directory.
                
        This method renames all the NFTs with a number from 0 to xxx
        in a random order, so all the NFTs are ready for OpenSea.
        
        Args:
            directory_name (str, optional) The name of the directory where all the final NFTs are.
        '''
        
        # Main paths
        cwd = os.getcwd()
        dist_path = os.path.join(cwd, directory_name)

        # Original NFTs
        names = os.listdir(dist_path)
        random.shuffle(names)  # Shuffle the list for random iterations
        driver = len(names)

        # Renaming (path modification) loop
        for i, name in enumerate(names):
            orig_path = os.path.join(dist_path, name)
            new_path = os.path.join(dist_path, f'{i+1}.png')
            os.rename(orig_path, new_path)
            Logger.pyprint('SUCCESS', '', f'{i+1}/{driver} NFTs renamed', same_line=True)
