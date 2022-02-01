# NFTs Advanced Generator

This tool is made by [Yoratoni](https://github.com/yoratoni) for the [AstroDreamerz](https://astrodreamerz.io/) project.

As we wanted our NFTs to show the whole body of the characters, we had more than 11 layers so we needed to create our own NFTs generator.

On the technical side, this generator integrates a comparative hashing system allowing duplicates detection and random regeneration as it is a lot more performant to detect exceptions before generating the images.

---

### Technical information:
  - Comparative hashes system to find duplicates based on the 128bits [xxHash](https://github.com/Cyan4973/xxHash) algorithm.
  - Debug mode that allows to verify an NFT (overwritten every x seconds)
  - Optimized system, it takes approximately 500ms to generate and save an NFT (1080x1080, 13 layers)
  - Custom logs system (pyprint & extime)
  - Optional layer & optional rarity
  - Image rarifier that virtually duplicates images into the paths list
  - Accessories handling (Allows multiple accessories)
  - Exceptions handling ('ORDER_CHANGE', 'INCOMPATIBLE' and 'DELETE')
  - [settings.py](settings/settings.py) to edit the settings for every character
  - Type hints, static method classes and full docstring for every method

### The main function:
Every setting can be modified inside the `Generator.generate_nfts()` function, ElonSettings for example concerns the first character settings of our NFTs, this class, based on the CharacterSettings class allows to define custom parameters for multiple character, the main function can be later called with only two arguments.

```py
# Character parameters obtained from the name
if character_name == GlobalSettings.character_folders[0]:
    settings = ElonSettings
elif character_name == GlobalSettings.character_folders[1]:
    settings = JeffSettings
elif character_name == GlobalSettings.character_folders[2]:
    settings = RichardSettings
```

The `debug_mode_latency` argument is set to 0 by default, if modified, the generator will be in debug mode,
in this mode, only one NFT is generated, using the name `DEBUG_NFT.png` to check if everything works perfectly fine.

The value defined in this parameter is the number of sleeping milliseconds between two generated NFTs,
I'm generally using 2500ms, it's enough to check a whole NFT.

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
this class also integrated the extime method that prints the formatted execution time. Verbose debugging can be turned off inside the `GlobalSettings` class to reduce the amount of printed data.

Here's an example of a `pyprint()` log:

![Alt text](docs/pyprint.png "Pyprint logs example")

This class uses [Colorama](https://github.com/tartley/colorama) to print colored terminal text. 








