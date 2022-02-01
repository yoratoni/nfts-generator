# NFTs Advanced Generator

This tool is made by Yoratoni for the AstroDreamerz project.

As we wanted our NFTs to show the whole body of the characters, we had more than 11 layers so we needed to create our own NFTs generator.

On the technical side, this generator integrates a comparative hashing system based on the [xxHash](https://github.com/Cyan4973/xxHash) non-cryptographic hashing algorithm allowing duplicates detection and random regeneration as it is a lot performant to detect exceptions before generating the images.

This generator also integrates exceptions handling, optional layers, optional rarity and an image rarifier.

---

### Handled exceptions:
  - `'ORDER_CHANGE'`:
      - Allows you to put an image before another image if used OR another layer (directory).
      - Change the order between two images: <br />
        `["ORDER_CHANGE", "name_1", "name_2"]`
      - Change the order between one image and one layer: <br />
        `["ORDER_CHANGE", "name", "layer"]`
        
  - `'INCOMPATIBLE'`:
      - NFT is regenerated if all the listed images are used: <br />
      `["INCOMPATIBLE", "image_1", "image_2", ...]`
      - NFT is regenerated if one of the images is inside a layer (Only one image and one layer): <br />
      `["INCOMPATIBLE", "image.png", "layer"]`
      
  - `'DELETE'`:
      - Deletes all the images of specific layers if the specified image is used
      - It can be used for overriding layers such as a space suit where all the jackets needs to be deleted
      - In this example, if 'space suit.png' is detected, all the images of these layers will be deleted:
      `['DELETE', 'space suit.png', '05_jackets', '03_trousers']`
      
### Logger class:
Pyprint is a simple custom logging system made to get a lot of formatted data about the generation of the NFTs,
this class also integrated the extime method that prints the formatted execution time.

This class uses [Colorama](https://github.com/tartley/colorama) to print colored terminal text. 

Here's an example of a `pyprint()` log:
![Alt text](docs/pyprint.png "Pyprint logs example")

      
      
