/**
 * �ڹٽ�ũ��Ʈ �����Լ�
 *
 * ����: �Ʒ��� ��� �޼ҵ�� �Է����� �ʵ��̸�(myform.myfield)��
 *       �Ķ���ͷ� �޴´�. �ʵ��� ��(myform.myfield.value)�� �ƴ���
 *       ������ ��.
 *
 */


/**
 * �Է°��� NULL���� üũ
 */
function isNull(input) {
    if (input.value == null || input.value == "") {
        return true;
    }
    return false;
}

/**
 * �Է°��� �����̽� �̿��� �ǹ��ִ� ���� �ִ��� üũ
 * ex) if (isEmpty(form.keyword)) {
 *         alert("�˻������� �Է��ϼ���.");
 *     }
 */
function isEmpty(input) {
    if (input.value == null || input.value.replace(/ /gi,"") == "") {
        return true;
    }
    return false;
}

/**
 * �Է°��� Ư�� ����(chars)�� �ִ��� üũ
 * Ư�� ���ڸ� ������� ������ �� �� ���
 * ex) if (containsChars(form.name,"!,*&^%$#@~;")) {
 *         alert("�̸� �ʵ忡�� Ư�� ���ڸ� ����� �� �����ϴ�.");
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
 * �Է°��� Ư�� ����(chars)������ �Ǿ��ִ��� üũ
 * Ư�� ���ڸ� ����Ϸ� �� �� ���
 * ex) if (!containsCharsOnly(form.blood,"ABO")) {
 *         alert("������ �ʵ忡�� A,B,O ���ڸ� ����� �� �ֽ��ϴ�.");
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
 * �Է°��� ���ĺ����� üũ
 * �Ʒ� isAlphabet() ���� isNumComma()������ �޼ҵ尡
 * ���� ���̴� ��쿡�� var chars ������
 * global ������ �����ϰ� ����ϵ��� �Ѵ�.
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
 * �Է°��� ���ĺ� �빮������ üũ
 */
function isUpperCase(input) {
    var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    return containsCharsOnly(input,chars);
}

/**
 * �Է°��� ���ĺ� �ҹ������� üũ
 */
function isLowerCase(input) {
    var chars = "abcdefghijklmnopqrstuvwxyz";
    return containsCharsOnly(input,chars);
}

/**
 * �Է°��� ���ڸ� �ִ��� üũ
 */
function isNumber(input) {
    var chars = "0123456789";
    return containsCharsOnly(input,chars);
}

/**
 * �Է°��� ���ĺ�,���ڷ� �Ǿ��ִ��� üũ
 */
function isAlphaNum(input) {
    var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    return containsCharsOnly(input,chars);
}

/**
 * �Է°��� ����,���(-)�� �Ǿ��ִ��� üũ
 */
function isNumDash(input) {
    var chars = "-0123456789";
    return containsCharsOnly(input,chars);
}

/**
 * �Է°��� ����,�޸�(,)�� �Ǿ��ִ��� üũ
 */
function isNumComma(input) {
    var chars = ",0123456789";
    return containsCharsOnly(input,chars);
}

/**
 * �Է°��� ����ڰ� ������ ���� �������� üũ
 * �ڼ��� format ������ �ڹٽ�ũ��Ʈ�� 'regular expression'�� ����
 */
function isValidFormat(input,format) {
    if (input.value.search(format) != -1) {
        return true; //�ùٸ� ���� ����
    }
    return false;
}

/**
 * �Է°��� �̸��� �������� üũ
 * ex) if (!isValidEmail(form.email)) {
 *         alert("�ùٸ� �̸��� �ּҰ� �ƴմϴ�.");
 *     }
 */
function isValidEmail(input) {
//    var format = /^(\S+)@(\S+)\.([A-Za-z]+)$/;
    var format = /^((\w|[\-\.])+)@((\w|[\-\.])+)\.([A-Za-z]+)$/;
    return isValidFormat(input,format);
}

/**
 * �Է°��� ��ȭ��ȣ ����(����-����-����)���� üũ
 */
