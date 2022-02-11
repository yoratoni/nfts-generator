from pathlib import Path
from libs import Logger

import random
import os


class NFTsUtils:
    '''This class contains file-related methods
    for the final preparation of NFTs for OpenSea.
    '''

    @staticmethod
    def mix_nfts():
        '''Mix all the NFTs from the dist directory.
        
        WARNING: This method overwrites the original NFTs inside the 'dist/' directory.
                
        This method renames all the NFTs with a number from 0 to xxx
        in a random order, so all the NFTs are ready for OpenSea.
        '''
        
        # Main paths
        cwd = os.getcwd()
        dist_path = os.path.join(cwd, 'dist')

        # Original NFTs
        names = os.listdir(dist_path)
        random.shuffle(names)  # Shuffle the list for random iterations
        driver = len(names)

        # Renaming (path modification) loop
        for i, name in enumerate(names):
            orig_path = os.path.join(dist_path, name)
            new_path = os.path.join(dist_path, f'{i+1}.png')
            os.rename(orig_path, new_path)
            Logger.pyprint(f'{i+1}/{driver} NFTs renamed', 'SUCCESS', same_line=True)
        
        