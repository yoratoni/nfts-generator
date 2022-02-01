from libs import Logger, CharacterRandomization
from settings import GlobalSettings, ElonSettings, JeffSettings, RichardSettings



class Generator:
    # Hashlib containing SHA1 hashes
    # Every hash is made with all the paths used in one image
    # Allows comparison between images without generating them
    nft_comparator_hashlib = []