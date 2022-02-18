class GlobalSettings:
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
        ['INCOMPATIBLE', 'Space helmet.png', 'Cigarette.png'],
        ['INCOMPATIBLE', 'Space helmet.png', 'Bandana.png'],
        ['INCOMPATIBLE', 'Space helmet.png', '04_jackets'],
        ['INCOMPATIBLE', 'Space helmet.png', '07_glasses'],
        ['INCOMPATIBLE', 'Spacesuit shirt.png', '04_jackets'],
        ['INCOMPATIBLE', 'Suit trousers.png', 'Motorbike boots.png'],
        
        ['ORDER_CHANGE', 'Spacesuit boots.png', 'Tesla jeans.png'],
        ['ORDER_CHANGE', 'Spacesuit boots.png', 'Suit trousers.png'],
        ['ORDER_CHANGE', 'Suit shoes.png', 'Tesla jeans.png'],
        ['ORDER_CHANGE', 'Suit shoes.png', 'Suit trousers.png'],
        ['ORDER_CHANGE', 'Barefoot.png', '02_trousers']
    ]
    
    # Optional layers (Accessories is not supported here)
    optional_layers = ['04_jackets', '07_glasses']
    
    # Optional layers rarity (List of rarity per layer)
    optional_rarity = [5, 6]
    
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
        ['Normal hair.png', 3],
        ['Short hair.png', 2],
        ['Normal hands.png', 5]
    ]
    
    # Metadata description
    metadata_description = ''
    
    # The attributes used for the character
    #   The key is the direct name of the directory
    #   The value is the name of the attribute
    #   Example: {'00_backgrounds': 'Background'}
    metadata_attributes = {
        '00_backgrounds': 'Background',
        '01_faces': 'Head',
        '02_trousers': 'Trousers',
        '03_shirts': 'Shirt',
        '04_jackets': 'Jacket',
        '05_shoes': 'Shoes',
        '06_accessories': 'Accessories',
        '07_glasses': 'Glasses',
        '08_hands': 'Hands',
    }


