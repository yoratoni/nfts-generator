from settings import GlobalSettings, CharacterSettings
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
        settings: CharacterSettings
    ):
        '''Generates the metadata of an NFT (IPFS/ERC OpenSea format).
        
        Notes:
            - The 'name' attribute is filled during the final NFT mix.
            - The 'tokenId' attribute is also filled during the final NFT mix.
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
            'tokenId': 0,
            'name': '',
            'description': settings.metadata_description,
            'attributes': []
        }

        # List of all the attribute directories listed (Check settings.py)
        attributes_listed = settings.metadata_attributes.keys()
        
        # Final sorted list of all the attributes
        final_attributes_list = []
        
        # Adding the character trait first
        character_attribute = attribute_format.copy()
        character_attribute['trait_type'] = 'Character'
        character_attribute['value'] = settings.character_name
        final_attributes_list.append(character_attribute)
        
        for layer in attributes_listed:
            value = settings.metadata_attributes[layer]
            
            # Check if the value is a list (Fallback trait value)
            if type(value) == list:
                trait_type = value[0]
                other_layer = value[1]
            else:
                trait_type = value
                other_layer = None
            
            # Copy & add the trait type (Example: '00_backgrounds': 'Background')
            current_attribute = attribute_format.copy()
            current_attribute['trait_type'] = trait_type
            
            # Get all the filenames used in the paths of this specific layer
            paths_in_layer = PathsHandling.get_paths_from_layer_name(metadata_bus, layer)
            filenames = PathsHandling.get_filename_from_paths(paths_in_layer)
            
            # If no filenames found, don't include this attribute
            if filenames is not None:
                current_attribute['value'] = filenames
                final_attributes_list.append(current_attribute)
                
            # Apply another trait value (other layer) if the metadata attribute is a list 
            elif other_layer is not None:
                paths_in_layer = PathsHandling.get_paths_from_layer_name(metadata_bus, other_layer)
                current_attribute['value'] = PathsHandling.get_filename_from_paths(paths_in_layer)
                final_attributes_list.append(current_attribute)
        
        metadata['attributes'] = final_attributes_list
        
        # Saves the metadata into a JSON file
        save_name = nft_name[:-4]
        save_path = os.path.join(metadata_path, f'{save_name}.json')
        with open(save_path, 'w+') as file:
            json.dump(metadata, file, indent=4)

        Logger.pyprint('SUCCESS', '', f'Metadata generated for "{nft_name}"', True)
        print('')
        