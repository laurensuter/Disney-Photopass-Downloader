#!/usr/bin/python

import string
import re #regex
import httplib, urllib, urllib2 #url encode
from cookielib import CookieJar
import requests # library for processing html

cookie_location = "cookies.txt" 
save_location = "./"
#username = "disney@schrauger.com"
#password = ""

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


### Load the login page. This will initialize some cookies. Save them.
#s = requests.session() # start a session to use cookies across urls
#html_request = s.get('https://disneyworld.disney.go.com/login/?returnUrl=https://mydisneyphotopass.disney.go.com/')

#login_page = urllib.urlopen('https://disneyworld.disney.go.com/login/?returnUrl=https://mydisneyphotopass.disney.go.com/')
cookies = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))
login_page = opener.open('https://disneyworld.disney.go.com/login/?returnUrl=https://mydisneyphotopass.disney.go.com/')

# cookies are automatically saved.
# grab the unique CSRF key.
#csrf_key = re.search('id="pep_csrf" value=".*"', html_request.content) # use content instead of text, because .text returns unicode
csrf_key = re.search('id="pep_csrf" value=".*"', login_page.read())

csrf_key = csrf_key.group(0)
csrf_key = string.split(csrf_key, "\"") # split on double quote. easiest way.

# get the second to last item (last item is empty). array is 0-based, length is 1-based, so subtract 2
csrf_key = csrf_key[len(csrf_key) - 2]

### Post the login page with credentials (and cookies). Save the cookies.
#post_data = {'pep_csrf': csrf_key, 'username': urllib.quote(config.username), 'password': urllib.quote(config.password)}

post_data = urllib.urlencode({'pep_csrf': csrf_key, 'username': config.username, 'password': config.password})

#html_request = s.post("https://disneyworld.disney.go.com/login/?returnUrl=https://mydisneyphotopass.disney.go.com/", data=post_data, allow_redirects=True)
#html_post = urllib.urlopen("https://disneyworld.disney.go.com/login/?returnUrl=https://mydisneyphotopass.disney.go.com/", post_data)
login_post = opener.open('https://disneyworld.disney.go.com/login/?returnUrl=https://mydisneyphotopass.disney.go.com/', post_data)


#print html_request.content
#media_html = opener.open("https://mydisneyphotopass.disney.go.com/mymedia/")
#print '#####'
#print media_html.read()
'''
### Grab the list of photos with their unique ids and medium resolution urls
medium_url_list = s.get("https://mydisneyphotopass.disney.go.com/slideshow/index/getMediumres")
print(medium_url_list.text)
medium_url_list.json()

### Grab the list of photo descriptions with their unique ids and timestamp and location information.
photo_detail_list = s.get("https://mydisneyphotopass.disney.go.com/disney/ajax/getGuestMedia")
photo_detail_list.json()
### Link arrays by unique id.

### For each array item, download the image. Image filename target should be something
### like yyyy-mm-dd_hhmmss_location.jpg

### After saving, add EXIF information to include timestamp

'''