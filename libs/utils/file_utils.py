from pathlib import Path

import os


class NFTsUtils:
    '''This class contains file-related methods
    for the preparation of NFTs.
    '''

    @staticmethod
    def nfts_mix():
        '''Mix all the NFTs.
        '''
        
        cwd = os.getcwd()
        output_path = Path(os.path.join(cwd, 'output'))
        output_dirs = os.listdir(output_path)
    