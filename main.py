from libraries.utility import *
from settings import *
from pathlib import Path


# Main paths
cwd = Path(__file__).parent
input_folder_path = (cwd / Param.main_input_dir_path).resolve()
output_folder_path = (cwd / Param.main_output_dir_path).resolve()


# Resources Path
elon_path = (input_folder_path / 'elon').resolve()
jeff_path = (input_folder_path / 'jeff').resolve()
richard_path = (input_folder_path / 'richard').resolve()
backgrounds_path = (input_folder_path / 'backgrounds').resolve()


NFT.generate_nfts(10_000_000, 'IMG_', Param, richard_path, backgrounds_path, output_folder_path, False, False)
