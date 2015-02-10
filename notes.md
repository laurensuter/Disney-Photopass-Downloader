Notable `getGuestMedia` fields. *Italics* indicate values found in other photos, not ones I have personally seen.

##### `campus` - Overall park location
* `WDWPR` - Walt Disney World Parks & Resorts

##### `venue` - Sub-Park location/hotel (sometimes events)
* `AK` animal kingdom
* `MNSSHP` - mickeys not so scary halloween party - located at magic kingdom
* `MK` - magic kingdom
* `EPCOT` - epcot
* *`POLY`* - Polynesian Resort
* `STUDIO` - hollywood studios

##### subjects - Characters in photo, or ride where photo was taken
* `RIDE` - rollercoaster or other ride photo
* Characters (can be a comma separated array)
 * `ALL MAGIC`
 * `ANNA`
 * `AURORA`
 * `BEAST`
 * `BELLE`
 * `CHRSTTREE` - Christmas tree
 * `CIND` - Cinderella
 * `DAISY`
 * `DONALD`
 * `ELSA`
 * `FLYNNRYDER`
 * `GOOFY`
 * `JACK` - Jack Skellington
 * `MAGIC`
 * `MICKEY`
 * `MINNIE`
 * `NONE` (this can show up in the same array list with others, so it doesn't mean there are no characters in the photo
 * `PCHARM` - Prince Charming
 * `PLUTO`
 * `PLUTO\nNONE` - not sure what this is; looks like a coding mistake behind the scenes :-)
 * `RAPUNZEL`
 * `SCROOGE` - During the Not So Scary Halloween party, at a character greeting
* Unique Ids
 * `ZZCBLV11`123 - I found multiple ids throughout my photos, usually taken at a character spot. the last 3 digits change, though likely all 5 digits can change based on the number of guests that day
 
##### `takenDate` - Date and timestamp when the photo was taken
##### `guestMediaCreateDate` - Date and timestamp when the photographer uplodaded the photo to the website/backend. Useless for us, but listed here so that it doesn't get confused with the other timestamp

##### `location` - Fairly specific location within the park where the photographer took the picture.

