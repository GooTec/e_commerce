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

/* 상세페이지 Tab */
var showTab = "";

function changeTab(showTab) {
	
	var tab1 = document.getElementById('detailTab_1');
	var tab2 = document.getElementById('detailTab_2');
	var tab3 = document.getElementById('detailTab_3');
	
	switch (showTab){
		case '1':
			document.getElementById('detailTab1').style.display = "block";
			document.getElementById('detailTab2').style.display = "none";
			document.getElementById('detailTab3').style.display = "none";
			
			tab1.style.fontWeight = "bold";
			tab1.style.borderBottom = "2px solid #ffca00";
			
			tab2.style.fontWeight = "normal";
			tab2.style.borderBottom = "0";
			
			tab3.style.fontWeight = "normal";
			tab3.style.borderBottom = "0";
			
			break;
			
		case '2':
			document.getElementById('detailTab1').style.display = "none";
			document.getElementById('detailTab2').style.display = "block";
			document.getElementById('detailTab3').style.display = "none";
			
			tab1.style.fontWeight = "normal";
			tab1.style.borderBottom = "0";
			
			tab2.style.fontWeight = "bold";
			tab2.style.borderBottom = "2px solid #ffca00";
			
			tab3.style.fontWeight = "normal";
			tab3.style.borderBottom = "0";
			
			break;
			
		case '3':
			document.getElementById('detailTab1').style.display = "none";
			document.getElementById('detailTab2').style.display = "none";
			document.getElementById('detailTab3').style.display = "block";
			
			tab1.style.fontWeight = "normal";
			tab1.style.borderBottom = "0";
			
			tab2.style.fontWeight = "normal";
			tab2.style.borderBottom = "0";
			
			tab3.style.fontWeight = "bold";
			tab3.style.borderBottom = "2px solid #ffca00";
			
			break;
	}
	
	document.getElementById(showTab).style.display = "block";
}