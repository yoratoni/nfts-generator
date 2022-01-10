class settings:
    # Default path to the main layers directory
    main_input_dir_path = 'input'
    
    # Default path to the output directory
    main_output_dir_path = 'output'

    # Exceptions handling:
    #   'ORDER_CHANGE' -> Change the order between two layers: [ORDER_CHANGE, name, put_before]
    #   'INCOMPATIBLE' -> NFT is regenerated if the listed images are used,
    #       or if one of the images are inside a layer (Supports only one image and one layer)
    exceptions = [
        # ['ORDER_CHANGE', 'bottes combinaison.png', 'jean tesla bleu.png'],
        # ['ORDER_CHANGE', 'bottes combinaison.png', 'pantalon costume.png'],
        # ['INCOMPATIBLE', 'bottes combinaison.png', '03_shirts']
        ['INCOMPATIBLE', 'visage casquette et ombre.png', '07_hats']
    ]
    
    # INCOMPATIBLE: Entre image et couche

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
