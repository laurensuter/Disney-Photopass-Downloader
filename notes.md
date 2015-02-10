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
* *`BRDGMDL`* - Bridge at Animal Kingdom with Tree of Life in background (not sure what MDL means)
* `BRDGTOP` - Bridge Top at Animal Kingdom
* `BUZZLIGHTYEARRIDE` - Buzz Lightyear Ride
* `CHRCON3` - At Epcot, just before the world showcase loop (taken during food and wine festival) - not sure what the acronym is, unless it is related to CHRistmas CONcert (photo taken Jan 3)
* *`DINOSAURRIDE`* - Dinosaur Ride at Animal Kingdom
* *`DPIRIDESYSGMTT`* - Disney Test Track Ride at Epcot (Disney Photo Imaging Ride System General Motors Test Track)
* `ECENTR1` - Epcot Center - Closer to the epcot ball (compared to ecentr2)
* `ECENTR2` - Epcot Center - Epcot ball and flowers behind us
* *`ECENTR4`* - Epcot Center (need to find a way to describe all these ecentr# locations)
* `ENTR` - Magic Kingdom Entrance - just after security before going through the tunnels, with the building behind
* `ENTR1` - Magic Kingdom (random places when assigned to stock photos)
* `ENTR3` - Animal Kingdom Entrance with Christmas Tree
* `ENTRTR1` - Magic Kingdom Entrance close to the castle stage (stock photo)
* *`EVRST3`* - Expedition Everest Sign at Animal Kingdom
* *`EVRST4`* - Expedition Everest Bridge at Animal Kingdom
* *`EXPEDITIONEVERESTRIDE`* - Expedition Everest Ride (Animal Kingdom)
* `FNTSYBRG` - Magic Kingdom bridge to New Fantasy Land, with castle in background
* `HBFIVEDM` - Hollywood Studios with hat in the background (stock photo) - not sure what the initials stand for; maybe Hollywood Big Five (DM - Disney something?)
* *`ENCHANTEDTALESBLUE`* - Enchanted Tales at Magic Kingdom (Blue side)
* *`ENCHANTEDTALESPURPLE`* - Enchanted Tales at Magic Kingdom (Purple side) {presumed to exist based on fairytale hall blue and purple}
* *`MINETRAIN`* - Mine Train Ride at Magic Kingdom
* `MSATHCLB` - Main Street Athletic Club at Magic Kingdom
* *`MSCINEMA`* - Main Street Cinema
* `MSFIRSTA` - Main Street just after the first loop
* `MSCASEYS` - Main Street Casey's Corner at Magic Kingdom - photo is past most of main street, with none of the shops visible in the photo
* *`MSGAZETT`* - Main Street Gazette
* `MSMKTHOU` - Main Street Magic Kingdom (THOU) - doesn't matter which way the photographer is facing (castle or opposite in background has same code)
* *`OHANA`* - Ohana at Polynesian Resort
* `OSBLIGHT2` - Osbourn Lights at Hollywood Studios - Merry Christmas sign is behind us; photo was taken at the intersection inside the main light area
* `PFTHBLUEA1CHAR` - Princess Fairytale Hall (BLUEA1) Character - Met Anna; This was the left side, I think (as you wait in line)
* `PFTHBLUEA2CHAR` - Princess Fairytale Hall (BLUEA2) Character - Met Elsa; This was the left side, I think (as you wait in line)
* `PFTHPURPLEB1CHAR` - Princess Fairytale Hall (PURPLEB1) Character - Met Flynn Ryder and Princess Rapunzel; This was the right side, I think
* `PFTHPURPLEB2CHAR` - Princess Cinderella and Prince Charming
* *`ROCKNRCOASTERRIDE`* - Rock'n Roller Coaster Ride at Hollywood Studios
* *`ROVER1`* - Hollywood Studios with hat in background
* `RPWCHARACTER` - Rafiki's Planet Watch Character greeting (with Rafiki)
* `SPACEMOUNTAINA` - Space Mountain Ride (Track A - to your left when you get shuffled to the left or right side - when you are at the ride gate, the car comes from the right and moves to the left)
* `SPACEMOUNTAINB` - Space Mountain Ride (Track B)
* `SBCCALLIOPECHAR` - Magic Kingdom Circus area (not sure about the acronym; best I could come up with is Sleeping Beauty Castle Calliope Character, which makes no sense. SBC is in California, and Calliope is one of the Muses in Hercules.)
* `SBCMARQUEECHAR` - Magic Kingdom close to circus area. Again, acronym doesn't make sense. Maybe programmers just reuse old codes rather than generate new ones for specific character meets.
* *`SPLASH`* - Splash Mountain Ride at Magic Kingdom
* *`STUDIOARCH`* - Hollywood Studios with the Arch in background
* *`SUNSET2`* - Hollywood Studios with Tower of Terror in background
* `TEST` - usually used for the bonus/stock photos
* `TOMBRDG1` - Tomorrowland Bridge, with the castle in the background
* *`TOWEROFTERRORARIDE`* - Tower of Terror Ride (Track A) at Hollywood Studios
* *`TOWEROFTERRORBRIDE`* - Tower of Terror Ride (Track B) at Hollywood Studios
* `TREEBACK` - Angle of the Tree of Life, framed by trees closer to the subjects
* `TSHOLIDAY` - just before main street, inside the street loop where the flagpole is (and where the Christmas tree or pumpkin display is set up during the holiday)
* `TSHOLICON` - same as `TSHOLIDAY`, I think.
* *`VERCHAR1`* - Magic Kingdom walkway by river near castle (character greeting spot)
* `WRLDSHW3` - World Showcase at Epcot - in front of the fountain (by France, I think)
* `WSFRN` - World Showcase France at Epcot
* `WSMEX` - World Showcase Mexico at Epcot

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
