/**
 * 자바스크립트 공통함수
 *
 * 주의: 아래의 모든 메소드는 입력폼의 필드이름(myform.myfield)을
 *       파라미터로 받는다. 필드의 값(myform.myfield.value)이 아님을
 *       유념할 것.
 *
 */


/**
 * 입력값이 NULL인지 체크
 */
function isNull(input) {
    if (input.value == null || input.value == "") {
        return true;
    }
    return false;
}

/**
 * 입력값에 스페이스 이외의 의미있는 값이 있는지 체크
 * ex) if (isEmpty(form.keyword)) {
 *         alert("검색조건을 입력하세요.");
 *     }
 */
function isEmpty(input) {
    if (input.value == null || input.value.replace(/ /gi,"") == "") {
        return true;
    }
    return false;
}

/**
 * 입력값에 특정 문자(chars)가 있는지 체크
 * 특정 문자를 허용하지 않으려 할 때 사용
 * ex) if (containsChars(form.name,"!,*&^%$#@~;")) {
 *         alert("이름 필드에는 특수 문자를 사용할 수 없습니다.");
 *     }
 */
function containsChars(input,chars) {
    for (var inx = 0; inx < input.value.length; inx++) {
       if (chars.indexOf(input.value.charAt(inx)) != -1)
           return true;
    }
    return false;
}

/**
 * 입력값이 특정 문자(chars)만으로 되어있는지 체크
 * 특정 문자만 허용하려 할 때 사용
 * ex) if (!containsCharsOnly(form.blood,"ABO")) {
 *         alert("혈액형 필드에는 A,B,O 문자만 사용할 수 있습니다.");
 *     }
 */
function containsCharsOnly(input,chars) {
    for (var inx = 0; inx < input.value.length; inx++) {
       if (chars.indexOf(input.value.charAt(inx)) == -1)
           return false;
    }
    return true;
}

/**
 * 입력값이 알파벳인지 체크
 * 아래 isAlphabet() 부터 isNumComma()까지의 메소드가
 * 자주 쓰이는 경우에는 var chars 변수를
 * global 변수로 선언하고 사용하도록 한다.
 * ex) var uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
 *     var lowercase = "abcdefghijklmnopqrstuvwxyz";
 *     var number    = "0123456789";
 *     function isAlphaNum(input) {
 *         var chars = uppercase + lowercase + number;
 *         return containsCharsOnly(input,chars);
 *     }
 */
function isAlphabet(input) {
    var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    return containsCharsOnly(input,chars);
}


/**
 * 입력값이 알파벳 대문자인지 체크
 */
function isUpperCase(input) {
    var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    return containsCharsOnly(input,chars);
}

/**
 * 입력값이 알파벳 소문자인지 체크
 */
function isLowerCase(input) {
    var chars = "abcdefghijklmnopqrstuvwxyz";
    return containsCharsOnly(input,chars);
}

/**
 * 입력값에 숫자만 있는지 체크
 */
function isNumber(input) {
    var chars = "0123456789";
    return containsCharsOnly(input,chars);
}

/**
 * 입력값이 알파벳,숫자로 되어있는지 체크
 */
function isAlphaNum(input) {
    var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    return containsCharsOnly(input,chars);
}

/**
 * 입력값이 숫자,대시(-)로 되어있는지 체크
 */
function isNumDash(input) {
    var chars = "-0123456789";
    return containsCharsOnly(input,chars);
}

/**
 * 입력값이 숫자,콤마(,)로 되어있는지 체크
 */
function isNumComma(input) {
    var chars = ",0123456789";
    return containsCharsOnly(input,chars);
}

/**
 * 입력값이 사용자가 정의한 포맷 형식인지 체크
 * 자세한 format 형식은 자바스크립트의 'regular expression'을 참조
 */
function isValidFormat(input,format) {
    if (input.value.search(format) != -1) {
        return true; //올바른 포맷 형식
    }
    return false;
}

