from ast import Global
from libraries.utility import *
from settings import *
from pathlib import Path


# NFTs parameters
number_of_nfts = 3  # The number of generated NFTs
character_generated = 'jeff'  # Name of the character folder
nft_names = 'IMG_'  # Name of the NFTs (plus a number after it) (Generates a unique NFT if empty)
is_saving_system_enabled = True  # If the NFTs are saved to the output folder


# Main paths
cwd = Path(__file__).parent
input_folder_path = (cwd / Global_Param.main_input_dir_path).resolve()
output_folder_path = (cwd / Global_Param.main_output_dir_path).resolve()
character_path = (input_folder_path / character_generated).resolve()
backgrounds_path = (input_folder_path / Global_Param.background_folder).resolve()


# Get Parameters based on the character
if character_generated == Global_Param.character_folders[0]:
    character_param = Elon_Param
elif character_generated == Global_Param.character_folders[1]:
    character_param = Jeff_Param
elif character_generated == Global_Param.character_folders[2]:
    character_param = Richard_Param


# Generates the NFTs
NFT.generate_nfts(number_of_nfts,
                  nft_names,
                  character_param,
                  character_path,
                  backgrounds_path,
                  output_folder_path,
                  is_saving_system_enabled
                 )
