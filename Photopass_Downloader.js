// ==UserScript==
// @name        Photopass Downloader
// @namespace   https://www.schrauger.com
// @description Download all your photopass photos (in medium resolution)
// @include     https://mydisneyphotopass.disney.go.com/mymedia/
// @include     https://mydisneyphotopass.disney.go.com/mymedia
// @include     https://mydisneyphotopass.disney.go.com/mymedia/*
// @version     1.0
// @require     //ajax.googleapis.com/ajax/libs/jquery/1.5.1/jquery.min.js
// @grant       none
// ==/UserScript==
jQuery(document).ready(function(){
	jQuery("div.mosaicHeaderRightTable").after("<a href='#' class='downloader' title='Warning - Clicking this link will open ALL of your photos in individual windows'>Open All</a>");
	jQuery("a.downloader").click(function(){
		jQuery.getJSON("/slideshow/index/getMediumres", function(data){
			jQuery.each( data, function(key,val){
				window.open(val);
			});
		});
	});
});