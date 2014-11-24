## Disney-Photopass-Downloader
### Greasemonkey Script
A greasemonkey script that alter's the Photopass page, allowing you to open each photo in a separate tab/window. From there, you can save each one individually in medium resolution (max 1280 pixels on one edge)

#### Known Issues
Firefox prevents this script from opening more than 20 tabs, even if popups are explicitely allowed for the photopass site.
* Workaround: Use the range function to download photos 20 at a time. After you save the first 20, increment the range input and click 'Open' to download the next 20.

### Python Linux Script
Run from a command prompt, this automatically downloads all photos, names them with a date and location filename, and sets both the EXIF timestamp and OS timestamp.

Requires the `jhead` package (for EXIF manipulation).

To run, first copy `sample.config.py` to `config.py`. Fill in your username (email) and password. Then run `python photopass-downloader.py`. It will download all photos to the script folder.
