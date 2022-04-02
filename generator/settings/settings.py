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
    '''Used for copy/pasting to create a new character settings class.
    
    Check the documentation on my GitHub:
    https://github.com/ostra-project/Advanced-NFTs-Generator
    
    Note:
        A character class file should be named 'name.py' by convention,
        This file should be inside "PROJECT_DIR/settings".
    '''
    
    name = ""               # Name of the character
    description = ""        # Description used for the metadata
    exceptions = []         # List of layer/trait exceptions
    optional_layers = []    # List of optional layers and their rarity
    trait_chances = []      # Allows to increase one specific trait chances
