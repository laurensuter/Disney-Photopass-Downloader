// ==UserScript==
// @name        Photopass Downloader
// @namespace   https://www.schrauger.com
// @description Download all your photopass photos (in medium resolution)
// @include     https://mydisneyphotopass.disney.go.com/mymedia/
// @include     https://mydisneyphotopass.disney.go.com/mymedia
// @include     https://mydisneyphotopass.disney.go.com/mymedia/*
// @version     2.1.3
// @require     https://ajax.googleapis.com/ajax/libs/jquery/1.5.1/jquery.min.js
// @grant       none
// @downloadURL https://raw.githubusercontent.com/schrauger/Disney-Photopass-Downloader/master/greasemonkey/Photopass_Downloader.user.js
// @updateURL   https://raw.githubusercontent.com/schrauger/Disney-Photopass-Downloader/master/greasemonkey/Photopass_Downloader.user.js
// ==/UserScript==
/*jslint browser: true*/
/*global jQuery*/
jQuery(document).ready(function () {
    "use strict";
    var str_space = ' '; // non-breaking space character.
    var max_photos = +jQuery('#totalMediaCount').text(); // number of photos in your account (the '+' character forces it to be a number instead of a string)
    var medium_url_list; // contains key->value of unique_id->url
    var photo_unique_ids = []; // contains 0-based count array with value of unique_id
    jQuery.getJSON("/slideshow/index/getMediumres", function (data) {
        // contains the urls for medium resolution, as well as the unique key
        medium_url_list = data;
        jQuery.each(medium_url_list, function (index, value) {
            photo_unique_ids.push(index); // an array of just the unique ids. This way, for ranges, we don't have to loop and count multiple times; just use the index of this array.
        });
    });
    var photo_detail_list; // contains raw object data with photo details
    var photo_detail_list_array = []; // contains key->value of unique_id->json_object
    jQuery.getJSON("/disney/ajax/getGuestMedia", function (data) {
        // contains the time and other information, as well as the unique key
        photo_detail_list = data.guestMedia;
        jQuery.each(photo_detail_list, function (index, value) {
            photo_detail_list_array[value.guestMediaId] = value; // array index by unique id for easy lookup later
        });
    });

    /**
     * A very simple date formatter. Takes the input javascript Date object and returns a string.
     * @param date
     */
    function format_date(date) {
        var str_return = '';
        str_return += date.getFullYear();
        str_return += '-' + date.getMonth();
        str_return += '-' + date.getDate();
        str_return += str_space + date.getHours(); // even when url encoded, disney's api will stop after a space, so we can't have any real spaces in our filename. use 'fake' non-breaking-spaces instead
        str_return += '_' + date.getMinutes();
        str_return += '_' + date.getSeconds();
        return encodeURIComponent(str_return);
    }

    /**
     * Downloads the photo based on the unique id as listed in both JSON requests.
     * @param unique_id
     */
    function download_photo(unique_id) {
        var url = medium_url_list[unique_id];
        var date_created = photo_detail_list_array[unique_id].takenDate;
        date_created = new Date(Date.parse(date_created)); // javascript can automatically parse the date given by Disney
        var media_type = photo_detail_list_array[unique_id].mediaType;
        var file_extension = '.jpg'; // default to jpg
        var date_created_string = format_date(date_created);
        var location = photo_detail_list_array[unique_id].venue;

        if (media_type === "ANIMATED MAGIC") {
            file_extension = '.mp4'; // movies are called "ANIMATED MAGIC" and are mp4 files.
        }
        var filename = date_created_string + str_space + location + str_space + unique_id + file_extension; // the full filename
        var full_url = url + '?&fname=' + filename; // this works whether '?' is defined or not (url doesn't care that multiple questions marks exist)
        window.open(full_url); // finally, we download the photo!
    }

    /**
     * Opens some or all of the available photos in new tabs to download them.
     * @param start Start range inclusive (0-based)
     * @param stop Stop range inclusive (if this is greater than available, it will stop at max available)
     */
    function download(start, stop) {
        if (start < max_photos) {
            var i;
            for (i = start; i <= stop && i < max_photos; i++) {
                if (photo_unique_ids[i]) {
                    download_photo(photo_unique_ids[i]);
                }
            }
        }
    }

    jQuery("div.myMediaButtonContainer:last").after(" " +
            '<div class="myMediaButtonContainer"><a class="button_secondary download_all" tabindex="-1" href="#" title="Warning - Clicking this link will open ALL of your photos in individual windows. Be prepared for ' + max_photos + ' download popups."><span tabindex="0" class="button150">Download All</span></a></div>' +
            '<div class="myMediaButtonContainer"><a class="button_secondary download_range" tabindex="-1" href="#" title="Clicking this link will download a specified range of your photos in individual windows."><span tabindex="0" class="button150">Download Range</span></a></div>' +
            '<div class="myMediaButtonContainer"><input size="2" name="photopassdownload_start" value="1" min="1" max="' + max_photos + '" type="number" style="width:3em;" step="20"/> through <label name="photopassdownload_end">' + ((max_photos < 20) ? max_photos : 20) + '</label></div>');
    // add links to download all or some photos

    jQuery("input[name='photopassdownload_start']").change(function () {
        // when start range is changed, calculate the end range
        var start = +jQuery("input[name='photopassdownload_start']").val();
        var end = start + 19;
        if (end > max_photos) {
            // make sure the end range isn't greater than the photos that are actually in the account
            end = max_photos;
        }
        jQuery("label[name='photopassdownload_end']").text(end);
        //jQuery("a.download_range span").text('Download ' + start + '-' + end);
    });

    jQuery("a.download_all").click(function () {
        // when 'download all' is clicked, get medium res photos and open each in a new tab
        download(0, max_photos - 1);
    });
    jQuery("a.download_range").click(function () {
        // when 'download some' is clicked, get all photos, but only open the range specified in new tabs
        download(((+jQuery("input[name='photopassdownload_start']").val()) - 1), ((+jQuery("label[name='photopassdownload_end']").text()) - 1));
    });
});
