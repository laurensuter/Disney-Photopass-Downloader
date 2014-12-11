# Disney Photopass Downloader
This repo contains two programs designed to download medium resolution Photopass images. These images are the same ones seen in the built-in slideshow page on the Photopass website. If you want full resolution images, you'll have to actually purchase them, but the medium resolution images are sufficient for facebook.

The first program is a UserScript, which installs to your browser and gives you a couple of links on the Photopass website to download your photos.

Alternatively, the Python script, which currently only runs on Linux, lets you batch download all the photos, and it also saves the files with useful names and sets the proper timestamps.

## UserScript
A UserScript (greasemonkey script) that alters the Photopass page, allowing you to download each photo individually in medium resolution (max 1280 pixels on one edge). It will also save the filename based on the location and date/time that the photo was taken.

### Installation Instructions
For Firefox or Chome, the easiest way to install the script is to first have [GreaseMonkey][greasemonkey] (Firefox) or [TamperMonkey][tampermonkey] (Chrome). If you have those addons installed already, simply [open the script][script] and follow the prompts to install it.
[greasemonkey]: https://addons.mozilla.org/en-us/firefox/addon/greasemonkey/
[tampermonkey]: https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkf
[script]: https://raw.githubusercontent.com/schrauger/Disney-Photopass-Downloader/master/greasemonkey/Photopass_Downloader.user.js

### Known Issues
* Firefox prevents this script from opening more than 20 tabs, even if popups are explicitely allowed for the photopass site.
 * Workaround: Use the range function to download photos 20 at a time. After you save the first 20, increment the range input and click 'Open' to download the next 20.
* Images do not contain date/time information<del>, and the names are random</del>. This cannot be altered by JavaScript and thus cannot be modified solely with this Greasemonkey script. Try the Linux Python script for those advanced features.

## Python Linux Script
Run from a command prompt, this automatically downloads all photos, names them with a date and location filename, and sets both the EXIF timestamp and OS timestamp.

Requires the `jhead` package (for EXIF manipulation).

To run, first copy `sample.config.py` to `config.py`. Fill in your username (email) and password. Then run `python photopass-downloader.py`. It will download all photos to the script folder.