function isValidPhone(input) {
    var format = /^(\d+)-(\d+)-(\d+)$/;
    return isValidFormat(input,format);
}

/**
 * �Է°��� �ð�(0~23�� ����)���� üũ
 */
function isValidHour(input) {
	return (input.value >= 0 && input.value <= 23);
}

/**
 * �Է°��� ��(0~59�� ����)���� üũ
 */
function isValidMinute(input) {
	return (input.value >= 0 && input.value <= 59);
}

/**
 * �Է°��� ��ȭ��ȣ ����(����-����-����)���� üũ
 */
function isValidPhone(input) {
    var format = /^(\d+)-(\d+)-(\d+)$/;
    return isValidFormat(input,format);
}

/**
 * �Է°��� ĳ���� ���̸� ����
 */
function getLength(input) {
    return input.value.length;
}

/**
 * �Է°��� ����Ʈ ���̸� ����
 * ex) if (getByteLength(form.title) > 100) {
 *         alert("������ �ѱ� 50��(���� 100��) �̻� �Է��� �� �����ϴ�.");
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
 * �Է°����� �޸��� ���ش�.
 */
function removeComma(input) {
    return input.value.replace(/,/gi,"");
}

/**
 * ���õ� ������ư�� �ִ��� üũ
 * ex) if (!hasCheckedRadioButton(form.myradio)) {
 *         alert("���õ� ������ư�� �����ϴ�.");
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
 * ���õ� üũ�ڽ��� �ִ��� üũ
 */
function hasCheckedCheckBox(input) {
    return hasCheckedRadioButton(input);
}


/*==================================
	function : openModalCenter()
	����     : ȭ���߾ӿ� ����.
	����     : openModalCenter("page.htm",'TITLE','280px','270px','scroll:1; help:0; status:0');
	��Ÿ     : width + 10 
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
	����     : OpenWindow�Ӽ� ����
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
	����     : ȭ���߾ӿ� ����.
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
	����     : OpenWindow�Ӽ� ����
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
	����     : �Է� Field���� enter üũ
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
 * len ��ŭ 0 �� ������ �����ش�
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

// message popup (alert ��� ���)
function openMessagePopup(flag, obj, title, message){

    //flag :
    // SA - ���� ������ + alert ���
    // SC - ���� ������ + confirm ���
    // AA - ���� ������ + alert ���
    // AC - ���� ������ + confirm ���

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
    // SA - ���� ������ + alert ���
    // SC - ���� ������ + confirm ���
    // AA - ���� ������ + alert ���
    // AC - ���� ������ + confirm ���

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
 * @param		message		message page�� �ѷ��� �޼���
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

	// �˾�ȣ��� �Ķ���ʹ� [1]��°����
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
	 * @param   strName -> ��.��ü�̸� (��¥�� ������ �ִ°�ü �ʵ�)
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
				alert("������ Ʋ�Ƚ��ϴ�. \n\n���� : \'yyyy-mm-dd\' Ȥ�� \'\'"); 
				objInput.focus();
				return;
			}	

			var d2 = v1.substring(0, v1.indexOf("-"));
			v1 = v1.substring(v1.indexOf("-")+1, v1.length);

			var d3 = v1.substring(0, v1.length);

			/*if(d1 < 1956 || d1 > 2088){
				alert("��ȿ�� �⵵�� �ƴմϴ�. \n\n 1956�⿡�� 2088�� ������ �⵵�� ��������.");
				objInput.focus();
				return;
			}else*/ if(d2 > 12 || d2 < 1){
				alert("���� ���� �� �� �ƽ��ϴ�. \n\n 1~12 ������ ���� ��������.");
				objInput.focus();
				return;
			}else if(d3 > 31 || d3 < 1){
				alert("���� ���� �� �� �ƽ��ϴ�. \n\n Ȯ���� �ּ���");
				objInput.focus();
				return;
			}else if(isNumeric(d1) && isNumeric(d2) && isNumeric(d3)){
			}else{
				alert("���ڰ� �ƴ� �ٸ� ���� �����ϴ�. \n\n ���� : \'yyyy-mm-dd\' Ȥ�� \'\'");
				objInput.focus();
				return;
			}

		}else{
			alert("������ Ʋ�Ƚ��ϴ�. \n\n ���� : \'yyyy-mm-dd\' Ȥ�� \'\'");
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
 * @param   strName1 -> ��.��ü�̸� (�Ѱܹ��� ��ü �̸�1)
 * @param   strName2 -> ��.��ü�̸� (�Ѱܹ��� ��ü �̸�1)
 * @return	
 * @since		1.0
 *
 * ex) openCalendar('form1.sdate')
 */
