This is essentially an updated version for Python 3 of the older tool found here: https://github.com/glutanimate/image-occlusion-enhanced/tree/master/tools/io2-svg-fix

Older versions of the image occlusion add-on created malformed SVG files that resulted in the obscured "question area" being the same color as the other rectangles. This script fixes those images.

# Usage

Place the `svgfix.py` file in the profile directory (e.g. C:\Users\Name\AppData\Roaming\Anki2\User 1), next to the collection.media folder. Run the script with `python3 svgfix.py`.