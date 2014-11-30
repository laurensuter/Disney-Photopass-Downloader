// ==UserScript==
// @name        Photopass Downloader
// @namespace   https://www.schrauger.com
// @description Download all your photopass photos (in medium resolution)
// @include     https://mydisneyphotopass.disney.go.com/mymedia/
// @include     https://mydisneyphotopass.disney.go.com/mymedia
// @include     https://mydisneyphotopass.disney.go.com/mymedia/*
// @version     1.23
// @require     https://ajax.googleapis.com/ajax/libs/jquery/1.5.1/jquery.min.js
// @grant       none
// @downloadURL https://raw.githubusercontent.com/schrauger/Disney-Photopass-Downloader/master/greasemonkey/Photopass_Downloader.user.js
// @updateURL   https://raw.githubusercontent.com/schrauger/Disney-Photopass-Downloader/master/greasemonkey/Photopass_Downloader.user.js
// ==/UserScript==
jQuery(document).ready(function () {
    var max_photos = +jQuery('#totalMediaCount').text(); // number of photos in your account
    jQuery("div.mosaicHeaderRightTable").after("<div style='position: relative; z-index: 100;'><a href='#' class='download_all' title='Warning - Clicking this link will open ALL of your photos in individual windows'>Open All</a> | " +
                                                   "<a href='#' class='download_range' title='Clicking this link will open a specified range of your photos in individual windows'>Open </a> " +
                                                   "<input size='2' name='photopassdownload_start' value='1' min='1' max='" + max_photos + "' type='number' style='width:3em;' step='20'/> through <label name='photopassdownload_end'>20</label></div>");
    // add links to download all or some photos
    
    jQuery("a.download_all").click(function () {
        // when 'download all' is clicked, get medium res photos and open each in a new tab
        jQuery.getJSON("/slideshow/index/getMediumres", function (data) {
            jQuery.each(data, function (key, val) {
                window.open(val);
            });
        });
    });
    jQuery("input[name='photopassdownload_start']").change(function () {
        // when start range is changed, calculate the end range
        var start = +jQuery("input[name='photopassdownload_start']").val();
        var end = start + 19;
        if (end > max_photos) {
            // make sure the end range isn't greater than the photos that are actually in the account
            end = max_photos;
        }
        jQuery("label[name='photopassdownload_end']").text(end);
    });
    jQuery("a.download_range").click(function () {
        // when 'download some' is clicked, get all photos, but only open the range specified in new tabs
        jQuery.getJSON("/slideshow/index/getMediumres", function (data) {
            var my_index = 1; // 1-based, since user-specified range begins at 1, not 0
            jQuery.each(data, function (key, val) {
                if ((my_index >= +(jQuery("input[name='photopassdownload_start']").val())) && (my_index <= (+jQuery("label[name='photopassdownload_end']").text()))) {
                    // this photo is within the specified range
                    window.open(val);
                }
                my_index = my_index + 1;
                // keep track of index, because jQuery.each can be finicky about the index number.
            });
        });
    });
});
