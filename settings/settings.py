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
    exceptions_list = ['ORDER_CHANGE', 'INCOMPATIBLE', 'DELETE']
    
    # Debugging
    dist_mode = False  # If True, remove all the console messages, even forced ones
    verbose_debugging = True  # Print a lot more data about the NFTs
    debug_types = ['INFO', 'DATA', 'WARN', 'ERRO', 'SUCCESS']  # List of debug message types

    # Exception handling
    order_change_modes = [
        'IMAGE BEFORE IMAGE',
        'LAYER BEFORE IMAGE',
        'IMAGE BEFORE LAYER',
        'LAYER BEFORE LAYER'
    ]
    
    
class CharacterSettings:
    '''Used for copy/pasting to create a new character settings class.
    Can also be used for typing.
    
    The class name should be defined like this by convention: NameSettings.
    '''
    
    # String name of the character
    character_name = 'Elon Musk'
    
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
    metadata_attributes = {
        
    }


class ElonSettings:
    # String name of the character
    character_name = 'Elon Musk'
    
    # Exceptions handling
    exceptions = [
        ['INCOMPATIBLE', 'Spacesuit helmet.png', '04_jackets'],
        ['INCOMPATIBLE', 'Spacesuit helmet.png', '07_glasses'],
        ['INCOMPATIBLE', 'Spacesuit shirt.png', '04_jackets'],
        
        ['INCOMPATIBLE', 'Black cap.png', '09_hats'],
        ['INCOMPATIBLE', 'Pink cap.png', '09_hats'],
        ['INCOMPATIBLE', 'Normal hair.png', '09_hats'],
        ['INCOMPATIBLE', 'Big blue sunglasses.png', '09_hats'],
        ['INCOMPATIBLE', 'Big orange sunglasses.png', '09_hats'],
        
        ['INCOMPATIBLE', 'Spacesuit helmet.png', 'Cigarette.png'],
        ['INCOMPATIBLE', 'Spacesuit helmet.png', 'Bandana.png'],
        ['INCOMPATIBLE', 'Suit trousers.png', 'Motorbike boots.png'],
        
        ['ORDER_CHANGE', 'Spacesuit boots.png', 'Tesla jeans.png'],
        ['ORDER_CHANGE', 'Spacesuit boots.png', 'Suit trousers.png'],
        ['ORDER_CHANGE', 'Suit shoes.png', 'Tesla jeans.png'],
        ['ORDER_CHANGE', 'Suit shoes.png', 'Suit trousers.png'],
        ['ORDER_CHANGE', 'Barefoot.png', '02_trousers'],
    ]
    
    # Optional layers (Accessories is not supported here)
    optional_layers = ['04_jackets', '07_glasses', '09_hats']
    
    # Optional layers rarity (List of rarity per layer)
    optional_rarity = [5, 6, 5]
    
    # Background directory
    backgrounds_dir = '00_backgrounds'
    
    # Accessories directory name
    # Handled separately from the main character randomizer function
    accessories_dir = '06_accessories'

    # Max amount of accessories
    max_accessories_amount = 1

    # Accessories rarity
    accessories_rarity = 4
    
    # Increases the chances to use a specific image
    # As an example, if one image is specified: ['image.png', XX]
    # This image will appears XX times inside the list of images,
    # Reducing the chances for other images to be used
    image_rarifier = [
        ['Normal hair.png', 2],
        ['Short hair.png', 2],
        ['Normal hands.png', 5]
    ]
    
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
        '00_backgrounds': 'Background',
        '02_trousers': 'Trousers',
        '03_shirts': 'Shirt',
        '04_jackets': 'Jacket',
        '05_shoes': 'Shoes',
        '06_accessories': 'Accessories',
        '07_glasses': 'Glasses',
        '08_hands': 'Hands',
        '09_hats': ['Head', '01_faces']
    }