/**
 * 입력값이 이메일 형식인지 체크
 * ex) if (!isValidEmail(form.email)) {
 *         alert("올바른 이메일 주소가 아닙니다.");
 *     }
 */
function isValidEmail(input) {
//    var format = /^(\S+)@(\S+)\.([A-Za-z]+)$/;
    var format = /^((\w|[\-\.])+)@((\w|[\-\.])+)\.([A-Za-z]+)$/;
    return isValidFormat(input,format);
}

/**
 * 입력값이 전화번호 형식(숫자-숫자-숫자)인지 체크
 */
function isValidPhone(input) {
    var format = /^(\d+)-(\d+)-(\d+)$/;
    return isValidFormat(input,format);
}

/**
 * 입력값이 시간(0~23의 숫자)인지 체크
 */
function isValidHour(input) {
	return (input.value >= 0 && input.value <= 23);
}

/**
 * 입력값이 분(0~59의 숫자)인지 체크
 */
function isValidMinute(input) {
	return (input.value >= 0 && input.value <= 59);
}

/**
 * 입력값이 전화번호 형식(숫자-숫자-숫자)인지 체크
 */
function isValidPhone(input) {
    var format = /^(\d+)-(\d+)-(\d+)$/;
    return isValidFormat(input,format);
}

/**
 * 입력값의 캐릭터 길이를 리턴
 */
function getLength(input) {
    return input.value.length;
}

/**
 * 입력값의 바이트 길이를 리턴
 * ex) if (getByteLength(form.title) > 100) {
 *         alert("제목은 한글 50자(영문 100자) 이상 입력할 수 없습니다.");
 *     }
 * Author : Wonyoung Lee
 */
function getByteLength(input) {
    var byteLength = 0;
    for (var inx = 0; inx < input.value.length; inx++) {
        var oneChar = escape(input.value.charAt(inx));
        if ( oneChar.length == 1 ) {
            byteLength ++;
        } else if (oneChar.indexOf("%u") != -1) {
            byteLength += 2;
        } else if (oneChar.indexOf("%") != -1) {
            byteLength += oneChar.length/3;
        }
    }
    return byteLength;
}

/**
 * 입력값에서 콤마를 없앤다.
 */
function removeComma(input) {
    return input.value.replace(/,/gi,"");
}

/**
 * 선택된 라디오버튼이 있는지 체크
 * ex) if (!hasCheckedRadioButton(form.myradio)) {
 *         alert("선택된 라디오버튼이 없습니다.");
 *     }
 */
function hasCheckedRadioButton(input) {
    if (input.length > 1) {
        for (var inx = 0; inx < input.length; inx++) {
            if (input[inx].checked) return true;
        }
    } else {
        if (input.checked) return true;
    }
    return false;
}

/**
 * 선택된 체크박스가 있는지 체크
 */
function hasCheckedCheckBox(input) {
    return hasCheckedRadioButton(input);
}


/*==================================
	function : openModalCenter()
	설명     : 화면중앙에 띄우기.
	예제     : openModalCenter("page.htm",'TITLE','280px','270px','scroll:1; help:0; status:0');
	기타     : width + 10 
	           heignt + 20
 ==================================*/
function openModalCenter(mypage,myname,w,h,features) {
	if(screen.width){
		var winl = (screen.width-w)/2;
		var wint = (screen.height-h)/2;
	}
	else {
		winl = 0;wint =0;
	}
	if (winl < 0) winl = 0;
	if (wint < 0) wint = 0;

	var settings = 'dialogHeight:' + h + ';';
	settings += 'dialogWidth:' + w + ';';
	settings += 'dialogTop:' + wint + 'px;';
	settings += 'dialogLeft:' + winl + 'px;';
	settings += features;

	win = window.showModalDialog (mypage,myname,settings);
	return win;

}

/*==================================
	function : openModal()
	설명     : OpenWindow속성 정의
 ==================================*/
 function openModal(d_url, w, h, etc)
{
	var stat;
	stat = 'dialogWidth:'+w+';dialogHeight:'+h;
	if(etc != ""){
		stat = stat + ";" + etc;
	}
	var Wp = window.showModalDialog (d_url,"_blank",stat);
}

