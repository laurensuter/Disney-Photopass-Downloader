Notable `getGuestMedia` fields

##### `campus` - Overall park location
* `WDWPR` - Walt Disney World (PR - Public Relations?)

##### `venue` - Sub-Park location (sometimes events)
* `AK` animal kingdom
* `MNSSHP` - mickeys not so scary halloween party - located at magic kingdom
* `MK` - magic kingdom
* `EPCOT` - epcot
* `STUDIO` - hollywood studios

##### subjects - Characters in photo, or ride where photo was taken
* `RIDE` - rollercoaster or other ride photo
* Characters (can be a comma separated array)
 * `ALL MAGIC`
 * `AURORA`
 * `BEAST`
 * `BELLE`
 * `CHRSTTREE` - Christmas tree
 * `DAISY`
 * `DONALD`
 * `GOOFY`
 * `MAGIC`
 * `MICKEY`
 * `MINNIE`
 * `NONE` (this can show up in the same array list with others, so it doesn't mean there are no characters in the photo
 * `PLUTO`
 * `PLUTO\nNONE` - not sure what this is; looks like a coding mistake behind the scenes :-)
* Unique Ids
 * `ZZCBLV11`123 - I found 6 ids throughout my photos, usually taken at a character spot. the last 3 digits change, though likely all 5 digits can change based on the number of guests that day
 
##### `takenDate` - Date and timestamp when the photo was taken
##### `guestMediaCreateDate` - Date and timestamp when the photographer uplodaded the photo to the website/backend. Useless for us, but listed here so that it doesn't get confused with the other timestamp

##### `location` - Fairly specific location within the park where the photographer took the picture.
* `BUZZLIGHTYEARRIDE` - Buzz Lightyear Ride
* `ECENTR2` - Epcot Center - Epcot ball and flowers behind us
* `ENTR` - Magic Kingdom Entrance - just after security before going through the tunnels, with the building behind
* `ENTR3` - Animal Kingdom Entrance with Christmas Tree
* `HBFIVEDM` - Hollywood Studios with hat in the background (stock photo) - not sure what the initials stand for
* `MSATHCLB` - Main Street Athletic Club at Magic Kingdom
* `MSCASEYS` - Main Street Casey's Corner at Magic Kingdom - photo is past most of main street, with none of the shops visible in the photo
* `MSMKTHOU` - Main Street Magic Kingdom (THOU) - doesn't matter which way the photographer is facing (castle or opposite in background has same code)
* `RPWCHARACTER` - Rafiki's Planet Watch Character greeting (with Rafiki)
* `SPACEMOUNTAINA` - Space Mountain (Track A - to your left when you get shuffled to the left or right side - when you are at the ride gate, the car comes from the right and moves to the left)
* `TEST` - usually used for the bonus/stock photos
* `TSHOLIDAY` - just before main street, closup with the Christmas tree behind us
* `WSFRN` - World Showcase France at Epcot

##### `description` - Fairly generic description
* `Visiting Magic Kingdom Park`
* `Visiting Walt Disney World`
* `Visiting Donald Duck and friends`
* `Visiting Disneys Hollywood Studios`
* `Visiting Rafiki` - Rafiki's Planet Watch
* `Visiting The Christmas Tree and Walt Disney World`
* `Visiting The Christmas Tree`
* `Visiting Epcot`
* `Visiting Princess Aurora and friends`
* `Visiting Princess Belle`

##### `mediaCategory` - whether the photo was of the guest or the photo is a bonus photo (usually just posed characters)
* `GUEST_MEDIA` - Photo of the guest
* `STOCK_BONUS_GUEST` - Generic character photos

##### `mediaType` - photo or video
* `PHOTO`
* `ANIMATED MAGIC`
