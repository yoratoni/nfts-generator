from libraries.utility import *
from settings import *
from pathlib import Path


# Main paths
cwd = Path(__file__).parent
input_folder_path = (cwd / Param.main_input_dir_path).resolve()
output_folder_ath = (cwd / Param.main_output_dir_path).resolve()


# Resources Path
elon_path = (input_folder_path / 'elon').resolve()
jeff_path = (input_folder_path / 'jeff').resolve()
richard_path = (input_folder_path / 'richard').resolve()
backgrounds_path = (input_folder_path / 'backgrounds').resolve()



multiproc_args = [
    []
]



test = NFT.multiproc(NFT.generate_nfts, )


NFT.generate_nfts(50, 'IMG_', Param, elon_path, backgrounds_path, output_folder_ath, False, False)
