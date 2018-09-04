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
}

/* 마이페이지 Tab */
var myTab1 = "";

function mypageFirstChangeTab(myTab1) {
	
	var tab1 = document.getElementById('mypageTab1');
	var tab2 = document.getElementById('mypageTab2');
	
	switch (myTab1){
		/* 주문관리 */
		case '1':
			tab1.classList.add("mypageSelected");tab1.classList.remove("mypageUNSelected");
			tab2.classList.add("mypageUNSelected");tab2.classList.remove("mypageSelected");
			
			document.getElementById('mypageTab_1').style.display = "block";
			document.getElementById('mypageTab_2').style.display = "none";
			
			break;
			
		/* 개인정보관 */
		case '2':
			tab1.classList.add("mypageUNSelected");tab1.classList.remove("mypageSelected");
			tab2.classList.add("mypageSelected");tab2.classList.remove("mypageUNSelected");
			
			document.getElementById('mypageTab_1').style.display = "none";
			document.getElementById('mypageTab_2').style.display = "block";
			
			break;
	}
}

var myTab2 = "";

function mypageSecondChangeTab(myTab2) {
	
	var tab1 = document.getElementById('mypageTab2_1');
	var tab2 = document.getElementById('mypageTab2_2');
	var tab3 = document.getElementById('mypageTab2_3');
	
	switch (myTab2){
		/* 회원정보수정 */
		case '1':
			tab1.classList.add("mypageSelected2");tab1.classList.remove("mypageUNSelected2");
			tab2.classList.add("mypageUNSelected2");tab2.classList.remove("mypageSelected2");
			tab3.classList.add("mypageUNSelected2");tab3.classList.remove("mypageSelected2");
			
			document.getElementById('mypageTab_2_1').style.display = "block";
			document.getElementById('mypageTab_2_2').style.display = "none";
			document.getElementById('mypageTab_2_3').style.display = "none";
			
			break;
			
		/* 환불계좌관리 */
		case '2':
			tab1.classList.add("mypageUNSelected2");tab1.classList.remove("mypageSelected2");
			tab2.classList.add("mypageSelected2");tab2.classList.remove("mypageUNSelected2");
			tab3.classList.add("mypageUNSelected2");tab3.classList.remove("mypageSelected2");
			
			document.getElementById('mypageTab_2_1').style.display = "none";
			document.getElementById('mypageTab_2_2').style.display = "block";
			document.getElementById('mypageTab_2_3').style.display = "none";
			
			break;
			
		/* 회원탈퇴 */
		case '3':
			tab1.classList.add("mypageUNSelected2");tab1.classList.remove("mypageSelected2");
			tab2.classList.add("mypageUNSelected2");tab2.classList.remove("mypageSelected2");
			tab3.classList.add("mypageSelected2");tab3.classList.remove("mypageUNSelected2");
			
			document.getElementById('mypageTab_2_1').style.display = "none";
			document.getElementById('mypageTab_2_2').style.display = "none";
			document.getElementById('mypageTab_2_3').style.display = "block";
			
			break;
	}
}

// *** 수정 필요 *** //
var n = 0;
var tmpId = "";

function numSet(n, tmpId){
	// 우선은 눈에 보이는 것만 바뀌도록 되어 있습니다.
	var val = document.getElementById(tmpId).value;
	var sum = Number(n) + Number(val);
	
	if(sum < 1){
		alert("1보다 작은 값은 입력할 수 없습니다.\n삭제 버튼을 눌러주세요.");
	}else{
		document.getElementById(tmpId).value = sum;
	}
	/*
	
	1. 장바구니 각 상품별로 ID 받아와서 값 바뀔 수 있도록
	2. 리스트에 합계와 리스트 아래에 있는 총합 수정되게 해야함.
	
	*/
}