class JeffSettings:
    # String name of the character
    character_name = 'Jeff Bezos'
    
    # Exceptions handling
    exceptions = [
        ['DELETE', 'Spacesuit jacket.png', '03_belts'],
        ['DELETE', 'Spacesuit.png', '02_trousers', '03_belts', '04_hands', '06_jackets', '03_belts'],
        
        ['INCOMPATIBLE', 'Astro white shirt.png', '09_wrist'],
        ['INCOMPATIBLE', 'Navy blue shirt 1.png', '09_wrist'],
        ['INCOMPATIBLE', 'Navy blue shirt 2.png', '09_wrist'],
        ['INCOMPATIBLE', 'Navy blue shirt 3.png', '09_wrist'],
        ['INCOMPATIBLE', 'Black shirt 1.png', '09_wrist'],
        ['INCOMPATIBLE', 'Black shirt 2.png', '09_wrist'],
        ['INCOMPATIBLE', 'Blue shirt 1.png', '09_wrist'],
        ['INCOMPATIBLE', 'Blue shirt 2.png', '09_wrist'],
        ['INCOMPATIBLE', 'Blue shirt 3.png', '09_wrist'],
        ['INCOMPATIBLE', 'White shirt.png', '09_wrist'],
        ['INCOMPATIBLE', 'Pink shirt.png', '09_wrist'],
        ['INCOMPATIBLE', 'Spacesuit.png', '09_wrist'],
        ['INCOMPATIBLE', '06_jackets', '09_wrist'],
        
        ['INCOMPATIBLE', 'Spacesuit.png', 'Tie.png'],
        ['INCOMPATIBLE', 'Spacesuit.png', 'Santiags.png'],
        ['INCOMPATIBLE', 'Spacesuit trousers.png', 'Santiags.png'],
        ['INCOMPATIBLE', 'Spacesuit jacket.png', 'Tie.png'],
        
        ['INCOMPATIBLE', 'Closed beige jacket 3.png', 'Blackboard.png'],

        ['ORDER_CHANGE', '07_shoes', 'Spacesuit.png'],
        ['ORDER_CHANGE', '07_shoes', 'Spacesuit trousers.png'],

        ['ORDER_CHANGE', 'Tie.png', '06_jackets'],
        ['ORDER_CHANGE', 'Suit shoes.png', '02_trousers'],
        ['ORDER_CHANGE', 'Spacesuit boots.png', 'Beige jeans 1.png'],
        ['ORDER_CHANGE', 'Spacesuit boots.png', 'Beige jeans 2.png'],
        ['ORDER_CHANGE', 'Spacesuit boots.png', 'Black jeans.png'],
        ['ORDER_CHANGE', 'Spacesuit boots.png', 'Blue jeans.png'],
        ['ORDER_CHANGE', 'Dress shoes.png', 'Beige jeans 1.png'],
        ['ORDER_CHANGE', 'Dress shoes.png', 'Beige jeans 2.png'],
        ['ORDER_CHANGE', 'Dress shoes.png', 'Black jeans.png'],
        ['ORDER_CHANGE', 'Dress shoes.png', 'Blue jeans.png'],
    ]
    
    # Optional layers (Accessories is not supported here)
    optional_layers = ['06_jackets', '09_wrist', '10_glasses', '11_hats']
    
    # Optional layers rarity (List of rarity per layer)
    optional_rarity = [4, 4, 5, 5]

    # Background directory
    backgrounds_dir = '00_backgrounds'
    
    # Accessories directory name
    # Handled separately from the main character randomizer function
    accessories_dir = '08_accessories'
    
    # Max amount of accessories
    max_accessories_amount = 2
    
    # Accessories rarity (MIN 1)
    accessories_rarity = 1
    
    # Increases the chances to use a specific image
    # As an example, if one image is specified: ['image.png', XX]
    # This image will appears XX times inside the list of images
    image_rarifier = [
        ['Tie.png', 2],
        ['Mask.png', 2],
        ['Bald.png', 16]
    ]
    
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
        '00_backgrounds': 'Background',
        '02_trousers': 'Trousers',
        '03_belts': 'Belt',
        '05_shirts': 'Shirt',
        '06_jackets': 'Jacket',
        '07_shoes': 'Shoes',
        '08_accessories': 'Accessories',
        '09_wrist': 'Wrist',
        '10_glasses': 'Glasses',
        '11_hats': ['Head', '01_faces']
    }
    

