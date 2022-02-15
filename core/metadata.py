from settings import CharacterSettings
from core import PathsHandling
from pathlib import Path
from core import Logger

import os


'''
JSON Structure:

{
    "image_path": "",
    "name": "",
    "external_link": "",
    "description": "",
    "attributes": [
        {
            "trait_type": "",
            "value": ""
        },
    ]
}
'''


class MetadataHandling:
    @staticmethod
    def generate_meta(
        metadata_path: os.path,
        metadata_bus: dict,
        settings: CharacterSettings
    ):
        '''Generates the metadata of all the NFTs,
        
        This method creates / reuse two files instead of one,
        it allows to delete the NFT metadata when using a macro,
        without loosing this NFT metadata
        '''
        
        attribute_format = {
            'trait_type': '',
            'value': ''
        }
        
        metadata = {
            'name': '',
            'description': settings.metadata_description,
            'image': '',
            'attributes': []
        }

        # List of all the attribute directories listed (Check settings.py)
        attributes_listed = settings.metadata_attributes.keys()
        
        for layer in attributes_listed:
            layer_name = settings.metadata_attributes[layer]
            
            # Copy & add the trait type (Example: '00_backgrounds': 'Background')
            current_attribute = attribute_format.copy()
            current_attribute['trait_type'] = layer_name
            
            # Get all the filenames used in the paths of this specific layer
            paths_in_layer = PathsHandling.get_paths_from_layer_name(metadata_bus, layer)
            filenames = PathsHandling.get_filename_from_paths(paths_in_layer)
            
            # Format the 'filenames' list and add it as a value
            current_attribute['value'] = str(filenames)[1:-1]
            
            # Fallback for an empty value
            if len(current_attribute['value']) == 0:
                current_attribute['value'] = 'None'
            
            # Include the final attribute inside the metadata dict
            metadata['attributes'].append(current_attribute)

        Logger.pyprint('WARN', 'METADATA TEST', metadata, True)