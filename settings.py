class Global_Param:
    # Default path to the main layers directory
    main_input_dir = 'input'
    
    # Default path to the output directory
    main_output_dir = 'output'
    
    # Character folders list
    character_folders = ['elon', 'jeff', 'richard']
    

class Elon_Param:
    # Exceptions handling:
    #   'ORDER_CHANGE' -> Change the order between two layers: [ORDER_CHANGE, name, put_before_this_layer]
    #   'INCOMPATIBLE' -> NFT is regenerated if the listed images are used,
    #       or if one of the images are inside a layer (Supports only one image and one layer)
    exceptions = [
        # Incompatibilities
        ['INCOMPATIBLE', 'visage et casquette rose.png', '08_hats'],
        ['INCOMPATIBLE', 'visage et casquette noir.png', '08_hats'],
        ['INCOMPATIBLE', 'clope.png', '08_hats'],
        
        ['INCOMPATIBLE', 'casque space transparence.png', 'bandana mask.png'],
        ['INCOMPATIBLE', 'casque space transparence.png', '07_glasses'],
        ['INCOMPATIBLE', 'casque space transparence.png', '04_jackets'],
        ['INCOMPATIBLE', 'combinaison haut.png', '04_jackets'],
        
        ['ORDER_CHANGE', 'bottes combinaison.png', 'jean tesla bleu.png'],
        ['ORDER_CHANGE', 'bottes combinaison.png', 'pantalon costume.png'],
        ['ORDER_CHANGE', 'chaussures costume.png', 'pantalon costume.png'],
        ['ORDER_CHANGE', 'chaussures costume.png', 'jean tesla bleu.png'],
    ]
    
    # Optional layers (Accessories is not supported here)
    optional_layers = ['04_jackets', '07_glasses', '08_hats']
    
    # Optional layers rarity (List of rarity per layer)
    optional_rarity = [5, 6, 5]
    
    # Background folder
    backgrounds_folder = '00_backgrounds'
    
    # Accessories folder name
    # Handled separately from the main character randomize function
    accessories_folder = '06_accessories'

    # Max amount of accessories
    max_accessories_amount = 2

    # Accessories rarity
    accessories_rarity = 3
    
    # Increases the chances to use a specific image
    # As an example, if one image is specified: ['image.png', XX]
    # This image will appears XX times inside the list of images
    image_rarifier = [
        ['visage.png', 2],
        ['visage coupe court.png', 2],
        ['mains.png', 3],
    ]