function openZipcd(strName1, strName2, strName3){

	var strURL = "common/zipcode_search.jsp?field1=" + strName1 + "&field2=" + strName2 + "&field3=" + strName3;

	openWinCenter(strURL, "Zip_Code_Popup", "450", "350", "alwaysRaised=yes, dependent=no, resizable=no, scrollbars=yes, ");
}


function showtip(text) { /* ������ ������ text��� �Ű������� �޾�... */
	tooltip.innerText=text; /* innerText�� �������ݴϴ�. */
	tooltip.style.display="inline";
}

function hidetip() {
	
     tooltip.style.display="none";
}

function movetip() {

     tooltip.style.pixelTop = event.y+document.body.scrollTop; 
     tooltip.style.pixelLeft = event.x+document.body.scrollLeft+10;
	/* event.x�� �̺�Ʈ�� �߻������� ���콺�� x ��ǥ�� ������ ������ �ֽ��ϴ�. */
	/* event.y�� �̺�Ʈ�� �߻������� ���콺�� y ��ǥ�� ������ ������ �ֽ��ϴ�.
 ��, document.body.scrollTop�� document.body.scrollLeft�� ���� �ش� �������� ������ ��ũ�ѵ� ������ ��Ÿ���ϴ�.*/
}

//document.onmousemove=movetip;


/**
 * ����� ��Ϲ�ȣ üũ 
 */ 
function check_cn(Num1, Num2, Num3) {
	var no1=Num1;
	var no2=Num2;
	var no3=Num3;

	// ����ڹ�ȣ üũ ����
	var strCorpNum = no1+no2+no3	// ����ڹ�ȣ 10�ڸ�

	return check_on2(strCorpNum);

}

function check_on2(strCorpNum){

    var chkRule = "137137135";

    if(strCorpNum.length!=10){
		return false;
	}
	var step1, step2, step3, step4, step5, step6, step7;

	step1=0;		// �ʱ�ȭ

	for (i=0; i<7; i++) {
		step1 = step1 + (strCorpNum.substring(i, i+1) * chkRule.substring(i, i+1));
	}

	step2=step1 % 10;
	step3=(strCorpNum.substring(7, 8) * chkRule.substring(7, 8)) % 10;
	step4=strCorpNum.substring(8, 9) * chkRule.substring(8, 9);
	step5=Math.round(step4 / 10 - 0.5);
	step6=step4 - (step5 * 10);
	step7=(10 - ((step2 + step3 + step5 + step6) % 10)) % 10;
	// ��� �� �Ǵ�
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

// �ֹε�Ϲ�ȣüũ() - �α��� �� üũ�� ���
function residenceNoChk2(resNoObj1, resNoObj2) {
    var str_f_num = resNoObj1.value;
    var str_l_num = resNoObj2.value;

    var i3 = 0;    

    for (var i = 0; i < str_f_num.length; i++) {
        var ch1 = str_f_num.substring(i, i + 1);
        if (ch1 < '0' || ch1 > '9') { i3 = i3 + 1; }
    }

    if ((str_f_num == '') || (i3 != 0)) {
        alert('�ֹε�Ϲ�ȣ�� �߸��ԷµǾ����ϴ�.1'); 
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
        alert('�ֹε�Ϲ�ȣ�� �߸��ԷµǾ����ϴ�.2');
		resNoObj1.value = '';
        resNoObj2.value = '';
		resNoObj2.focus();
        return false;
    }

    if (str_l_num.substring(0, 1) > 2) {
        alert('�ֹε�Ϲ�ȣ�� �߸��ԷµǾ����ϴ�.3');
		resNoObj1.value = '';
        resNoObj2.value = '';
		resNoObj2.focus();
        return false;
    }

    if ((str_f_num.length > 7)) {
        alert('�ֹε�Ϲ�ȣ�� �߸��ԷµǾ����ϴ�.4');
		resNoObj1.value = '';
        resNoObj2.value = '';
		resNoObj1.focus();
        return false;
    }

    if ((str_l_num.length > 8)) {
        alert('�ֹε�Ϲ�ȣ�� �߸��ԷµǾ����ϴ�.5');
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
        alert('�ֹε�Ϲ�ȣ�� �߸��ԷµǾ����ϴ�.6');
        resNoObj1.value = '';
        resNoObj2.value = '';
        resNoObj1.focus();
        return false;
    }
    return true;
} 
// �ֹε�Ϲ�ȣüũ() - �α��� �� üũ�� ���
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
		  alert("�ֹι�ȣ ������ �߸��Ǿ����ϴ�.");
		  resNoObj1.value = '';
		  resNoObj2.value = '';
		  resNoObj1.focus();
		  return false;
		 } 
	}else{
		alert("�ֹι�ȣ ������ �߸��Ǿ����ϴ�.");
		resNoObj1.value = '';
        resNoObj2.value = '';
        resNoObj1.focus();
		return false;
	}
	return false;
}