class JeffSettings:
    # String name of the character
    character_name = 'Jeff Bezos'
    
    # Exceptions handling
    exceptions = [
        ['DELETE', 'combi haut.png', '03_belts'],
        
        ['INCOMPATIBLE', 'combi haut.png', '06_jackets'],
        
        ['INCOMPATIBLE', 'montre.png', '06_jackets'],
        ['INCOMPATIBLE', 'montre.png', 'chemise blanc motifs astro.png'],
        ['INCOMPATIBLE', 'montre.png', 'chemise blanc.png'],
        ['INCOMPATIBLE', 'montre.png', 'chemise bleu ciel effet noir morpion.png'],
        ['INCOMPATIBLE', 'montre.png', 'chemise bleu ciel motif morpion.png'],
        ['INCOMPATIBLE', 'montre.png', 'chemise bleu ciel.png'],
        ['INCOMPATIBLE', 'montre.png', 'chemise bleu marine motif morpion.png'],
        ['INCOMPATIBLE', 'montre.png', 'chemise bleu marine motif pois.png'],
        ['INCOMPATIBLE', 'montre.png', 'chemise bleu marine.png'],
        ['INCOMPATIBLE', 'montre.png', 'chemise noir motif morpion.png'],
        ['INCOMPATIBLE', 'montre.png', 'chemise noir.png'],
        ['INCOMPATIBLE', 'montre.png', 'chemise rose.png'],
        
        ['INCOMPATIBLE', 'bracelet.png', '06_jackets'],
        ['INCOMPATIBLE', 'bracelet.png', 'chemise blanc motifs astro.png'],
        ['INCOMPATIBLE', 'bracelet.png', 'chemise blanc.png'],
        ['INCOMPATIBLE', 'bracelet.png', 'chemise bleu ciel effet noir morpion.png'],
        ['INCOMPATIBLE', 'bracelet.png', 'chemise bleu ciel motif morpion.png'],
        ['INCOMPATIBLE', 'bracelet.png', 'chemise bleu ciel.png'],
        ['INCOMPATIBLE', 'bracelet.png', 'chemise bleu marine motif morpion.png'],
        ['INCOMPATIBLE', 'bracelet.png', 'chemise bleu marine motif pois.png'],
        ['INCOMPATIBLE', 'bracelet.png', 'chemise bleu marine.png'],
        ['INCOMPATIBLE', 'bracelet.png', 'chemise noir motif morpion.png'],
        ['INCOMPATIBLE', 'bracelet.png', 'chemise noir.png'],
        ['INCOMPATIBLE', 'bracelet.png', 'chemise rose.png'],
        ['INCOMPATIBLE', 'bracelet.png', 'combi haut.png'],
        
        ['INCOMPATIBLE', 'bracelet 2.png', '06_jackets'],
        ['INCOMPATIBLE', 'bracelet 2.png', 'chemise blanc motifs astro.png'],
        ['INCOMPATIBLE', 'bracelet 2.png', 'chemise blanc.png'],
        ['INCOMPATIBLE', 'bracelet 2.png', 'chemise bleu ciel effet noir morpion.png'],
        ['INCOMPATIBLE', 'bracelet 2.png', 'chemise bleu ciel motif morpion.png'],
        ['INCOMPATIBLE', 'bracelet 2.png', 'chemise bleu ciel.png'],
        ['INCOMPATIBLE', 'bracelet 2.png', 'chemise bleu marine motif morpion.png'],
        ['INCOMPATIBLE', 'bracelet 2.png', 'chemise bleu marine motif pois.png'],
        ['INCOMPATIBLE', 'bracelet 2.png', 'chemise bleu marine.png'],
        ['INCOMPATIBLE', 'bracelet 2.png', 'chemise noir motif morpion.png'],
        ['INCOMPATIBLE', 'bracelet 2.png', 'chemise noir.png'],
        ['INCOMPATIBLE', 'bracelet 2.png', 'chemise rose.png'],
        ['INCOMPATIBLE', 'bracelet 2.png', 'combi haut.png'],

        ['INCOMPATIBLE', 'combi bas.png', 'santiags.png'],
        ['ORDER_CHANGE', 'chaussures costume.png', 'combi bas.png'],
        ['ORDER_CHANGE', 'chaussures costume.png', '02_trousers'],

        ['ORDER_CHANGE', '07_shoes', 'combi bas.png'],
        
        ['ORDER_CHANGE', 'bottes combi.png', 'pantalon beige effets.png'],
        ['ORDER_CHANGE', 'bottes combi.png', 'pantalon beige.png'],
        ['ORDER_CHANGE', 'bottes combi.png', 'pantalon bleu.png'],
        ['ORDER_CHANGE', 'bottes combi.png', 'pantalon noir.png'],
        ['ORDER_CHANGE', 'mocassins.png', 'pantalon beige effets.png'],
        ['ORDER_CHANGE', 'mocassins.png', 'pantalon beige.png'],
        ['ORDER_CHANGE', 'mocassins.png', 'pantalon bleu.png'],
        ['ORDER_CHANGE', 'mocassins.png', 'pantalon noir.png'],
    ]
    
    # Optional layers (Accessories is not supported here)
    optional_layers = ['06_jackets', '09_wrist', '10_glasses', '11_hats']
    
    # Optional layers rarity (List of rarity per layer)
    optional_rarity = [4, 4, 8, 4]

    # Background directory
    backgrounds_dir = '00_backgrounds'
    
    # Accessories directory name
    # Handled separately from the main character randomizer function
    accessories_dir = '06_accessories'
    
    # Max amount of accessories
    max_accessories_amount = 2 
    
    # Accessories rarity
    accessories_rarity = 5
    
    # Increases the chances to use a specific image
    # As an example, if one image is specified: ['image.png', XX]
    # This image will appears XX times inside the list of images
    image_rarifier = [
        ['cravate.png', 2],
        ['mask.png', 2]
    ]
    
    # Metadata description
    metadata_description = ''
    
    # The attributes used for the character
    #   The key is the direct name of the directory
    #   The value is the name of the attribute
    #   Example: {'00_backgrounds': 'Background'}
    metadata_attributes = {
        
    }
    

