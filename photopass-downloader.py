#!/usr/bin/python

import os
import sys
import string
import time
import re  # regex
import httplib, urllib, urllib2  # url encode, image saving
import json
from cookielib import CookieJar
import datetime
from subprocess import call  # call linux command to set exif data

# from datutil.parser import parse #requires python-dateutil package. used to parse with timezone
# from gi.repository import GExiv2 # requires python-gi
save_location = "./photos/"


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


# Initialize cookie jar and session
cookies = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))

print("Load login page")

### Load the login page. This will initialize some cookies. Save them.
login_page = opener.open('https://disneyworld.disney.go.com/login/?returnUrl=https://mydisneyphotopass.disney.go.com/')
# cookies are automatically saved.

# grab the unique CSRF key. parse it.
csrf_key = re.search('id="pep_csrf" value=".*"', login_page.read())
csrf_key = csrf_key.group(0)
csrf_key = string.split(csrf_key, "\"")  # split on double quote. easiest way.
csrf_key = csrf_key[len(csrf_key) - 2]  # get the second to last item (last item is empty). array is 0-based, length is 1-based, so subtract 2

print("POST login info")
### Post the login page with credentials (and cookies). Save the cookies.
post_data = urllib.urlencode({'pep_csrf': csrf_key, 'username': config.username, 'password': config.password})
login_post = opener.open('https://disneyworld.disney.go.com/login/?returnUrl=https://mydisneyphotopass.disney.go.com/', post_data)

print("Get photo URLs")
### Grab the list of photos with their unique ids and medium resolution urls
medium_url_list_html = opener.open("https://mydisneyphotopass.disney.go.com/slideshow/index/getMediumres")
medium_url_list = json.load(medium_url_list_html)
#print (json.dumps(medium_url_list, sort_keys=True, indent=4))

print("Get photo details")
### Grab the list of photo descriptions with their unique ids and timestamp and location information.
photo_detail_list_html = opener.open("https://mydisneyphotopass.disney.go.com/disney/ajax/getGuestMedia")
photo_detail_list = json.load(photo_detail_list_html)
### Link arrays by unique id.

if not os.path.exists(save_location):
    os.makedirs(save_location)

print("Save photos")
for photo in photo_detail_list['guestMedia']:

    photo_id = photo['guestMediaId']
    if medium_url_list[photo_id]:  # if both lists have same id, continue. in medium_url_list, id is the json key.
        url = medium_url_list[photo_id]
        date_created = photo['takenDate']
        media_type = photo['mediaType'] # can be "PHOTO" or "ANIMATED MAGIC" (video)

        # get timestamp
        timezone = re.search('[-+][0-9]{2}:[0-9]{2}$', date_created).group(0)
        timezone_hour = (int)(timezone[:3])  # characters 0, 1, and 2
        timezone_minute = (int)(timezone[:1] + timezone[4:])  # the arithmetic sign and the minute portion (there exist some timezones with half hour offsets)
        date_created = re.sub('([+-][0-9]{2}):([0-9]{2})$', '', date_created)  # remove timezone at end
        date_created = datetime.datetime.strptime(date_created, '%Y-%m-%dT%H:%M:%S')  # convert to datetime
        date_created_utc = date_created + datetime.timedelta(hours=(-1 * timezone_hour))
        date_created_utc = date_created_utc + datetime.timedelta(minutes=(-1 * timezone_minute))
        # doesn't currently use the uct timestamp, but in the future, this script could let the user
        # force utc, or their local timestamp. that way, if they forgot to change their camera clocks,
        # at least these photos would line up chronologically.
        date_created_string = datetime.datetime.strftime(date_created, '%Y-%m-%d %H_%M_%S')  # readable string for file save
        #print (date_created_utc)

        location = photo['venue']  # AK {animal kingdom], MK {magic kingdom}, EPCOT, MNSSHP {mickeys not so scary halloween party - located at magic kingdom}
        filename = save_location + '/' + date_created_string + ' ' + location + ' ' + photo_id + '.jpg'  # default to current folder. also assumes jpg
        #print (url)
        if url:  # one final check to make sure the url is defined
            urllib.urlretrieve(url, filename)  # gets the file and saves it
            date_created_exif_format = datetime.datetime.strftime(date_created, '%Y:%m:%d-%H:%M:%S')
            #exif = GExiv2.Metadata(filename)
            #exif['Exif.Image.DateTime'] = date_created_exif_format
            #exif['Exif.Photo.DateTimeDigitized'] = date_created_exif_format
            #exif['Exif.Photo.DateTimeOriginal'] = date_created_exif_format
            #exif.save_file()

            if (media_type != "ANIMATED MAGIC"):  # If video, don't change exif. Otherwise, assume it's a PHOTO (I'll add other cases as they come up)
                try:
                    call(['jhead', '-mkexif', filename])  # initialize exif
                    call(['jhead', '-ts' + date_created_exif_format, filename])  # set timestamp
                    call(['jhead', '-ft', filename])  # set the OS timestamp to be the same as the exif timestamp
                except OSError as e:
                    print("'jhead' is not installed. EXIF and OS timestamp not set.")
            else:
                print("Media type is video. 'jhead' only works on jpg files. Timestamp not set.")  # Perhaps in the future, I'll use a tool that works on videos.

### After saving, add EXIF information to include timestamp
