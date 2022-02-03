# Advanced NFTs Generator

This tool is made by [Yoratoni](https://github.com/yoratoni) for the [AstroDreamerz](https://astrodreamerz.io/) project.

As we want our NFTs to show the whole body of the characters, we have more than 11 layers per character so we needed to create our own NFTs generator.

On the technical side, this generator integrates a comparative hashing system allowing duplicates detection and random paths regeneration as it is a lot more performant to detect exceptions and to regenerate only the paths list before generating / merging the images.

---

### Technical information:
  - Comparative hashes system to find duplicates based on the 128bits [xxHash](https://github.com/Cyan4973/xxHash) algorithm.
  - Debug mode that allows to verify an NFT (overwritten every x seconds)
  - Optimized system, it takes approximately 500ms to generate and save an NFT (1080x1080, 13 layers)
  - Path modulation (everything is done before saving any file to the hard drive)
  - Custom logs system (pyprint & extime)
  - Optional layers & optional layers rarity
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

This function also integrates an estimated time system, it generates a single NFT and multiply the timer value by the final number of NFTs, this method is not really accurate because of the complexity caused by the incompatibilities, but it gives at least an estimation.

![](docs/estimated_time.png "Estimated time log example")

### Handled exceptions:
You can check the [settings.py](settings/settings.py) file to have an example of these exceptions and how they works (It is for the AstroDreamerz project so, it's not really pretty lol)

  - `'ORDER_CHANGE'`: <br />
      Allows you to put an image/layer before another image/layer, the first parameter concerns the name of the layer/image that will go before the layer/image precised by the second parameter. <br />
      <br />
      The format is simply the name of the image with the .png extension, or the name of the directory in the case of the layer mode.
      - Change the order between two images: <br />
        `["ORDER_CHANGE", "image", "put_before_this_image"]`
      - Change the order between one image and one layer: <br />
        `["ORDER_CHANGE", "image", "put_before_this_layer"]`
      - Change the order between a layer and one image: <br />
        `["ORDER_CHANGE", "layer", "put_before_this_image"]`
      - **[NOT YET IMPLEMENTED]** Change the order between a layer and another layer: <br />
        `["ORDER_CHANGE", "layer", "put_before_this_layer"]`
        <br />
        <br />
        
  - `'INCOMPATIBLE'`: <br />
      Allows you to make two images (or one image and a whole layer) incompatible, if they're used together, the generated NFT will be considered as incompatible, and another NFT will be generated (everything works by path modulation, so before saving the valid NFT on the HDD/SSD, it's a lot more faster that way). <br />
      
      The order of the names doesn't matter.
      - NFT is regenerated if all the listed images are used: <br />
      `["INCOMPATIBLE", "image_1", "image_2", ...]`
      - NFT is regenerated if the image is used with an image that comes from this specific layer **(Only one image and one layer)**: <br />
      `["INCOMPATIBLE", "image.png", "layer"]`
      <br />
    
  - `'DELETE'`: <br />
      Allows you to delete one or multiple layers if a specific image is used, it can be used in the case of a mandatory layer (any layer that is not specified inside the layer list). Note that this exception should be noted first (exceptions are handled in the order of the list) so any other exception is not handled for nothing (It would still works but it's less performant)<br />
      
      It can be used for something that overrides multiple layers like a space suit. <br />
      Precise the image first, and any number of layers after it.
      - In this example, if 'space suit.png' is detected, all the images of these layers will be deleted: <br />
      `['DELETE', 'space suit.png', '05_jackets', '03_trousers']` 
      
### Logger class:
Pyprint is a simple custom logging system made to get a lot of formatted data about the generation of the NFTs,
this class also integrated the extime method that prints the formatted execution time. Verbose debugging can be turned off inside the `GlobalSettings` class to reduce the amount of printed data.

Here's an example of a `pyprint()` log:

![](docs/pyprint.png "Pyprint logs example")

This class uses [Colorama](https://github.com/tartley/colorama) to print colored terminal text. 








