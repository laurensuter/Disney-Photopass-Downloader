#!/usr/bin/python

import string
import re #regex
import httplib, urllib, urllib2 #url encode
import json
from cookielib import CookieJar

save_location = "./"

def module_exists(module_name):
    try:
        __import__(module_name)
    except ImportError:
        return False
    else:
        return True


# Import user created settings. This will override built-in settings if defined.
if module_exists("config"):
    import config
else:
    print("Please set up the config.py file. Copy 'sample.config.py' to 'config.py' and set up options")
    sys.exit(2)

# Initializ cookie jar and session
cookies = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))

### Load the login page. This will initialize some cookies. Save them.
login_page = opener.open('https://disneyworld.disney.go.com/login/?returnUrl=https://mydisneyphotopass.disney.go.com/')
# cookies are automatically saved.

# grab the unique CSRF key. parse it.
csrf_key = re.search('id="pep_csrf" value=".*"', login_page.read())
csrf_key = csrf_key.group(0)
csrf_key = string.split(csrf_key, "\"") # split on double quote. easiest way.
csrf_key = csrf_key[len(csrf_key) - 2] # get the second to last item (last item is empty). array is 0-based, length is 1-based, so subtract 2

### Post the login page with credentials (and cookies). Save the cookies.
post_data = urllib.urlencode({'pep_csrf': csrf_key, 'username': config.username, 'password': config.password})
login_post = opener.open('https://disneyworld.disney.go.com/login/?returnUrl=https://mydisneyphotopass.disney.go.com/', post_data)

### Grab the list of photos with their unique ids and medium resolution urls
medium_url_list_html = opener.open("https://mydisneyphotopass.disney.go.com/slideshow/index/getMediumres")
medium_url_list = json.load(medium_url_list_html)
#print json.dumps(medium_url_list, sort_keys=True, indent=4)

### Grab the list of photo descriptions with their unique ids and timestamp and location information.
photo_detail_list_html = opener.open("https://mydisneyphotopass.disney.go.com/disney/ajax/getGuestMedia")
photo_detail_list = json.load(photo_detail_list_html)
### Link arrays by unique id.

### For each array item, download the image. Image filename target should be something
### like yyyy-mm-dd_hhmmss_location.jpg

### After saving, add EXIF information to include timestamp

