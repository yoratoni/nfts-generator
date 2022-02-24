class ElonSettings:
    # String name of the character
    character_name = 'Elon Musk'
    
    # Exceptions handling
    exceptions = [
        ['INCOMPATIBLE', '07_glasses', 'Spacesuit helmet.png'],
        ['INCOMPATIBLE', '04_jackets', 'Spacesuit shirt.png'],
        ['INCOMPATIBLE', '04_jackets', 'Spacesuit helmet.png'],
        
        ['INCOMPATIBLE', '09_hats', 'Black cap.png'],
        ['INCOMPATIBLE', '09_hats', 'Blue cap.png'],
        ['INCOMPATIBLE', '09_hats', 'Green cap.png'],
        ['INCOMPATIBLE', '09_hats', 'Navy blue cap.png'],
        ['INCOMPATIBLE', '09_hats', 'Pink cap.png'],
        ['INCOMPATIBLE', '09_hats', 'Red cap.png'],
        ['INCOMPATIBLE', '09_hats', 'Normal hair.png'],
        
        ['INCOMPATIBLE', 'Spacesuit helmet.png', 'Cigarette.png'],
        ['INCOMPATIBLE', 'Spacesuit helmet.png', 'Bandana.png'],
        ['INCOMPATIBLE', 'Suit pants.png', 'Motorbike boots.png'],
        
        ['ORDER_CHANGE', 'Spacesuit boots.png', 'Tesla jeans.png'],
        ['ORDER_CHANGE', 'Spacesuit boots.png', 'Suit pants.png'],
        ['ORDER_CHANGE', 'Suit shoes.png', 'Tesla jeans.png'],
        ['ORDER_CHANGE', 'Suit shoes.png', 'Suit pants.png'],
        ['ORDER_CHANGE', 'Barefoot.png', '02_pants'],
    ]
    
    # Optional layers (Accessories is not supported here)
    optional_layers = ['04_jackets', '07_glasses', '09_hats']
    
    # Optional layers rarity (List of rarity per layer)
    optional_rarity = [4, 6, 3]
    
    # Background directory
    backgrounds_dir = '00_backgrounds'
    
    # Accessories directory name
    # Handled separately from the main character randomizer function
    accessories_dir = '06_accessories'

    # Max amount of accessories
    max_accessories_amount = 1

    # Accessories rarity
    accessories_rarity = 2
    
    # Increases the chances to use a specific image
    # As an example, if one image is specified: ['image.png', XX]
    # This image will appears XX times inside the list of images,
    # Reducing the chances for other images to be used
    image_rarifier = [
        ['Normal hair.png', 5],
        ['Short hair.png', 5],
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
        '09_hats': ['Head', '01_faces'],
        '02_pants': 'Pants',
        '03_shirts': 'Shirt',
        '04_jackets': 'Jacket',
        '08_hands': 'Hands',
        '05_shoes': 'Shoes',
        '06_accessories': 'Accessories',
        '07_glasses': 'Glasses'
    }
    