// �ֹε�Ϲ�ȣüũ() - �α��� �� üũ�� ���
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
		  alert(strTarget+" ������ �߸��Ǿ����ϴ�.");
		  resNoObj1.value = '';
		  resNoObj2.value = '';
		  resNoObj1.focus();
		  return false;
		 } 
	}else{
		alert(strTarget+" ������ �߸��Ǿ����ϴ�.");
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
	���콺Ŭ���̳� Ű����� ���õ� �������� �Ǵ�

	��Ű�� �ش� ������ ��Ŀ���� ���� �ٽ� ������ �Ѿ ��� onkeypress �̺�Ʈ�� �߻��Ͽ� ���ϴ� �̺�Ʈ ó���� �ȵȴ�.
	���콺�� ����Ű�� ������ ��� keycode = 1)�� �̺�Ʈ�� �߻��ϰ� ó���Ѵ�.
	Netscape/Firefox/Opera �� ��� e.which 1�� üũ, Safari �� ��� window.event 0 ���� üũ
	IE�� ��� event.button �̳� keycode 13(����Ű)�� üũ
----------------------------------------------------------------------------------------*/
function isAccess(e) {
	
	var keynum;
	var ismouseClick = 1;
	
	if (window.event) {		//IE & Safari
		keynum = e.keyCode;
		
		//Safari�� ��� ���콺Ŭ���� keynum 0 �� �Ѿ��
		if (event.button == 0 || keynum == 0){
			ismouseClick = 0;
		}		
		
	} else if ( e.which ){		// Netscape/Firefox/Opera
		keynum = e.which;
		
		if (keynum == 1) {
			ismouseClick = 0;
		}		
		
	}
	
	//���콺 Ŭ���̰ų� ����Ű�� ������� true�� ��ȯ
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
	����Ÿ ���۳�¥ ���ᳯ¥ üũ
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


//��ȸ�ϱ�
function checkSearchValue(form)
{	
	var searchKey = form.SEARCHKEY.value;
	var searchValue = form.SEARCHVALUE.value;	
	if( searchKey != "" && searchValue == ""){
		alert("�˻� ������ �Է��ϼ���");
		form.SEARCHVALUE.focus();
		return false;
	}
	if (containsChars(form.SEARCHVALUE,"~!@#$%^&*()+|`-=\\[]{};:'\",.<>/?")) {
		alert("�̸� �ʵ忡�� Ư�� ���ڸ� ����� �� �����ϴ�.");
		form.SEARCHVALUE.value="";
		form.SEARCHVALUE.focus();
		return false;
	}
	form.page.value = 1;
	return true;
}