/*==================================
	function : openWinCenter()
	설명     : 화면중앙에 띄우기.
 ==================================*/
function openWinCenter(mypage,myname,w,h,features) {
	if(screen.width){
		var winl = (screen.width-w)/2;
		var wint = (screen.height-h)/2;
	}
	else {
		winl = 0;wint =0;
	}
	if (winl < 0) winl = 0;
	if (wint < 0) wint = 0;

	var settings = 'height=' + h + ',';
	settings += 'width=' + w + ',';
	settings += 'top=' + wint + ',';
	settings += 'left=' + winl + ',';
	settings += features;
	win = window.open(mypage,myname,settings);


	win.window.focus();
	//window.showModalDialog (mypage,myname,settings);

	return win;

}
/*==================================
	function : openWin()
	설명     : OpenWindow속성 정의
 ==================================*/
 function openWin(d_url, w, h, etc)
{
	var stat;
	stat = 'width='+w+',height='+h;
	if(etc != ""){
		stat = stat + "," + etc;
	}
	var Wp = window.open(d_url, "_blank", stat);
	Wp.focus();

}

/*==================================
	function : checkEnter()
	설명     : 입력 Field에서 enter 체크
 ==================================*/
function checkEnter(event)
{
	var theKey;

	theKey = window.event.keyCode ;

	if (theKey == 13)
		return true ;
	return false;
}

/*
*/

function changeSelectIndex(objSelect, aKey)
{
	for(i=0; i< objSelect.length;i++) {
		if (objSelect.options[i].value == aKey) {
			objSelect.selectedIndex = i;
			break;
		}
	}
}

/*
 * len 만큼 0 의 갯수를 맞춰준다
 * figure(8,2) => 08
 */
function figure(aValue, len)
{
	temp = "";
	aValue = aValue+"";

	if(aValue.length < len) {
		for(i=0; i < len - aValue.length; i++) {
			temp = temp + "0";
		}
		return temp + aValue;
	}
	return aValue;
}

// message popup (alert 대신 사용)
function openMessagePopup(flag, obj, title, message){

    //flag :
    // SA - 서비스 디자인 + alert 기능
    // SC - 서비스 디자인 + confirm 기능
    // AA - 어드민 디자인 + alert 기능
    // AC - 어드민 디자인 + confirm 기능

    if(flag=='SA'){

        return showMessage(message,'S');

    }else if(flag=='SC'){

        return showMessage(message,'S','CONFIRM');

    }else if(flag=='AA'){

        return showMessage(message,'A');

    }else if(flag=='AC'){

        return showMessage(message,'A','CONFIRM');

    }



}

function openModalMessage(flag, obj, title, message){

    //flag :
    // SA - 서비스 디자인 + alert 기능
    // SC - 서비스 디자인 + confirm 기능
    // AA - 어드민 디자인 + alert 기능
    // AC - 어드민 디자인 + confirm 기능

	obj='';

	var rst = true;

    if(flag=='SA'){
        var url = '/view/common/Message.jsp?message=' + message + '&title=' + title + '&object=' + obj + '&flag=A';
        rst     = openModalCenter(url,'message','265px','160px','scroll:0; help:0; status:0');

    }else if(flag=='SC'){
        var url = '/view/common/Message.jsp?message=' + message + '&title=' + title + '&object=' + obj + '&flag=C';
        rst     = openModalCenter(url,'message','265px','160px','scroll:0; help:0; status:0');

    }else if(flag=='AA'){
        var url = '/view/common/MessageAdmin.jsp?message=' + message + '&title=' + title + '&object=' + obj + '&flag=A';
        rst     = openModalCenter(url,'message','290px','115px','scroll:0; help:0; status:0');

    }else if(flag=='AC'){
        var url = '/view/common/MessageAdmin.jsp?message=' + message + '&title=' + title + '&object=' + obj + '&flag=C';
        rst     = openModalCenter(url,'message','290px','115px','scroll:0; help:0; status:0');
    }

    return rst;

}



