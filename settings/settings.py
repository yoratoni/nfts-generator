from colorama import Fore


class DebugSettings:
    # If true, print all the available logs,
    # Else, just the types defined in 'forced_types'
    verbose_debugging = True
    
    # The section title, to separate the logs
    section_separators = '-' * 35
    section_color = Fore.LIGHTBLUE_EX
    section_title = 'NFTs GENERATOR'
    
    # List of debug log types and their colors in a dict
    all_types = {
        'INFO': Fore.LIGHTBLUE_EX,
        'DATA': Fore.CYAN,
        'WARN': Fore.YELLOW,
        'ERRO': Fore.LIGHTRED_EX,
        'SUCCESS': Fore.LIGHTGREEN_EX
    }
    
    # Debug log types that are always printed (even when verbose debugging is turned off)
    forced_types = ['WARN', 'ERRO', 'SUCCESS']
    
    # Debug log types that shows the name of the function that calls pyprint()
    show_function_name_types = ['WARN', 'ERRO']
    
    # Status codes used for general errors
    # I usually use modified HTTP Status Codes
    # Simply use 'log_or_status' with 'ST_' and the code after it (log_or_status = 'ST_42')
    status_codes = {}


class GlobalSettings:
    # Name of the collection (used for the NFTs name -> 'NAME' + ' #0123')
    collection_name = 'ASTRO'
    
    # Default path to the main layers directory
    main_input_dir = 'input'
    
    # Default path to the output directory
    main_output_dir = 'output'
    
    # Character directories list
    character_dirs = ['elon', 'jeff', 'richard']
    
    # List of all the available exceptions
    exceptions_list = ['ORDER_CHANGE', 'INCOMPATIBLE', 'DELETE', 'DELETE_ACCESSORY']
    
    # Exception handling
    order_change_modes = [
        'IMAGE BEFORE IMAGE',
        'LAYER BEFORE IMAGE',
        'IMAGE BEFORE LAYER',
        'LAYER BEFORE LAYER'
    ]
    
    
class CharacterSettings:
    '''Used for copy/pasting to create a new character settings class.
    Can also be used for type hints.
    
    Note:
        The characters class should be named like this by convention: NameSettings.
        Example: "JeffSettings" etc..
    '''
    
    # String name of the character
    character_name = ''
    
    # Exceptions Handling
    exceptions = []
    
    # Optional layers (Accessories is not supported here)
    optional_layers = []
    
    # Optional layers rarity (List of rarity per layer)
    optional_rarity = []
    
    # Background directory
    backgrounds_dir = ''
    
    # Accessories directory name
    # Handled separately from the main character randomizer function
    accessories_dir = ''

    # Max amount of accessories
    max_accessories_amount = 0

    # Accessories rarity
    accessories_rarity = 0
    
    # Increases the chances to use a specific image
    # As an example, if one image is specified: ['image.png', XX]
    # This image will appears XX times inside the list of images,
    # Reducing the chances for other images to be used
    image_rarifier = []
    
    # Metadata description
    metadata_description = ''
    
    # The attributes used for the character
    #   The key is the direct name of the directory
    #   The value is the name of the attribute
    #   Example: {'00_backgrounds': 'Background'}
    # Option (Fallback trait value):
    #   The attribute can be a list with another layer directory as the second argument:
    #   If te main layer is not used, the other layer value will be added instead
    #   Example: {'10_hats': ['Head', '01_faces']}
    #   Which means that if no hat is used, use the mandatory layer instead
    #   If no hat -> Use 'Short hair' or 'Normal hair' as a value
    metadata_attributes = {
        
    }
