# Python scripts for SVG

Theese scripts were made when I had a designer that liked to send icons as `Icon-Name@2.png`.  
To fix that, I had to rename that to `xhdpi/icon_name.png`.

The file `icon converting/convert_svg.py` uses the `inscape command line` to convert a SVG to multiple PNGs.  
The generated files use the same naming convention as my designer, so that `icon converting/androidify_icons.py` can
rename them and put them in the appropriate folders.

The scripts in `icon resizing/` might create incorrect results, as I didn't use them much.  
They require `Pillow` (install with `pip install Pillow`)


# Usage

## convert_svg.py

Set the name of the SVG file in the variable `input_file`. Set it's base (1x, mdpi) size in `size`.  
Then run with python.

## androidify_icons.py

Drop a bunch of `png` files in the same folder as the script, and run. Make sure they follow the strange
naming convention; that way it can read the scale and put it in the correct drawable folders.
