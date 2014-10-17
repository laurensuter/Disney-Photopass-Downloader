#!/usr/bin/python

import re #regex
import urllib #url encode
import requests # library for processing html

cookie_location = "cookies.txt" 
save_location = "./"
username = ""
password = ""

# Import user created settings. This will override built-in settings if defined.
if module_exists("config"):
    import config
else:
    print("Please set up the config.py file. Copy 'sample.config.py' to 'config.py' and set up options")
    sys.exit(2)



### Load the login page. This will initialize some cookies. Save them.
html_session = requests.Session() # start a session to use cookies across urls
html_request = html_session.get('https://disneyworld.disney.go.com/login/?returnUrl=https://mydisneyphotopass.disney.go.com/')
# cookies are automatically saved.
# grab the unique CSRF key.
csrf_key = re.search('id="pep_csrf" value=".*"', html_request.text)
csrf_key = string.split(csrf_key, '"') # split on double quote. easiest way.

# get the second to last item (last item is empty). array is 0-based, length is 1-based, so subtract 2
csrf_key = csrf_key[len(csrf_key) - 2]

### Post the login page with credentials (and cookies). Save the cookies.
post_data = {'pep_csrf': urllib.quote(csrf_key), 'username': urllib.quote(username), 'password': urllib.quote(password)}
html_request = html_session.post("https://disneyworld.disney.go.com/login/?returnUrl=https://mydisneyphotopass.disney.go.com/", data=post_data)


### Grab the list of photos with their unique ids and medium resolution urls
medium_url_list = html_session.get("https://mydisneyphotopass.disney.go.com/slideshow/index/getMediumres")
meduim_url_list.json()

### Grab the list of photo descriptions with their unique ids and timestamp and location information.
photo_detail_list = html_session.get("https://mydisneyphotopass.disney.go.com/disney/ajax/getGuestMedia")
photo_detail_list.json()
### Link arrays by unique id.

### For each array item, download the image. Image filename target should be something
### like yyyy-mm-dd_hhmmss_location.jpg

### After saving, add EXIF information to include timestamp

