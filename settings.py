class Param:
    # Default path to the main layers directory
    main_input_dir_path = 'input'
    
    # Default path to the output directory
    main_output_dir_path = 'output'

    # Background folder
    background_folder = 'backgrounds'
    
    # Character folders list
    character_folders = ['elon', 'jeff', 'richard']
    
    # Exceptions handling:
    #   'ORDER_CHANGE' -> Change the order between two layers: [ORDER_CHANGE, name, put_before_this_layer]
    #   'INCOMPATIBLE' -> NFT is regenerated if the listed images are used,
    #       or if one of the images are inside a layer (Supports only one image and one layer)
    exceptions = [
        # Watches
        ['INCOMPATIBLE', 'montre bleu.png', '05_jackets'],
        ['INCOMPATIBLE', 'montre bleu.png', 'chemise blanc anglais.png'],
        ['INCOMPATIBLE', 'montre bleu.png', 'chemise blanc.png'],
        ['INCOMPATIBLE', 'montre bleu.png', 'chemise cirque.png'],
        ['INCOMPATIBLE', 'montre bleu.png', 'chemise gris foncé.png'],
        ['INCOMPATIBLE', 'montre bleu.png', 'chemise gris.png'],
        ['INCOMPATIBLE', 'montre bleu.png', 'combi space entier.png'],
        ['INCOMPATIBLE', 'montre bleu.png', 'tenue sport haut.png'],
        ['INCOMPATIBLE', 'montre rouge.png', '05_jackets'],
        ['INCOMPATIBLE', 'montre rouge.png', 'chemise blanc anglais.png'],
        ['INCOMPATIBLE', 'montre rouge.png', 'chemise blanc.png'],
        ['INCOMPATIBLE', 'montre rouge.png', 'chemise cirque.png'],
        ['INCOMPATIBLE', 'montre rouge.png', 'chemise gris foncé.png'],
        ['INCOMPATIBLE', 'montre rouge.png', 'chemise gris.png'],
        ['INCOMPATIBLE', 'montre rouge.png', 'combi space entier.png'],
        ['INCOMPATIBLE', 'montre rouge.png', 'tenue sport haut.png'],

        # Combi space
        ['INCOMPATIBLE', 'combi space entier.png', '05_jackets'],
        ['INCOMPATIBLE', 'combi space entier.png' '03_trousers'],
        ['INCOMPATIBLE', 'combi space entier.png' 'chaussures hotesse.png'],

        # Other incompatibilities
        ['INCOMPATIBLE', 'tenue sport haut.png', '05_jackets'],
        ['INCOMPATIBLE', 'chemise cirque.png', '05_jackets'],
        ['INCOMPATIBLE', 'chaussures hotesse.png', 'combi space bas.png'],
        
        # Order Change
        ['ORDER CHANGE', 'chaussures hotesse.png', 'jean bleu.png'],
        ['ORDER CHANGE', 'chaussures hotesse.png', 'jean noir.png'],
        ['ORDER CHANGE', 'chaussures hotesse.png', 'pantalon costume gis.png'],
        ['ORDER CHANGE', 'chaussures hotesse.png', 'pantalon costume noir rayé.png'],
        ['ORDER CHANGE', 'chaussures hotesse.png', 'pantalon costume noir.png'],
        ['ORDER CHANGE', 'chaussures hotesse.png', 'pantalon costume txeed nude.png'],
        ['ORDER CHANGE', 'chaussures hotesse.png', 'pantalon costume tweed rayé.png'],
        ['ORDER CHANGE', 'chaussures hotesse.png', 'combi space entier.png'],
        ['ORDER CHANGE', 'tenue sport haut.png', 'tenue sport bas.png']
    ]

    # Optional layers (Accessories is not supported here)
    optional_layers = ['05_jackets', '08_glasses']
    
    # Optional layers rarity (List of rarity per layer)
    optional_rarity = [3, 5]
    
    # Accessories folder name
    # Handled separately from the main character randomize function
    accessories_folder = '07_accessories'
    
    # Max amount of accessories
    max_accessories_amount = 2

    # Accessories rarity
    accessories_rarity = 3

    # Increases the chances to use a specific image
    # As an example, if one image is specified: ['image.png', XX]
    # This image will appears XX times inside the list of images
    image_rarifier = [
        ['visage.png', 4]
    ]