//--------------------------


/**
 * open message page
 *
 * @param		message		message page에 뿌려줄 메세지
 * @param		optional	Confirm message flag
 * @since		1.0
 */
function showMessage (message) {

    if (arguments[1] == "A"){

        if (arguments[2] == null)
            return openModalPopup("/common/MessageAdmin.jsp", "305", "140", message);
        else
            return openModalPopup("/common/MessageAdmin.jsp", "305", "140", message, arguments[2]);

	} else {

        if (arguments[2] == null)
            return openModalPopup("/common/Message.jsp", "265", "160", message);
        else
            return openModalPopup("/common/Message.jsp", "265", "160", message, arguments[2]);
    }

}


/**
 * open modal popup
 *
 * @param		sURL		url
 * @param		sWidth		window width(optional)
 * @param		sHeight		window height(optional)
 * @param		vArguments	passed Arguments(optional)
 * @return	window object
 * @since		1.0
 *
 * ex) openModalPopup('popup_test1.htm')
 *     openModalPopup('popup_test1.htm','600','400','aaa')
 *     openModalPopup('popup_test1.htm','600','400','aaa','bbb','ccc')
 */
function openModalPopup (sURL) {
	var sWidth, sHeight;
	var sFeatures;
	var oWindow;
	var vArguments = new Array();

	sHeight	= "500px";
	sWidth	= "500px";

	if (arguments[1] != null && arguments[1] != "") sWidth = arguments[1] + "px" ;
	if (arguments[2] != null && arguments[2] != "") sHeight = arguments[2] + "px" ;

	vArguments[0] = window;

	// 팝업호출시 파라미터는 [1]번째부터
	for (var i=3; i<arguments.length; i++) {
		vArguments[i-2] = arguments[i] ;
	}

	sFeatures =  "dialogWidth:" + sWidth + "; dialogHeight:" + sHeight ;
	sFeatures += ";center:yes;resizable:no;scroll:no;status:no";

	oWindow = window.showModalDialog(sURL, vArguments, sFeatures);

	return oWindow;
}


	function isNumeric(input) {
		var chars = "0123456789";

		for (var inx = 0; inx < input.length; inx++) {
		   if (chars.indexOf(input.charAt(inx)) == -1)
			   return false;
		}
		return true;
	}

	/**
	 * openCalendar
	 *
	 * @param   strName -> 폼.객체이름 (날짜를 가지고 있는객체 필드)
	 * @return	
	 * @since		1.0
	 *
	 * ex) openCalendar('form1.sdate')
	 */
	function openCalendar(strName){

		var strURL = "";
		strName = "document." + strName;
		var objInput = eval(strName);

		var v1 = new String(objInput.value);

		if(v1==''){
		}else if(v1.indexOf("-") > 0){

			var d1 = v1.substring(0, v1.indexOf("-"));
			v1 = v1.substring(v1.indexOf("-")+1, v1.length);

			if(v1.indexOf("-") <= 0){
				alert("사용법이 틀렸습니다. \n\n사용법 : \'yyyy-mm-dd\' 혹은 \'\'"); 
				objInput.focus();
				return;
			}	

			var d2 = v1.substring(0, v1.indexOf("-"));
			v1 = v1.substring(v1.indexOf("-")+1, v1.length);

			var d3 = v1.substring(0, v1.length);

			/*if(d1 < 1956 || d1 > 2088){
				alert("유효한 년도가 아닙니다. \n\n 1956년에서 2088년 사이의 년도을 넣으세요.");
				objInput.focus();
				return;
			}else*/ if(d2 > 12 || d2 < 1){
				alert("월의 값이 잘 못 됐습니다. \n\n 1~12 사이의 값을 넣으세요.");
				objInput.focus();
				return;
			}else if(d3 > 31 || d3 < 1){
				alert("일의 값이 잘 못 됐습니다. \n\n 확인해 주세요");
				objInput.focus();
				return;
			}else if(isNumeric(d1) && isNumeric(d2) && isNumeric(d3)){
			}else{
				alert("숫자가 아닌 다른 값이 들어갔습니다. \n\n 사용법 : \'yyyy-mm-dd\' 혹은 \'\'");
				objInput.focus();
				return;
			}

		}else{
			alert("사용법이 틀렸습니다. \n\n 사용법 : \'yyyy-mm-dd\' 혹은 \'\'");
			objInput.focus();
			return;
		}

		strURL = "/common/calendar.jsp?date=" + objInput.value + "&field=" + strName;

		win = window.open(strURL, "Calendar", "alwaysRaised=yes, dependent=no, resizable=no, scrollbars=no, width=255, height=275 top=246, left=384");
	}

