from libraries.utility import *
from parameters import *
from pathlib import Path


# Main paths
cwd = Path(__file__).parent
input_path = (cwd / settings.main_input_dir_path).resolve()
output_path = (cwd / settings.main_output_dir_path).resolve()


# Resources Path
elon_path = (input_path / 'elon').resolve()
jeff_path = (input_path / 'jeff').resolve()
richard_path = (input_path / 'richard').resolve()
backgrounds_path = (input_path / 'backgrounds').resolve()


for i in range(1000):
    nft_name = f'IMG_{str(i).zfill(3)}'
    nft_path = (output_path / nft_name).resolve()
    NFT.generate_unique_nft(settings, backgrounds_path, elon_path, nft_path)