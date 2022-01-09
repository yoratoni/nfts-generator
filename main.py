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

# TESTING
for i in range(10):
    output_full_path = (output_path / f'IMG_{i}.png').resolve()
    NFT.generate_unique_nft(settings, backgrounds_path, elon_path, output_full_path)