function MM_swapImgRestore() { //v3.0
  var i,x,a=document.MM_sr; for(i=0;a&&i<a.length&&(x=a[i])&&x.oSrc;i++) x.src=x.oSrc;
}

function MM_preloadImages() { //v3.0
  var d=document; if(d.images){ if(!d.MM_p) d.MM_p=new Array();
    var i,j=d.MM_p.length,a=MM_preloadImages.arguments; for(i=0; i<a.length; i++)
    if (a[i].indexOf("#")!=0){ d.MM_p[j]=new Image; d.MM_p[j++].src=a[i];}}
}

function MM_findObj(n, d) { //v4.01
  var p,i,x;  if(!d) d=document; if((p=n.indexOf("?"))>0&&parent.frames.length) {
    d=parent.frames[n.substring(p+1)].document; n=n.substring(0,p);}
  if(!(x=d[n])&&d.all) x=d.all[n]; for (i=0;!x&&i<d.forms.length;i++) x=d.forms[i][n];
  for(i=0;!x&&d.layers&&i<d.layers.length;i++) x=MM_findObj(n,d.layers[i].document);
  if(!x && d.getElementById) x=d.getElementById(n); return x;
}

function MM_swapImage() { //v3.0
  var i,j=0,x,a=MM_swapImage.arguments; document.MM_sr=new Array; for(i=0;i<(a.length-2);i+=3)
   if ((x=MM_findObj(a[i]))!=null){document.MM_sr[j++]=x; if(!x.oSrc) x.oSrc=x.src; x.src=a[i+2];}
}

function reloadPage(){
	document.location.reload();
}

function openAdmConfirm(titleID, messageID)
{
	var rslt = window.showModalDialog("common/AdmConfirmPopUI.jsp?titleID="+titleID+"&messageID="+messageID, "", "dialogWidth:300px; dialogHeight:200px; scroll:0; help:0; status:0; center:1;");
	return rslt;
}

function openAdmConfirmLarge(titleID, messageID)
{
	var rslt = window.showModalDialog("common/AdmConfirmPopUI.jsp?titleID="+titleID+"&messageID="+messageID, "", "dialogWidth:400px; dialogHeight:300px; scroll:0; help:0; status:0; center:1;");
	return rslt;
}

function openAdmAlert(titleID, messageID)
{	
	var rslt = window.showModalDialog("common/AdmAlertPopUI.jsp?titleID="+titleID+"&messageID="+messageID, "", "dialogWidth:300px; dialogHeight:200px; scroll:0; help:0; status:0; center:1;");
	return rslt;
}

function openAdmAlertMsg(message)
{
	var rslt = window.showModalDialog("common/AdmAlertPopUI.jsp?message="+message, "", "dialogWidth:300px; dialogHeight:200px; scroll:0; help:0; status:0; center:1;");
	return rslt;
}

