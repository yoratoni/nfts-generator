class GlobalSettings:
    # Name of the collection
    collection_name = ""
    
    # List of all the character
    characters = []
    
    # NFT name format
    # "_X_": Collection name (Uppercased), "_N_": NFT ID
    name_format = "_X_ #_N_"
    
    # If filled, applied as description for every NFT (Overwritten by character class descriptions)
    unique_description = ""


class CharacterSettings:
    """Used for copy/pasting to create a new character settings class.
    
    Check the documentation on my GitHub:
    https://github.com/ostra-project/Advanced-NFTs-Generator
    
    Note:
        A character class file should be named "name.py" by convention,
        This file should be inside "PROJECT_DIR/settings".
    """
    
    ### MAIN INFO ###
    name = ""                           # Name of the character
    description = ""                    # Description used for the metadata
    
    ### CHANCES ###
    accessories_rarity = 0              # Rarity of the accessories
    optional_layers = {}                # List of optional layers and their rarity ({"00_backgrounds": 3})
    trait_chances = {}                  # Allows to increase one trait chances ({"trait_1.png": 3})
    
    ### DIRECTORIES ###
    accessories_dir = ""                # Name of the accessories directory (= layer name)
    background_dir = ""                 # Name of the background directory (= layer name)
    
    ### OTHERS ###
    max_accessories_amount = 0          # Max amount of accessories at the same time (for one NFT)
    exceptions = []                     # List of layer/trait exceptions
    