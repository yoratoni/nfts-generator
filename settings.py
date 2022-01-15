class Param:
    # Default path to the main layers directory
    main_input_dir_path = 'input'
    
    # Default path to the output directory
    main_output_dir_path = 'output'

    # Exceptions handling:
    #   'ORDER_CHANGE' -> Change the order between two layers: [ORDER_CHANGE, name, put_before]
    #   'INCOMPATIBLE' -> NFT is regenerated if the listed images are used,
    #       or if one of the images are inside a layer (Supports only one image and one layer)
    exceptions = [
        ['ORDER_CHANGE', 'bottes combinaison.png', 'jean tesla bleu.png'],
        ['ORDER_CHANGE', 'bottes combinaison.png', 'pantalon costume.png'],
        ['ORDER_CHANGE', 'chaussures costume.png', 'pantalon costume.png'],
        ['ORDER_CHANGE', 'chaussures costume.png', 'jean tesla bleu.png'],
        
        # Glasses / Bandana
        ['ORDER_CHANGE', 'lunettes brun orange adaptées.png', 'bandana mask.png'],
        ['ORDER_CHANGE', 'lunettes brun orange grosse.png', 'bandana mask.png'],
        ['ORDER_CHANGE', 'lunettes soleil adaptées.png', 'bandana mask.png'],
        ['ORDER_CHANGE', 'lunettes soleil grosse.png', 'bandana mask.png'],
        ['ORDER_CHANGE', 'lunettes vu.png', 'bandana mask.png'],
        
        # Incompatibilities
        ['INCOMPATIBLE', 'visage et casquette rose.png', '07_hats'],
        ['INCOMPATIBLE', 'visage et casquette noir.png', '07_hats'],
        ['INCOMPATIBLE', 'clope.png', 'bandana mask.png']
    ]

    # Background folder
    background_folder = 'backgrounds'
    
    # Character folders list
    character_folders = [
        'elon',
        'jeff',
        'richard'
    ]
    
    # Optional layers (Accessories is not supported here)
    optional_layers = [
        '04_jackets',
        '07_hats'
    ]
    
    # Optional layers rarity (List of rarity per layer)
    optional_rarity = [2, 2]
    
    # Accessories folder name
    # Handled separately from the main character randomize function
    accessories_folder = '06_accessories'
    
    # Max amount of accessories
    max_accessories_amount = 2