function checkJumin(val1, val2)
{
	var tmp1,tmp2
	var t1, t2, t3, t4, t5, t6, t7
	tmp1 = val1.substring(2,4);
	tmp2 = val1.substring(4);

	if ((tmp1 < "01") || (tmp1 > "12")) return false;
	if ((tmp2 < "01") || (tmp2 > "31")) return false;
	t1 = val1.substring(0,1);
	t2 = val1.substring(1,2);
	t3 = val1.substring(2,3);
	t4 = val1.substring(3,4);
	t5 = val1.substring(4,5);
	t6 = val1.substring(5,6);
	t11 = val2.substring(0,1);
	t12 = val2.substring(1,2);
	t13 = val2.substring(2,3);
	t14 = val2.substring(3,4);
	t15 = val2.substring(4,5);
	t16 = val2.substring(5,6);
	t17 = val2.substring(6,7);

	var tot = t1*2 + t2*3 + t3*4 + t4*5 + t5*6 + t6*7;
	tot += t11*8 + t12*9 + t13*2 + t14*3 + t15*4 + t16*5 ;

	var result = tot % 11;
	result = (11 - result) % 10;
	if (result != t17) return false;
	return true;
}

/**
 * openCalendar
 *
 * @param   strName1 -> 폼.객체이름 (넘겨받을 객체 이름1)
 * @param   strName2 -> 폼.객체이름 (넘겨받을 객체 이름1)
 * @return	
 * @since		1.0
 *
 * ex) openCalendar('form1.sdate')
 */
function openZipcd(strName1, strName2, strName3){

	var strURL = "common/zipcode_search.jsp?field1=" + strName1 + "&field2=" + strName2 + "&field3=" + strName3;

	openWinCenter(strURL, "Zip_Code_Popup", "450", "350", "alwaysRaised=yes, dependent=no, resizable=no, scrollbars=yes, ");
}


function showtip(text) { /* 툴팁의 내용을 text라는 매개변수로 받아... */
	tooltip.innerText=text; /* innerText에 대입해줍니다. */
	tooltip.style.display="inline";
}

function hidetip() {
	
     tooltip.style.display="none";
}

function movetip() {

     tooltip.style.pixelTop = event.y+document.body.scrollTop; 
     tooltip.style.pixelLeft = event.x+document.body.scrollLeft+10;
	/* event.x는 이벤트가 발생했을때 마우스의 x 좌표를 값으로 가지고 있습니다. */
	/* event.y는 이벤트가 발생했을때 마우스의 y 좌표를 값으로 가지고 있습니다.
 또, document.body.scrollTop과 document.body.scrollLeft는 현재 해당 프레임의 문서가 스크롤된 정도를 나타냅니다.*/
}

//document.onmousemove=movetip;


/**
 * 사업자 등록번호 체크 
 */ 
function check_cn(Num1, Num2, Num3) {
	var no1=Num1;
	var no2=Num2;
	var no3=Num3;

	// 사업자번호 체크 형식
	var strCorpNum = no1+no2+no3	// 사업자번호 10자리

	return check_on2(strCorpNum);

}

function check_on2(strCorpNum){

    var chkRule = "137137135";

    if(strCorpNum.length!=10){
		return false;
	}
	var step1, step2, step3, step4, step5, step6, step7;

	step1=0;		// 초기화

	for (i=0; i<7; i++) {
		step1 = step1 + (strCorpNum.substring(i, i+1) * chkRule.substring(i, i+1));
	}

	step2=step1 % 10;
	step3=(strCorpNum.substring(7, 8) * chkRule.substring(7, 8)) % 10;
	step4=strCorpNum.substring(8, 9) * chkRule.substring(8, 9);
	step5=Math.round(step4 / 10 - 0.5);
	step6=step4 - (step5 * 10);
	step7=(10 - ((step2 + step3 + step5 + step6) % 10)) % 10;
	// 결과 비교 판단
	if (strCorpNum.substring(9, 10) != step7) {
		return false;
	}
	return true;
}


function trim(str)
{
	return lTrim(rTrim(str));
}

function lTrim(str)
{
	for (var i = 0; i < str.length; i++) {
		if (str.charAt(i) != ' ') break;
	}
	return str.substring(i, str.length);
}

function rTrim(str)
{
	for (var i = str.length - 1; i >= 0; i--) {
		if (str.charAt(i) != ' ') break;
	}
	return str.substring(0, i + 1);
}