class RichardSettings:
    # String name of the character
    character_name = 'Richard Branson'
    
    # Exceptions handling
    exceptions = [
        ['DELETE', 'combi space entier.png', '03_trousers', '05_jackets'],
        
        ['INCOMPATIBLE', 'montre bleu.png', 'chemise blanc anglais.png'],
        ['INCOMPATIBLE', 'montre bleu.png', 'chemise blanc.png'],
        ['INCOMPATIBLE', 'montre bleu.png', 'chemise cirque.png'],
        ['INCOMPATIBLE', 'montre bleu.png', 'chemise gris foncé.png'],
        ['INCOMPATIBLE', 'montre bleu.png', 'chemise gris.png'],
        ['INCOMPATIBLE', 'montre bleu.png', 'combi space entier.png'],
        ['INCOMPATIBLE', 'montre bleu.png', 'tenue sport haut.png'],
        ['INCOMPATIBLE', 'montre rouge.png', 'chemise blanc anglais.png'],
        ['INCOMPATIBLE', 'montre rouge.png', 'chemise blanc.png'],
        ['INCOMPATIBLE', 'montre rouge.png', 'chemise cirque.png'],
        ['INCOMPATIBLE', 'montre rouge.png', 'chemise gris foncé.png'],
        ['INCOMPATIBLE', 'montre rouge.png', 'chemise gris.png'],
        ['INCOMPATIBLE', 'montre rouge.png', 'combi space entier.png'],
        ['INCOMPATIBLE', 'montre rouge.png', 'tenue sport haut.png'],

        # Jackets incompatibilities
        ['INCOMPATIBLE', 'montre bleu.png', '05_jackets'],
        ['INCOMPATIBLE', 'montre rouge.png', '05_jackets'],
        ['INCOMPATIBLE', 'tenue sport haut.png', '05_jackets'],
        ['INCOMPATIBLE', 'combi space bas.png', '05_jackets'],
        ['INCOMPATIBLE', 'chemise cirque.png', '05_jackets'],
        ['INCOMPATIBLE', 'chemise et veste hotess.png', '05_jackets'],
        
        ['INCOMPATIBLE', 'chaussures hotesse.png', 'combi space bas.png'],

        # Bottes combi space
        ['INCOMPATIBLE', 'bottes combi space.png', 'tenue sport bas.png'],
        ['INCOMPATIBLE', 'bottes combi space.png', 'pantalon costume tweed nude.png'],
        ['INCOMPATIBLE', 'bottes combi space.png', 'pantalon costume tweed rayé.png'],
        ['INCOMPATIBLE', 'bottes combi space.png', 'pantalon costume noir.png'],
        ['INCOMPATIBLE', 'bottes combi space.png', 'pantalon costume noir rayé.png'],
        ['INCOMPATIBLE', 'bottes combi space.png', 'pantalon costume gis.png'],
        ['INCOMPATIBLE', 'bottes combi space.png', 'jupe hotesse.png'],
        ['INCOMPATIBLE', 'bottes combi space.png', 'jean noir.png'],
        ['INCOMPATIBLE', 'bottes combi space.png', 'jean bleu.png'],
        
        ['INCOMPATIBLE', 'tenue sport haut.png', 'jupe hotesse.png'],
        
        # Pockets incompatibilities
        ['INCOMPATIBLE', 'tenue sport bas.png', 'chemise blanc anglais.png'],
        ['INCOMPATIBLE', 'tenue sport bas.png', 'chemise blanc court.png'],
        ['INCOMPATIBLE', 'tenue sport bas.png', 'chemise blanc.png'],
        ['INCOMPATIBLE', 'tenue sport bas.png', 'chemise gris court.png'],
        ['INCOMPATIBLE', 'tenue sport bas.png', 'chemise gris foncé court.png'],
        ['INCOMPATIBLE', 'tenue sport bas.png', 'chemise gris foncé.png'],
        ['INCOMPATIBLE', 'tenue sport bas.png', 'chemise gris.png'],
        ###
        ['INCOMPATIBLE', 'combi space bas.png', 'chemise blanc anglais.png'],
        ['INCOMPATIBLE', 'combi space bas.png', 'chemise blanc court.png'],
        ['INCOMPATIBLE', 'combi space bas.png', 'chemise blanc.png'],
        ['INCOMPATIBLE', 'combi space bas.png', 'chemise gris court.png'],
        ['INCOMPATIBLE', 'combi space bas.png', 'chemise gris foncé court.png'],
        ['INCOMPATIBLE', 'combi space bas.png', 'chemise gris foncé.png'],
        ['INCOMPATIBLE', 'combi space bas.png', 'chemise gris.png'],
        ###
        ['INCOMPATIBLE', 'jupe hotesse.png', 'chemise blanc anglais.png'],
        ['INCOMPATIBLE', 'jupe hotesse.png', 'chemise blanc court.png'],
        ['INCOMPATIBLE', 'jupe hotesse.png', 'chemise blanc.png'],
        ['INCOMPATIBLE', 'jupe hotesse.png', 'chemise gris court.png'],
        ['INCOMPATIBLE', 'jupe hotesse.png', 'chemise gris foncé court.png'],
        ['INCOMPATIBLE', 'jupe hotesse.png', 'chemise gris foncé.png'],
        ['INCOMPATIBLE', 'jupe hotesse.png', 'chemise gris.png'],
        ###
        ['INCOMPATIBLE', 'maquillage.png', 'chemise blanc anglais.png'],
        ['INCOMPATIBLE', 'maquillage.png', 'chemise blanc court.png'],
        ['INCOMPATIBLE', 'maquillage.png', 'chemise blanc.png'],
        ['INCOMPATIBLE', 'maquillage.png', 'chemise cirque.png'],
        ['INCOMPATIBLE', 'maquillage.png', 'chemise gris court.png'],
        ['INCOMPATIBLE', 'maquillage.png', 'chemise gris foncé court.png'],
        ['INCOMPATIBLE', 'maquillage.png', 'chemise gris foncé.png'],
        ['INCOMPATIBLE', 'maquillage.png', 'chemise gris.png'],
        ['INCOMPATIBLE', 'maquillage.png', 'tenue sport haut.png'],
        ['INCOMPATIBLE', 'maquillage.png', 'mask.png'],
        ['INCOMPATIBLE', 'maquillage.png', 'mask rouge.png'],
        ['INCOMPATIBLE', 'maquillage.png', '09_glasses'],

        # Order Change
        ['ORDER_CHANGE', 'chaussures hotesse.png', '03_trousers'],
        ['ORDER_CHANGE', 'chaussures hotesse.png', 'combi space entier.png'],
        ['ORDER_CHANGE', 'tenue sport haut.png', '03_trousers']
    ]

    # Optional layers (Accessories is not supported here)
    optional_layers = ['05_jackets', '09_glasses', '07_makeup']
    
    # Optional layers rarity (List of rarity per layer)
    optional_rarity = [3, 4, 5]
    
    # Background directory
    backgrounds_dir = '00_backgrounds'
    
    # Accessories directory name
    # Handled separately from the main character randomizer function
    accessories_dir = '06_accessories'
    
    # Max amount of accessories
    max_accessories_amount = 2

    # Accessories rarity
    accessories_rarity = 3

    # Increases the chances to use a specific image
    # As an example, if one image is specified: ['image.png', XX]
    # This image will appears XX times inside the list of images
    image_rarifier = [
        ['visage.png', 2],
        ['chemise blanc anglais.png', 2],
        ['chemise blanc court.png', 2],
        ['chemise blanc.png', 2],
        ['chemise gris court.png', 2],
        ['chemise gris foncé.png', 2],
        ['chemise gris foncé court.png', 2],
        ['chemise gris foncé.png', 2],
        ['chemise gris.png', 2]
    ]
    
    # Metadata description
    metadata_description = ''
    
    # The attributes used for the character
    #   The key is the direct name of the directory
    #   The value is the name of the attribute
    #   Example: {'00_backgrounds': 'Background'}
    metadata_attributes = {
        
    }
