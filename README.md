# Advanced NFTs Generator

This tool is made by [Yoratoni](https://github.com/yoratoni) for the [AstroDreamerz](https://astrodreamerz.io/) project.

As we wanted our NFTs to show the whole body of every character, some of our NFTs had more than 11 layers so we definitely needed to create our own generator.

On the technical side, this generator integrates a comparative hashing system allowing detection of potential duplicates. <br />
It also integrates an exception handling system (See below).

I decided to separate the program into two parts:
  - The first part only concerns the generated list of random paths (Random generation, optional layers, exception handling & comparative hashing).
  - The second part merges the images of the list together and saves the final NFT.

Why ? <br />
Because it is a lot more performant to detect exceptions & potential duplicates by checking the paths list
instead of doing that after generating the image (I don't want to destroy my SSD by saving / deleting invalid NFTs 10 times in a row..)

---

## Technical information:
  - Comparative hashing system to find duplicates based on the 128bits [xxHash](https://github.com/Cyan4973/xxHash) algorithm.
  - Debug mode that allows to verify an NFT (overwritten every x seconds)
  - Optimized system, it takes approximately 500ms to generate and save an NFT (1080x1080, 12 layers)
  - Optional layers & optional layers rarity
  - Image rarifier that virtually duplicates images into the paths list
  - Accessories handling (Allows multiple accessories)
  - Exceptions handling ('ORDER_CHANGE', 'INCOMPATIBLE' and 'DELETE')
  - [settings.py](settings/settings.py) to edit the settings for every character
  - Type hints, static method classes and full docstring for every method
  - Paths verification (everything is done before saving any file to the hard drive)
  - Custom logs system (pyprint & extime)



## The layers structure:
Note: I'm always using a number before the name (as VS Code sorts the directories by alphabetic order),
something like `00_backgrounds`, `07_hands` etc.. so all the layers are sorted in the correct order,
the first layer named `00_..` is generally the background, after that comes the face, the clothes etc..  <br />

Check this example:
```
input/
|-- character_0/
|   |-- 00_backgrounds/
|   |-- 01_faces/
|   |-- 02_trousers/
|   |-- 03_shirts/
|   |-- 04_jackets/
|   |-- etc..
|
|-- character_1/
    |-- 00_backgrounds/
    |-- 01_faces/
    |-- 02_foobar/
    |-- etc..
```

After that, the name `character_0` and the name `character_1` can be used inside the settings for the main function,
something like `character_directories = ['character_0', 'character_1']`



## Settings
All the settings can be modified inside the [settings.py](settings/settings.py) file. The first class called `GlobalSettings` concerns all the main settings such as the main input directory, the name of the characters (character_directories) and other debugging settings.

About the character settings: `ElonSettings` for example concerns the first character settings of our NFTs, this class, based on the `CharacterSettings` class allows to define custom parameters per character (exceptions, optional layers, etc..)

After defining your character classes, you need to modify these lines into the [generator.py](https://github.com/ostra-project/Advanced-NFTs-Generator/blob/main/libs/generator.py#L187) file

```py
# Character parameters obtained from the name
if character_name == GlobalSettings.character_directories[0]:
    settings = CharacterNumberOneSettings
elif character_name == GlobalSettings.character_directories[1]:
    settings = CharacterNumberTwoSettings
elif character_name == GlobalSettings.character_directories[2]:
    settings = CharacterNumberThreeSettings
```

_This will be modified later, I want this to be as simple as possible_



## The main function:
The `Generator.generate_nfts()` function, which is the main function, is actually pretty simple to understand.

Arguments:
  - The first argument is the final number of NFTs for the later-defined character.
  - The second argument is the name of the character (Defined inside the `character_directories` list (Check [settings.py](settings/settings.py))
  - [**OPTIONAL**] The `debug_mode_latency` argument is set to 0 by default, if modified, the generator will be in debug mode,
    in this mode, only one NFT is generated, using the name `DEBUG_NFT.png` to check if everything works perfectly fine.
    The value defined in this parameter is the number of sleeping milliseconds between two generated NFTs,
    I'm generally using 2500ms, it's enough to check a whole NFT.

This function also integrates an estimated time system, it generates a single NFT and multiply the time that it took by the final number of NFTs, this method is not really accurate because the complexity per NFT fully depends on the incompatibilites and the number of used images, but it gives at least an estimation.

![](docs/estimated_time.png "Estimated time log example")



## Handled exceptions:
You can check the [settings.py](settings/settings.py) file to have an example of these exceptions and how they works (It is for the AstroDreamerz project so, it's not really pretty lol)

  <br />

  - `'ORDER_CHANGE'`: <br />
    Allows you to put an image/layer before another image/layer, the first parameter concerns the name of the layer/image that will go before the layer/image precised by the         second parameter. <br />
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
      


## Logger class:
Pyprint is a simple custom logging system made to get a lot of formatted data about the generation of the NFTs,
this class also integrated the extime method that prints the formatted execution time. Verbose debugging can be turned off inside the `GlobalSettings` class to reduce the amount of printed data.

Here's an example of a `pyprint()` log:

![](docs/pyprint.png "Pyprint logs example")

This class uses [Colorama](https://github.com/tartley/colorama) to print colored terminal text. 