// 주민등록번호체크() - 로그인 폼 체크시 사용
function residenceNoChk2(resNoObj1, resNoObj2) {
    var str_f_num = resNoObj1.value;
    var str_l_num = resNoObj2.value;

    var i3 = 0;    

    for (var i = 0; i < str_f_num.length; i++) {
        var ch1 = str_f_num.substring(i, i + 1);
        if (ch1 < '0' || ch1 > '9') { i3 = i3 + 1; }
    }

    if ((str_f_num == '') || (i3 != 0)) {
        alert('주민등록번호가 잘못입력되었습니다.1'); 
		resNoObj1.value = '';
        resNoObj2.value = '';
		resNoObj1.focus();
        return false;
    }

    var i4 = 0;
    for (var i = 0; i < str_l_num.length; i++) {
        var ch1 = str_l_num.substring(i, i + 1);
        if (ch1 < '0' || ch1 > '9') { i4 = i4 + 1; }
    }
    if ((str_l_num == '') || ( i4 != 0 )) {
        alert('주민등록번호가 잘못입력되었습니다.2');
		resNoObj1.value = '';
        resNoObj2.value = '';
		resNoObj2.focus();
        return false;
    }

    if (str_l_num.substring(0, 1) > 2) {
        alert('주민등록번호가 잘못입력되었습니다.3');
		resNoObj1.value = '';
        resNoObj2.value = '';
		resNoObj2.focus();
        return false;
    }

    if ((str_f_num.length > 7)) {
        alert('주민등록번호가 잘못입력되었습니다.4');
		resNoObj1.value = '';
        resNoObj2.value = '';
		resNoObj1.focus();
        return false;
    }

    if ((str_l_num.length > 8)) {
        alert('주민등록번호가 잘못입력되었습니다.5');
        resNoObj1.value = '';
        resNoObj2.value = '';
		resNoObj2.focus();
        return false;
    }

    var f1 = str_f_num.substring(0, 1);
    var f2 = str_f_num.substring(1, 2);
    var f3 = str_f_num.substring(2, 3);
    var f4 = str_f_num.substring(3, 4);
    var f5 = str_f_num.substring(4, 5);
    var f6 = str_f_num.substring(5, 6);
    var hap = f1 * 2 + f2 * 3 + f3 * 4 + f4 * 5 + f5 * 6 + f6 * 7;

    var l1 = str_l_num.substring(0, 1);
    var l2 = str_l_num.substring(1, 2);
    var l3 = str_l_num.substring(2, 3);
    var l4 = str_l_num.substring(3, 4);
    var l5 = str_l_num.substring(4, 5);
    var l6 = str_l_num.substring(5, 6);
    var l7 = str_l_num.substring(6, 7);
    hap = hap + l1 * 8 + l2 * 9 + l3 * 2 + l4 * 3 + l5 * 4 + l6 * 5;
    var rem = hap % 11;
    rem = (11 - rem) % 10;
    if (rem != l7) {
        alert('주민등록번호가 잘못입력되었습니다.6');
        resNoObj1.value = '';
        resNoObj2.value = '';
        resNoObj1.focus();
        return false;
    }
    return true;
} 
// 주민등록번호체크() - 로그인 폼 체크시 사용
function checkJuminNo(resNoObj1, resNoObj2){
	var my=(resNoObj1.value) + (resNoObj2.value);	
	var chk="234567892345";
	var sum=0;
	if(IsInteger(my)){
		 for(i=0; i<=11; i++){
		  sum +=my.charAt(i)*chk.charAt(i);
		 }
		 sum=(11-sum%11)%10;
		 if(parseInt(my.charAt(12))==sum){			
		  return true;
		 }else{
		  alert("주민번호 형식이 잘못되었습니다.");
		  resNoObj1.value = '';
		  resNoObj2.value = '';
		  resNoObj1.focus();
		  return false;
		 } 
	}else{
		alert("주민번호 형식이 잘못되었습니다.");
		resNoObj1.value = '';
        resNoObj2.value = '';
        resNoObj1.focus();
		return false;
	}
	return false;
}

