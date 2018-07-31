// JavaScript Document

/* Banner Start */
var BannerImage = 1;
var BannerImageMAX = 2;

function banner_click_left() {
	if(BannerImage>1){
	
		BannerImage -= 1;
		var fileName = "banner"+BannerImage+".png";
		
		var banner_wrap = document.getElementById("banner_wrap");
		banner_wrap.style.backgroundImage = "url("+fileName+")";
	}
}

function banner_click_right() {
	if(BannerImage<BannerImageMAX){
	
		BannerImage += 1;
		var fileName = "banner"+BannerImage+".png";
		
		var banner_wrap = document.getElementById("banner_wrap");
		banner_wrap.style.backgroundImage = "url("+fileName+")";
	}
}
/* Banner End */