#!/usr/bin/python

import string
import time
import re #regex
import httplib, urllib, urllib2 #url encode, image saving
import json
from cookielib import CookieJar
import datetime
#from datutil.parser import parse #requires python-dateutil package. used to parse with timezone

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

for photo in photo_detail_list['guestMedia']:
	
	id = photo['guestMediaId']
	if medium_url_list[id]: #if both lists have same id, continue. in medium_url_list, id is the json key.
		url = medium_url_list[id]
		date_created = photo['takenDate']
		
		# get timestamp
		timezone = re.search('[-+][0-9]{2}:[0-9]{2}$', date_created).group(0)
		timezone_hour = (int)(timezone[:3]) # characters 0, 1, and 2
		timezone_minute = (int)(timezone[:1] + timezone[4:]) # the arithmetic sign and the minute portion (there exist some timezones with half hour offsets)
		date_created = re.sub('([+-][0-9]{2}):([0-9]{2})$', '', date_created) #remove timezone at end
		date_created = datetime.datetime.strptime(date_created, '%Y-%m-%dT%H:%M:%S') #convert to datetime
		date_created_utc = date_created + datetime.timedelta(hours=(-1 * timezone_hour))
		date_created_utc = date_created_utc + datetime.timedelta(minutes=(-1 * timezone_minute))
		# doesn't currently use the uct timestamp, but in the future, this script could let the user
		# force utc, or their local timestamp. that way, if they forgot to change their camera clocks,
		# at least these photos would line up chronologically.
		date_created_string = datetime.datetime.strftime(date_created, '%Y-%m-%d %H_%M_%S') # readable string for file save
		
		#print date_created_utc
		location = photo['venue'] #AK {animal kingdom], MK {magic kingdom}, EPCOT, MNSSHP {mickeys not so scary halloween party - located at magic kingdom}
		filename = date_created_string + ' ' + location + '.jpg' #default to current folder. also assumes jpg
		#print url
		urllib.urlretrieve(url, filename) # gets the file and saves it
		
#  url = photo['url']
#  date_created = photo_detail_list[photo['id']]
#  date_created_format = date('yyyy-mm-dd', date_created)
#  location = photo_detail_list[photo['venue']]
#  save_location = save_directory + '/' + date_created_format + location + '.jpg'
#  wget url > save_location
#  addexif date=date_created save_location





### For each array item, download the image. Image filename target should be something
### like yyyy-mm-dd_hhmmss_location.jpg

### After saving, add EXIF information to include timestamp