// 주민등록번호체크() - 로그인 폼 체크시 사용
function checkJuminNoTarget(resNoObj1, resNoObj2, strTarget){
	var my=(resNoObj1.value) + (resNoObj2.value);	
	var chk="234567892345";
	var sum=0;
	if(IsInteger(my)){
		 for(i=0; i<=11; i++){
		  sum +=my.charAt(i)*chk.charAt(i);
		 }
		 sum=(11-sum%11)%10;
		 if(parseInt(my.charAt(12))==sum){			
		  return true;
		 }else{
		  alert(strTarget+" 형식이 잘못되었습니다.");
		  resNoObj1.value = '';
		  resNoObj2.value = '';
		  resNoObj1.focus();
		  return false;
		 } 
	}else{
		alert(strTarget+" 형식이 잘못되었습니다.");
		resNoObj1.value = '';
        resNoObj2.value = '';
        resNoObj1.focus();
		return false;
	}
	return false;
}

function IsInteger(st){   
	for (j=0; j<st.length; j++)        
	{
	if (((st.substring(j, j+1) < "0") || (st.substring(j, j+1) > "9"))) 
		return false;        
	}  
	return true ;
}
/*----------------------------------------------------------------------------------------
* 	isAccess(e)
*	example : 
*	if (isAccess(event)) {
*	}
*	return : true | false
*	date : 2008.9.17

*	descript : 
	마우스클릭이나 키보드로 선택된 상태인지 판단

	탭키로 해당 영역에 포커스가 간후 다시 탭으로 넘어갈 경우 onkeypress 이벤트가 발생하여 원하는 이벤트 처리가 안된다.
	마우스나 엔터키가 눌러진 경우 keycode = 1)만 이벤트가 발생하게 처리한다.
	Netscape/Firefox/Opera 의 경우 e.which 1로 체크, Safari 의 경우 window.event 0 으로 체크
	IE의 경우 event.button 이나 keycode 13(엔터키)로 체크
----------------------------------------------------------------------------------------*/
function isAccess(e) {
	
	var keynum;
	var ismouseClick = 1;
	
	if (window.event) {		//IE & Safari
		keynum = e.keyCode;
		
		//Safari의 경우 마우스클릭은 keynum 0 이 넘어옴
		if (event.button == 0 || keynum == 0){
			ismouseClick = 0;
		}		
		
	} else if ( e.which ){		// Netscape/Firefox/Opera
		keynum = e.which;
		
		if (keynum == 1) {
			ismouseClick = 0;
		}		
		
	}
	
	//마우스 클릭이거나 엔터키를 누른경우 true값 반환
	if ( ismouseClick == 0 || keynum == 13 ) {
		return true;
	} else {
		return false;
	}
}

/*----------------------------------------------------------------------------------------
* 	createDateCheck(createDate1, createDate2)
*	return : true | false
*	date : 2008.9.26

*	descript : 
	데이타 시작날짜 종료날짜 체크
----------------------------------------------------------------------------------------*/
function createDateCheck(createDate1, createDate2) {
	
	if (createDate1 > createDate2) {
		return true;
	} else {
		return false;
	}
}

function alertMessage(message){
	alert(message);
	return false;
}


//조회하기
function checkSearchValue(form)
{	
	var searchKey = form.SEARCHKEY.value;
	var searchValue = form.SEARCHVALUE.value;	
	if( searchKey != "" && searchValue == ""){
		alert("검색 조건을 입력하세요");
		form.SEARCHVALUE.focus();
		return false;
	}
	if (containsChars(form.SEARCHVALUE,"~!@#$%^&*()+|`-=\\[]{};:'\",.<>/?")) {
		alert("이름 필드에는 특수 문자를 사용할 수 없습니다.");
		form.SEARCHVALUE.value="";
		form.SEARCHVALUE.focus();
		return false;
	}
	form.page.value = 1;
	return true;
}