Code | Venue | Acronym | Details
---- | ----- | ------- | -------
*`BRDGMDL`* | Animal Kingdom | Bridge Middle | Tree of Life in background
`BRDGTOP` | Animal Kingdom | Bridge Top | 
`BUZZLIGHTYEARRIDE` | Magic Kingdom | Buzz Lightyear Ride
`CHRCON3` | Epcot | (possibly) Christmas Concert 3 |Just before the world showcase loop (taken during food and wine festival on Jan 3)
*`DINOSAURRIDE`* | Animal Kingdom | Dinosaur Ride
*`DPIRIDESYSGMTT`* | Epcot | (Disney Photo Imaging Ride System General Motors Test Track) | Test Track Ride
`ECENTR1` | Epcot | Epcot Center 1 | Closer to the epcot ball (compared to ecentr2)
`ECENTR2` | Epcot | Epcot Center 2 | Epcot ball and flowers behind us
*`ECENTR4`* | Epcot | Epcot Center 4 | (need to find a way to describe all these ecentr# locations)
`ENTR` | Magic Kingdom | Entrance | just after security before going through the tunnels, with the building behind
`ENTR1` | Magic Kingdom | Entrance 1 | random places when assigned to stock photos
`ENTR3` | Animal Kingdom | Entrance 3 | with Christmas Tree
`ENTRTR1` | Magic Kingdom | Entrance (TR?) 1 | close to the castle stage (stock photo)
*`EVRST3`* | Animal Kingdom | Expedition Everest 3 | Expedition Everist ride sign
*`EVRST4`* | Animal Kingdom | Expedition Everest 4 | Bridge near Expedition Everest
*`EXPEDITIONEVERESTRIDE`* | Animal Kingdom | Expedition Everest Ride
`FNTSYBRG` | Magic Kingdom | Fantasy Bridge | bridge to New Fantasy Land, with castle in background
`HBFIVEDM` | Hollywood Studios | (possibly) Hollywood Big Five (DM - Disney something?) | hat in the background (stock photo)
*`ENCHANTEDTALESBLUE`* | Magic Kingdom | Enchanted Tales Blue | Blue side
*`ENCHANTEDTALESPURPLE`* | Magic Kingdom | Enchanted Tales Purple |Purple side
*`MINETRAIN`* | Magic Kingdom | Mine Train | Ride photo
`MSATHCLB` | Magic Kingdom | Main Street Athletic Club |
*`MSCINEMA`* | Magic Kingdom | Main Street Cinema |
`MSFIRSTA` | Magic Kingdom | Main Street First A | Main Street just after the first loop
`MSCASEYS` | Magic Kingdom | Main Street Casey's Corner | photo is past most of main street, with none of the shops visible in the photo
*`MSGAZETT`* | Magic Kingdom | Main Street Gazette |
`MSMKTHOU` | Magic Kingdom | Main Street Magic Kingdom (THOU?) |
*`OHANA`* | Polynesian Resort | 'Ohana | Character dining
`OSBLIGHT2` | Hollywood Studios | Osbourn Lights 2 | Merry Christmas sign is behind us; photo was taken at the intersection inside the main light area
`PFTHBLUEA1CHAR` | Magic Kingdom | Princess Fairytale Hall Blue A 1 Character | Met Anna; This was the left side, I think (as you wait in line)
`PFTHBLUEA2CHAR` | Magic Kingdom | Princess Fairytale Hall Blue A 2 Character | Met Elsa; This was the left side, I think (as you wait in line)
`PFTHPURPLEB1CHAR` | Magic Kingdom | Princess Fairytale Hall Purple B 1 Character | Met Flynn Ryder and Princess Rapunzel; This was the right side, I think
`PFTHPURPLEB2CHAR` | Magic Kingdom | Princess Fairytale Hall Purple B 2 Character | Met Princess Cinderella and Prince Charming
*`ROCKNRCOASTERRIDE`* | Hollywood Studios | Rock'n Roller Coaster Ride |
*`ROVER1`* | Hollywood Studios | Rover 1 | with hat in background - not sure what Rover refers to
`RPWCHARACTER` | Animal Kingdom | Rafiki's Planet Watch Character |
`SPACEMOUNTAINA` | Magic Kingdom | Space Mountain Ride Track A | to your left when you get shuffled to the left or right side - when you are at the ride gate, the car comes from the right and moves to the left
`SPACEMOUNTAINB` | Magic Kingdom | Space Mountain Ride Track B
`SBCCALLIOPECHAR` | Magic Kingdom | ? | Circus area. (not sure about the acronym; best I could come up with is Sleeping Beauty Castle Calliope Character, which makes no sense. SBC is in California, and Calliope is one of the Muses in Hercules.)
`SBCMARQUEECHAR` | Magic Kingdom | ? | close to circus area. Again, acronym doesn't make sense. Maybe programmers just reuse old codes rather than generate new ones for specific character meets.
*`SPLASH`* | Magic Kingdom | Splash | Splash Mountain Ride 
*`STUDIOARCH`* | Hollywood Studios | Studio Arch | HOllywood Studios Arch in background
*`SUNSET2`* | Hollywood Studios | Sunset 2 | Tower of Terror in background
`TEST` | N/A | Test | usually used for the bonus/stock photos
`TOMBRDG1` | Magic Kingdom | Tomorrowland Bridge 1 | the castle in the background
*`TOWEROFTERRORARIDE`* | Hollywood Studios | Tower of Terror Ride Track A |
*`TOWEROFTERRORBRIDE`* | Hollywood Studios | Tower of Terror Ride Track B |
`TREEBACK` | Animal Kingdom | Tree Back | angle of the Tree of Life, framed by trees closer to the subjects
`TSHOLIDAY` | Magic Kingdom | TS Holiday | just before main street, inside the street loop where the flagpole is (and where the Christmas tree or pumpkin display is set up during the holiday)
`TSHOLICON` | Magic Kingdom | TS Holiday (CON?) | same as `TSHOLIDAY`, I think.
*`VERCHAR1`* | Magic Kingdom | (VER?) Character 1 | walkway by river near castle (character greeting spot)
`WRLDSHW3` | Epcot | World Showcase 3 | in front of the fountain (by France, I think)
`WSFRN` | Epcot | World Showcase France |
`WSMEX` | Epcot | World Showcase Mexico |

##### `description` - Fairly generic description
* `Visiting Anna and Elsa`
* `Visiting Daisy Duck and friends`
* `Visiting Disneys Animal Kingdom Park`
* `Visiting Disneys Hollywood Studios`
* `Visiting Donald Duck`
* `Visiting Donald Duck and friends` - the `f` in friends is not capitalized
* `Visiting Elsa`
* `Visiting Epcot`
* `Visiting Flynn Ryder and Princess Rapunzel` - Princess Fairytale Hall during Christmas party
* `Visiting Jack Skellington`
* `Visiting Magic Kingdom Park`
* `Visiting Mickeys Not So Scary Halloween Party`
* `Visiting Mickeys Very Merry Christmas Party`
* `Visiting Minnie Mouse` - at Epcot Center
* `Visiting Princess Aurora and friends` - the `f` in friends is not capitalized
* `Visiting Princess Belle`
* `Visiting Princess Cinderella and Prince Charming` - Princess Fairytale Hall during Christmas party
* `Visiting Rafiki` - Rafiki's Planet Watch
* `Visiting The Christmas Tree`
* `Visiting The Christmas Tree and Walt Disney World`
* `Visiting Walt Disney World`

##### `mediaCategory` - whether the photo was of the guest or the photo is a bonus photo (usually just posed characters)
* `GUEST_MEDIA` - Photo of the guest (usually; sometimes, stock photos are given this tag)
* `STOCK_BONUS_GUEST` - Generic character photos

##### `mediaType` - photo or video
* `PHOTO`
* `ANIMATED MAGIC`
