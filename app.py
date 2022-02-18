from core import Generator, NFTsUtils
from pathlib import Path

import os


# The main generator function:
#   This one will generate NFTs for one character (Check the function docstring for more info)
Generator.generate_nfts(2000, 'jeff', 1000)


# The main mixing function
#   This function takes all the NFTs from ONE directory (called 'dist' by defaults),
#   And mix/renames all the NFTs from 1 to the number of files in the directory
# Mixing function folder structure:
#   Inside of this folder, there's two directories called 'NFTs' and 'metadata',
#   The first directory contains ALL the NFTs, just copy/paste them from the original output dir
#   The second one contains the JSON metadata files (with the same name as the NFTs),
#   Same thing for this one, just copy/paste all the metadata files from the output dir
# Notes:
#   This function also adds the data inside the 'name' key of every NFT
# NFTsUtils.mix_nfts()


# Finally, this function adds the IPFS url into the metadata files