class RichardSettings:
    # String name of the character
    character_name = 'Richard Branson'
    
    # Exceptions handling
    exceptions = [
        ['DELETE', 'Spacesuit.png', '03_trousers', '05_jackets'],
        
        ['INCOMPATIBLE', 'Spacesuit trousers.png', '05_jackets'],
        ['INCOMPATIBLE', 'Hostess shirt.png', '05_jackets'],
        ['INCOMPATIBLE', 'Circus shirt.png', '05_jackets'],
        ['INCOMPATIBLE', 'Sports top.png', '05_jackets'],
        ['INCOMPATIBLE', 'Blue watch.png', '05_jackets'],
        ['INCOMPATIBLE', 'Red watch.png', '05_jackets'],
        ['INCOMPATIBLE', 'Makeup.png', '09_glasses'],
        
        # Incompatibilities with watches
        ['INCOMPATIBLE', 'Blue watch.png', 'White shirt 1.png'],
        ['INCOMPATIBLE', 'Blue watch.png', 'White shirt 2.png'],
        ['INCOMPATIBLE', 'Blue watch.png', 'Circus shirt.png'],
        ['INCOMPATIBLE', 'Blue watch.png', 'Black shirt.png'],
        ['INCOMPATIBLE', 'Blue watch.png', 'Gray shirt.png'],
        ['INCOMPATIBLE', 'Blue watch.png', 'Sports top.png'],
        ['INCOMPATIBLE', 'Blue watch.png', 'Spacesuit.png'],
        ['INCOMPATIBLE', 'Red watch.png', 'White shirt 1.png'],
        ['INCOMPATIBLE', 'Red watch.png', 'White shirt 2.png'],
        ['INCOMPATIBLE', 'Red watch.png', 'Circus shirt.png'],
        ['INCOMPATIBLE', 'Red watch.png', 'Black shirt.png'],
        ['INCOMPATIBLE', 'Red watch.png', 'Gray shirt.png'],
        ['INCOMPATIBLE', 'Red watch.png', 'Sports top.png'],
        ['INCOMPATIBLE', 'Red watch.png', 'Spacesuit.png'],

        ['INCOMPATIBLE', 'Hostess shoes.png', 'Spacesuit trousers.png'],
        ['INCOMPATIBLE', 'Sports top.png', 'Hostess skirt.png'],

        ['INCOMPATIBLE', 'Spacesuit boots.png', 'Sports shorts.png'],
        ['INCOMPATIBLE', 'Spacesuit boots.png', 'Tweed striped suit trousers.png'],
        ['INCOMPATIBLE', 'Spacesuit boots.png', 'Tweed suit trousers.png'],
        ['INCOMPATIBLE', 'Spacesuit boots.png', 'Black striped suit trousers.png'],
        ['INCOMPATIBLE', 'Spacesuit boots.png', 'Black suit trousers.png'],
        ['INCOMPATIBLE', 'Spacesuit boots.png', 'Gray suit trousers.png'],
        ['INCOMPATIBLE', 'Spacesuit boots.png', 'Hostess skirt.png'],
        ['INCOMPATIBLE', 'Spacesuit boots.png', 'Black jeans.png'],
        ['INCOMPATIBLE', 'Spacesuit boots.png', 'Blue jeans.png'],

        # Pockets incompatibilities
        ['INCOMPATIBLE', 'Sports shorts.png', 'White short-sleeved shirt.png'],
        ['INCOMPATIBLE', 'Sports shorts.png', 'White shirt 1.png'],
        ['INCOMPATIBLE', 'Sports shorts.png', 'White shirt 2.png'],
        ['INCOMPATIBLE', 'Sports shorts.png', 'Gray short-sleeved shirt.png'],
        ['INCOMPATIBLE', 'Sports shorts.png', 'Gray shirt.png'],
        ['INCOMPATIBLE', 'Sports shorts.png', 'Black short-sleeved shirt.png'],
        ['INCOMPATIBLE', 'Sports shorts.png', 'Black shirt.png'],
        
        ['INCOMPATIBLE', 'Spacesuit trousers.png', 'White short-sleeved shirt.png'],
        ['INCOMPATIBLE', 'Spacesuit trousers.png', 'White shirt 1.png'],
        ['INCOMPATIBLE', 'Spacesuit trousers.png', 'White shirt 2.png'],
        ['INCOMPATIBLE', 'Spacesuit trousers.png', 'Gray short-sleeved shirt.png'],
        ['INCOMPATIBLE', 'Spacesuit trousers.png', 'Gray shirt.png'],
        ['INCOMPATIBLE', 'Spacesuit trousers.png', 'Black short-sleeved shirt.png'],
        ['INCOMPATIBLE', 'Spacesuit trousers.png', 'Black shirt.png'],
        
        ['INCOMPATIBLE', 'Hostess skirt.png', 'White short-sleeved shirt.png'],
        ['INCOMPATIBLE', 'Hostess skirt.png', 'White shirt 1.png'],
        ['INCOMPATIBLE', 'Hostess skirt.png', 'White shirt 2.png'],
        ['INCOMPATIBLE', 'Hostess skirt.png', 'Gray short-sleeved shirt.png'],
        ['INCOMPATIBLE', 'Hostess skirt.png', 'Gray shirt.png'],
        ['INCOMPATIBLE', 'Hostess skirt.png', 'Black short-sleeved shirt.png'],
        ['INCOMPATIBLE', 'Hostess skirt.png', 'Black shirt.png'],

        ['INCOMPATIBLE', 'Makeup.png', 'White short-sleeved shirt.png'],
        ['INCOMPATIBLE', 'Makeup.png', 'White shirt 1.png'],
        ['INCOMPATIBLE', 'Makeup.png', 'White shirt 2.png'],
        ['INCOMPATIBLE', 'Makeup.png', 'Circus shirt.png'],
        ['INCOMPATIBLE', 'Makeup.png', 'Gray short-sleeved shirt.png'],
        ['INCOMPATIBLE', 'Makeup.png', 'Gray shirt.png'],
        ['INCOMPATIBLE', 'Makeup.png', 'Black short-sleeved shirt.png'],
        ['INCOMPATIBLE', 'Makeup.png', 'Black shirt.png'],
        ['INCOMPATIBLE', 'Makeup.png', 'Sports top.png'],
        ['INCOMPATIBLE', 'Makeup.png', 'Black mask.png'],
        ['INCOMPATIBLE', 'Makeup.png', 'Red mask.png'],

        ['ORDER_CHANGE', 'Hostess shoes.png', '03_trousers'],
        ['ORDER_CHANGE', 'Hostess shoes.png', 'Spacesuit.png'],
        ['ORDER_CHANGE', 'Sports top.png', '03_trousers']
    ]

    # Optional layers (Accessories is not supported here)
    optional_layers = ['05_jackets', '07_makeup', '09_glasses']
    
    # Optional layers rarity (List of rarity per layer)
    optional_rarity = [3, 5, 4]
    
    # Background directory
    backgrounds_dir = '00_backgrounds'
    
    # Accessories directory name
    # Handled separately from the main character randomizer function
    accessories_dir = '08_accessories'
    
    # Max amount of accessories
    max_accessories_amount = 2

    # Accessories rarity
    accessories_rarity = 4

    # Increases the chances to use a specific image
    # As an example, if one image is specified: ['image.png', XX]
    # This image will appears XX times inside the list of images
    image_rarifier = [
        ['Normal hair.png', 12],
        ['White short-sleeved shirt.png', 2],
        ['White shirt 1.png', 2],
        ['White shirt 2.png', 2],
        ['Black short-sleeved shirt.png', 2],
        ['Black shirt.png', 2],
        ['Gray short-sleeved shirt.png', 2],
        ['Gray shirt.png', 2]
    ]
    
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
        '00_backgrounds': 'Background',
        '01_faces': 'Head',
        '03_trousers': 'Trousers',
        '04_shirts': 'Shirt',
        '05_jackets': 'Jacket',
        '06_shoes': 'Shoes',
        '07_makeup': 'Makeup',
        '08_accessories': 'Accessories',
        '09_glasses': 'Glasses'
    }
