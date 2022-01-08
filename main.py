from libraries.utility import *
from parameters import *
from pathlib import Path


test_path = Path('E:/nfts-generator/input/elon')


# Main paths
cwd = Path(__file__).parent
input_path = (cwd / settings.main_input_dir_path).resolve()
output_path = (cwd / settings.main_output_dir_path).resolve()


# Character paths
elon_path = (input_path / 'elon').resolve()
jeff_path = (input_path / 'jeff').resolve()
richard_path = (input_path / 'richard').resolve()


test = NFT.get_character_layers(elon_path)
Randomize.character(test)
