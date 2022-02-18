from settings import CharacterSettings
from core import PathsHandling
from core import Logger

import json
import os


class MetadataHandling:
    @staticmethod
    def generate_meta(
        metadata_path: os.path,
        metadata_bus: dict,
        nft_name: str,
        token_id: int,
        settings: CharacterSettings
    ):
        '''Generates the metadata of an NFT (IPFS/ERC OpenSea format).
        
        Notes:
            - The 'name' attribute is filled during the final NFT mix.
            - The 'image' attribute is the IPFS url, should be filled after the final Pinata upload
        '''
        
        # The original format of one attribute
        attribute_format = {
            'trait_type': '',
            'value': ''
        }
        
        # The original metadata format
        metadata = {
            'image': '',
            'tokenId': token_id,
            'name': '',
            'description': settings.metadata_description,
            'attributes': []
        }

        # List of all the attribute directories listed (Check settings.py)
        attributes_listed = settings.metadata_attributes.keys()
        
        # Adding the character trait first
        character_attribute = attribute_format.copy()
        character_attribute['trait_type'] = 'Character'
        character_attribute['value'] = settings.character_name
        metadata['attributes'].append(character_attribute)
        
        # Adding every listed layer
        for layer in attributes_listed:
            # Copy & add the trait type (Example: '00_backgrounds': 'Background')
            current_attribute = attribute_format.copy()
            current_attribute['trait_type'] = settings.metadata_attributes[layer]
            
            # Get all the filenames used in the paths of this specific layer
            paths_in_layer = PathsHandling.get_paths_from_layer_name(metadata_bus, layer)
            filenames = PathsHandling.get_filename_from_paths(paths_in_layer)
            
            # If no filenames found, don't include this attribute
            if filenames is not None:
                current_attribute['value'] = filenames
                
                # Include the final attribute inside the metadata dict
                metadata['attributes'].append(current_attribute)

        # Saves the metadata into a JSON file
        save_name = nft_name[:-4]  # Removes the '.png' extension
        save_path = os.path.join(metadata_path, f'{save_name}.json')
        with open(save_path, 'w+') as file:
            json.dump(metadata, file, indent=4)

        Logger.pyprint('SUCCESS', '', f'Metadata generated for "{nft_name}"')
        print('')
        