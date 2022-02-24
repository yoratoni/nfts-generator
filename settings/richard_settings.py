class RichardSettings:
    # String name of the character
    character_name = 'Richard Branson'
    
    # Exceptions handling
    exceptions = [
        ['DELETE', 'Spacesuit.png', '03_pants', '05_jackets'],
        
        ['INCOMPATIBLE', 'Spacesuit pants.png', '05_jackets'],
        ['INCOMPATIBLE', 'Hostess shirt.png', '05_jackets'],
        ['INCOMPATIBLE', 'Circus shirt.png', '05_jackets'],
        ['INCOMPATIBLE', 'Sports top.png', '05_jackets'],
        
        ['DELETE_ACCESSORY', 'Blue watch.png', '05_jackets'],
        ['DELETE_ACCESSORY', 'Red watch.png', '05_jackets'],
        ['DELETE_ACCESSORY', 'Makeup.png', '09_glasses'],
        
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

        ['INCOMPATIBLE', 'Hostess shoes.png', 'Spacesuit pants.png'],
        ['INCOMPATIBLE', 'Sports top.png', 'Hostess skirt.png'],

        ['INCOMPATIBLE', 'Spacesuit boots.png', 'Sports shorts.png'],
        ['INCOMPATIBLE', 'Spacesuit boots.png', 'Tweed striped suit pants.png'],
        ['INCOMPATIBLE', 'Spacesuit boots.png', 'Tweed suit pants.png'],
        ['INCOMPATIBLE', 'Spacesuit boots.png', 'Black striped suit pants.png'],
        ['INCOMPATIBLE', 'Spacesuit boots.png', 'Black suit pants.png'],
        ['INCOMPATIBLE', 'Spacesuit boots.png', 'Gray suit pants.png'],
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
        
        ['INCOMPATIBLE', 'Spacesuit pants.png', 'White short-sleeved shirt.png'],
        ['INCOMPATIBLE', 'Spacesuit pants.png', 'White shirt 1.png'],
        ['INCOMPATIBLE', 'Spacesuit pants.png', 'White shirt 2.png'],
        ['INCOMPATIBLE', 'Spacesuit pants.png', 'Gray short-sleeved shirt.png'],
        ['INCOMPATIBLE', 'Spacesuit pants.png', 'Gray shirt.png'],
        ['INCOMPATIBLE', 'Spacesuit pants.png', 'Black short-sleeved shirt.png'],
        ['INCOMPATIBLE', 'Spacesuit pants.png', 'Black shirt.png'],
        
        ['INCOMPATIBLE', 'Hostess skirt.png', 'White short-sleeved shirt.png'],
        ['INCOMPATIBLE', 'Hostess skirt.png', 'White shirt 1.png'],
        ['INCOMPATIBLE', 'Hostess skirt.png', 'White shirt 2.png'],
        ['INCOMPATIBLE', 'Hostess skirt.png', 'Gray short-sleeved shirt.png'],
        ['INCOMPATIBLE', 'Hostess skirt.png', 'Gray shirt.png'],
        ['INCOMPATIBLE', 'Hostess skirt.png', 'Black short-sleeved shirt.png'],
        ['INCOMPATIBLE', 'Hostess skirt.png', 'Black shirt.png'],
        ['INCOMPATIBLE', 'Hostess skirt.png', 'Sports top.png'],

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

        ['ORDER_CHANGE', 'Hostess shoes.png', '03_pants'],
        ['ORDER_CHANGE', 'Hostess skirt.png', 'Hostess shoes.png'],
        ['ORDER_CHANGE', 'Hostess shoes.png', 'Spacesuit.png'],
        ['ORDER_CHANGE', 'Sports top.png', '03_pants']
    ]

    # Optional layers (Accessories is not supported here)
    optional_layers = ['05_jackets', '07_makeup', '09_glasses']
    
    # Optional layers rarity (List of rarity per layer)
    optional_rarity = [3, 3, 4]
    
    # Background directory
    backgrounds_dir = '00_backgrounds'
    
    # Accessories directory name
    # Handled separately from the main character randomizer function
    accessories_dir = '08_accessories'
    
    # Max amount of accessories
    max_accessories_amount = 2

    # Accessories rarity
    accessories_rarity = 2

    # Increases the chances to use a specific image
    # As an example, if one image is specified: ['image.png', XX]
    # This image will appears XX times inside the list of images
    image_rarifier = [
        ['Normal hair.png', 10],
        ['White short-sleeved shirt.png', 2],
        ['White shirt 1.png', 2],
        ['White shirt 2.png', 2],
        ['Black short-sleeved shirt.png', 2],
        ['Black shirt.png', 2],
        ['Gray short-sleeved shirt.png', 2],
        ['Gray shirt.png', 2],
        ['Hostess shirt.png', 2]
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
        '03_pants': 'Pants',
        '04_shirts': 'Shirt',
        '05_jackets': 'Jacket',
        '06_shoes': 'Shoes',
        '07_makeup': 'Makeup',
        '08_accessories': 'Accessories',
        '09_glasses': 'Glasses'
    }
