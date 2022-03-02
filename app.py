from core import Generator, NFTsUtils


# The main generator function:
#   This one will generate NFTs for one character (Check the function docstring for more info)
# Generator.generate_nfts(5, 'elon')


# The main mixing function
#   This function takes all the NFTs from ONE directory (called 'dist' by defaults),
#   And mix/renames all the NFTs from 1 to the number of files in the directory
#
# Mixing function directory structure:
#   Inside of this directory, there's two directories called 'NFTs' and 'metadata',
#   The first directory contains ALL the NFTs, just copy/paste them from the original output dir
#   The second one contains the JSON metadata files (with the same name as the NFTs),
#   Same thing for this one, just copy/paste all the metadata files from the metadata dir
# NFTsUtils.mix_nfts()


# Finally, this function adds the IPFS URI into the metadata files
# It also adds the name which is 'NAME #XXXX' (Check the var 'collection_name' inside the main settings)
NFTsUtils.prepare_nfts_for_opensea()