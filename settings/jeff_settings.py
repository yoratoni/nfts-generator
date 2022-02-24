class JeffSettings:
    # String name of the character
    character_name = 'Jeff Bezos'
    
    # Exceptions handling
    exceptions = [
        ['DELETE', 'Spacesuit jacket.png', '03_belts', '05_shirts'],
        ['DELETE', 'Spacesuit.png', '02_pants', '03_belts', '04_hands', '06_jackets'],
        
        ['INCOMPATIBLE', '09_wrist', 'Astro white shirt.png'],
        ['INCOMPATIBLE', '09_wrist', 'Navy blue shirt 1.png'],
        ['INCOMPATIBLE', '09_wrist', 'Navy blue shirt 2.png'],
        ['INCOMPATIBLE', '09_wrist', 'Navy blue shirt 3.png'],
        ['INCOMPATIBLE', '09_wrist', 'Black shirt 1.png'],
        ['INCOMPATIBLE', '09_wrist', 'Black shirt 2.png'],
        ['INCOMPATIBLE', '09_wrist', 'Blue shirt 1.png'],
        ['INCOMPATIBLE', '09_wrist', 'Blue shirt 2.png'],
        ['INCOMPATIBLE', '09_wrist', 'Blue shirt 3.png'],
        ['INCOMPATIBLE', '09_wrist', 'White shirt.png'],
        ['INCOMPATIBLE', '09_wrist', 'Pink shirt.png'],
        ['INCOMPATIBLE', '09_wrist', 'Spacesuit.png'],
        ['INCOMPATIBLE', '09_wrist', '06_jackets'],
        
        ['INCOMPATIBLE', 'Spacesuit.png', 'Tie.png'],
        ['INCOMPATIBLE', 'Spacesuit.png', 'Santiags.png'],
        ['INCOMPATIBLE', 'Spacesuit pants.png', 'Santiags.png'],
        ['INCOMPATIBLE', 'Spacesuit jacket.png', 'Tie.png'],
        
        ['INCOMPATIBLE', 'Closed beige jacket 3.png', 'Blackboard.png'],

        ['ORDER_CHANGE', '07_shoes', 'Spacesuit.png'],
        ['ORDER_CHANGE', '07_shoes', 'Spacesuit pants.png'],

        ['ORDER_CHANGE', 'Tie.png', '06_jackets'],
        ['ORDER_CHANGE', 'Suit shoes.png', '02_pants'],
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
    optional_rarity = [3, 3, 4, 4]

    # Background directory
    backgrounds_dir = '00_backgrounds'
    
    # Accessories directory name
    # Handled separately from the main character randomizer function
    accessories_dir = '08_accessories'
    
    # Max amount of accessories
    max_accessories_amount = 2
    
    # Accessories rarity (MIN 1)
    accessories_rarity = 2
    
    # Increases the chances to use a specific image
    # As an example, if one image is specified: ['image.png', XX]
    # This image will appears XX times inside the list of images
    image_rarifier = [
        ['Tie.png', 2],
        ['Mask.png', 2]
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
        '11_hats': ['Head', '01_faces'],
        '02_pants': 'Pants',
        '03_belts': 'Belt',
        '05_shirts': 'Shirt',
        '06_jackets': 'Jacket',
        '07_shoes': 'Shoes',
        '09_wrist': 'Wrist',
        '08_accessories': 'Accessories',
        '10_glasses': 'Glasses'
    }