class Jeff_Param:
    # Exceptions handling:
    #   'ORDER_CHANGE' -> Change the order between two layers: [ORDER_CHANGE, name, put_before_this_layer]
    #   'INCOMPATIBLE' -> NFT is regenerated if the listed images are used,
    #       or if one of the images are inside a layer (Supports only one image and one layer)
    exceptions = [
        # Incompatibilities
        ['INCOMPATIBLE', 'combi haut.png', '06_jackets'],
        
        ['INCOMPATIBLE', 'montre.png', 'veste fermée beige effets.png'],
        ['INCOMPATIBLE', 'montre.png', 'veste fermée beige et noir.png'],
        ['INCOMPATIBLE', 'montre.png', 'veste fermée beige.png'],
        ['INCOMPATIBLE', 'montre.png', 'veste fermée noir effet.png'],
        ['INCOMPATIBLE', 'montre.png', 'veste fermée noir net.png'],
        ['INCOMPATIBLE', 'montre.png', 'veste fermée rayures rouges.png'],
        ['INCOMPATIBLE', 'montre.png', 'veste ouverte beige.png'],
        ['INCOMPATIBLE', 'montre.png', 'veste ouverte noir.png'],
        ['INCOMPATIBLE', 'montre.png', 'veste splash.png'],
        
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

        ['INCOMPATIBLE', 'bracelet.png', 'veste fermée beige effets.png'],
        ['INCOMPATIBLE', 'bracelet.png', 'veste fermée beige et noir.png'],
        ['INCOMPATIBLE', 'bracelet.png', 'veste fermée beige.png'],
        ['INCOMPATIBLE', 'bracelet.png', 'veste fermée noir effet.png'],
        ['INCOMPATIBLE', 'bracelet.png', 'veste fermée noir net.png'],
        ['INCOMPATIBLE', 'bracelet.png', 'veste fermée rayures rouges.png'],
        ['INCOMPATIBLE', 'bracelet.png', 'veste ouverte beige.png'],
        ['INCOMPATIBLE', 'bracelet.png', 'veste ouverte noir.png'],
        ['INCOMPATIBLE', 'bracelet.png', 'veste splash.png'],
        
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

        ['INCOMPATIBLE', 'bracelet 2.png', 'veste fermée beige effets.png'],
        ['INCOMPATIBLE', 'bracelet 2.png', 'veste fermée beige et noir.png'],
        ['INCOMPATIBLE', 'bracelet 2.png', 'veste fermée beige.png'],
        ['INCOMPATIBLE', 'bracelet 2.png', 'veste fermée noir effet.png'],
        ['INCOMPATIBLE', 'bracelet 2.png', 'veste fermée noir net.png'],
        ['INCOMPATIBLE', 'bracelet 2.png', 'veste fermée rayures rouges.png'],
        ['INCOMPATIBLE', 'bracelet 2.png', 'veste ouverte beige.png'],
        ['INCOMPATIBLE', 'bracelet 2.png', 'veste ouverte noir.png'],
        ['INCOMPATIBLE', 'bracelet 2.png', 'veste splash.png'],

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
        
        ['INCOMPATIBLE', 'combi haut.png', '03_belts'],
        ['INCOMPATIBLE', 'combi bas.png', '03_belts'],
        
        ['ORDER_CHANGE', 'chaussures costume.png', '02_trousers'],
        ['ORDER_CHANGE', 'bottes combi.png', '02_trousers'],
        ['ORDER_CHANGE', 'mocassins.png', '02_trousers']
    ]
    
    # Optional layers (Accessories is not supported here)
    optional_layers = ['06_jackets', '09_wrist', '10_glasses', '11_hats']
    
    # Optional layers rarity (List of rarity per layer)
    optional_rarity = [5, 4, 7, 5]

    # Background folder
    backgrounds_folder = '00_backgrounds'

    # Accessories folder name
    # Handled separately from the main character randomize function
    accessories_folder = '08_accessories'
    
    # Max amount of accessories
    max_accessories_amount = 2 
    
    # Accessories rarity
    accessories_rarity = 3
    
    # Increases the chances to use a specific image
    # As an example, if one image is specified: ['image.png', XX]
    # This image will appears XX times inside the list of images
    image_rarifier = [
        ['cravate.png', 5]
    ]


class Richard_Param:
    # Exceptions handling:
    #   'ORDER_CHANGE' -> Change the order between two images: [ORDER_CHANGE, name, put_before_this_image]
    #       or the order between an image and a whole layer [ORDER_CHANGE, name, put_before_this_layer]
    #   'INCOMPATIBLE' -> NFT is regenerated if the listed images are used,
    #       or if one of the images are inside a layer (Supports only one image and one layer as arg_1 and arg_2)
    exceptions = [
        # Watches incompatibilities
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

        # Other incompatibilities
        ['INCOMPATIBLE', 'tenue sport haut.png', '05_jackets'],
        ['INCOMPATIBLE', 'chemise cirque.png', '05_jackets'],
        ['INCOMPATIBLE', 'chemise et veste hotess.png', '05_jackets'],
        ['INCOMPATIBLE', 'combi space bas.png', '05_jackets'],
        
        ['INCOMPATIBLE', 'tenue sport haut.png', 'jupe hotesse.png'],
        ['INCOMPATIBLE', 'chaussures hotesse.png', 'combi space bas.png'],
        
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

        # Order Change
        ['ORDER_CHANGE', 'chaussures hotesse.png', '03_trousers'],
        ['ORDER_CHANGE', 'tenue sport haut.png', '03_trousers']
    ]

    # Optional layers (Accessories is not supported here)
    optional_layers = ['05_jackets', '08_glasses']
    
    # Optional layers rarity (List of rarity per layer)
    optional_rarity = [3, 5]
    
    # Background folder
    backgrounds_folder = '00_backgrounds'
    
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
