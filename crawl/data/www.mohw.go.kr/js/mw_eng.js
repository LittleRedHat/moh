
// JavaScript Document

/*
guideToggle - html_guide 메뉴하무

[클래스관련]
hasClass, addClass, removeClass

[이벤트관련]
addEvent, removeEvent, eventStopBubble

[dom관련함수]
id, next, prev, first, last, getElementsByClass, parent

[노드 삽입/삭제 관련]
insertBefore, insertAfter
appendTo, append
replaceChild, removeChild, empty

[노드 생성/속성]
create, checkElem, attr, text

[css 관련]
getStyle
insertCSS

[노드 보이기/감추기]
toggle, eleshow, elehidden

[쿠기]
getCookie, setCookie, removeCookie

[이미지 롤오버]
menuOver, menuOut
imgMenuOver

[기타]
popup
quicks
insertSWF
*/

function right(e) {  

	if (navigator.appName == 'Netscape' &&  (e.which == 3 || e.which == 2)) { 
		return false; 
	} else if (navigator.appName == 'Microsoft Internet Explorer' && (event.button == 2 || event.button == 3)) { 
		alert("Can't use the right mouse button!");  
		return false;  
	}  

	return true;  
}

//document.onmousedown=right;

/* Class */
function hasClass(element,value) {
    var re = new RegExp("(^|\\s)" + value + "(\\s|$)");
    return re.test(element.className);
}
function addClass(element,value) {
    if (!element.className)
		element.className = value;
    else
        if (!hasClass(element,value)) element.className += " " + value;
}
function removeClass(element,value) {
    if (element.className && hasClass(element,value)) {
        var re = new RegExp("(^|\\s)" + value);
        element.className = element.className.replace(re,"");
    }
}

/* Event */
function addEvent(obj,evt,fn){
	evt = (evt.indexOf(" ") != -1) ? evt.split(" ") : [evt];
	for(i in evt){
		var e = evt[i];
		if(e == "mousewheel"){
			if(obj.addEventListener) obj.addEventListener('DOMMouseScroll', fn, false);
			obj.onmousewheel = fn;
			break;
		}
		if(obj.addEventListener) obj.addEventListener( (e=="mousewheel") ? "DOMMouseScroll" : e,fn,false );
		else if(obj.attachEvent) obj.attachEvent('on'+e,fn);
	}
}
function removeEvent(obj,evt,fn){
	evt = (evt.indexOf(" ") != -1) ? evt.split(" ") : [evt];
	for(i in evt){
		var e = evt[i];
		if(e == "mousewheel"){
			if(obj.removeEventListener) obj.removeEventListener('DOMMouseScroll', fn, false);
			obj.onmousewheel = null;
			break;
		}
		if(obj.removeEventListener) obj.removeEventListener( (e=="mousewheel") ? "DOMMouseScroll" : e,fn,false );
		else if(obj.detachEvent) obj.detachEvent('on'+e,fn);
	}
}
function stopBubble(e){
	if (e.stopPropagation) e.stopPropagation();
	else window.event.cancelBubble = true;
}
function stopDefault(e){
    if (e.preventDefault) e.preventDefault();
    return false;
}

/* 노드탐색관련 */
function id(id){
	return document.getElementById(id);
}
function next(ele){
	do{
		ele = ele.nextSibling;
	}while(ele && ele.nodeType!=1)
	return ele;
}
function prev(ele){
	do{
		ele = ele.previousSibling;
	}while(ele && ele.nodeType!=1)
	return ele;
}
function first(ele){
	ele = ele.firstChild;
	return ele && ele.nodeType!=1 ? next(ele) : ele;
}
function last(ele){
	ele = ele.lastChild;
	return ele && ele.nodeType!=1 ? prev(ele) : ele;
}

/* getElementsByClass('노드/생략[윈도우]', '태그/생략[*]', '클래스명'); */
function getElementsByClass(node, tagName, srchClass) {
    node = node || window.document;
    tagName = tagName ? tagName.toUpperCase() : "*";
    var eles = node.getElementsByTagName(tagName);
	
	if(!srchClass) return eles;

    var arr = new Array;
    for (var i=0; i<eles.length; i++) {
        if (hasClass(eles[i],srchClass)) arr.push(eles[i]);
    }
    return arr;
}

/* 자신을 덮고있는태그 선택하기(클래스명 분류가능) */
function parent(ele, tagName, srchClass){
	if(typeof tagName=="number"){
		for(var i=0; i<tagName; i++){
			if(ele!=null) ele = ele.parentNode;
		}
		return ele;
	}	
	
	tagName = tagName ? tagName.toUpperCase() : "*";
	if(srchClass){
		if(tagName!="*"){
			while((ele.nodeName!=tagName || !hasClass(ele,srchClass)) && ele.nodeName!="BODY")
				ele = ele.parentNode;
		}else{
			while(!hasClass(ele,srchClass) && ele.nodeName!="BODY")
				ele = ele.parentNode;
		}
	}else{
		if(tagName!="*"){
			while(ele.nodeName!=tagName && ele.nodeName!="BODY")
				ele = ele.parentNode;
		}else{
			ele = ele.parentNode;
		}
	}
	return ele;
}

/* insertBefore = target의 형제레벨로 앞쪽에 삽입 */
function insertBefore(source, target){
    target.parentNode.insertBefore(source, target);
}

/* insertAfter - target의 형제레벨로 뒤쪽에 삽입 */
function insertAfter(source, target) {
    var parent = target.parentNode;
    if(parent.lastChild == target)
        parent.appendChild(source);
    else
        parent.insertBefore(source, target.nextSibling);
}

/* appendTo = 자식요소로 앞쪽에 삽입 */
function appendTo(source, target){
    var first = target.firstChild;
    first.parentNode.insertBefore(source, first);
}

/* appendChild = 자식요소로 뒤쪽에 삽입 */
function append(source, target){
	target.appendChild(source);
}

/* 노드교체 */
function replaceNode(newNode, oldNode){
	return oldNode.parentNode.replaceChild(newNode, oldNode);	
}

/* 노드지우기 */
function removeNode(ele){
	return ele.parentNode.removeChild(ele);
}

/* 노드비우기 */
function emptyNode(oldNode){
	var newNode = oldNode.cloneNode(false);
	return oldNode.parentNode.replaceChild(newNode, oldNode);
}

/* create */
function create( elem ) {
    return document.createElementNS ?
        document.createElementNS( 'http://www.w3.org/1999/xhtml', elem ) :
        document.createElement( elem );
}

/* checkElem */
function checkElem( elem ) {
    return elem && elem.constructor == String ?
        document.createTextNode( elem ) : elem;
}

/* attr */
function attr(elem, name, value) {
    if ( !name || name.constructor != String ) return '';

    name = { "for":"htmlFor", "class":"className" }[name] || name;
    if (value != null){
        if (elem[name]) elem[name] = value;
        if (elem.setAttribute)
            elem.setAttribute(name,value);
    }
    return elem[name] || elem.getAttribute(name) || '';
}

/* text */
function text(e){
	var t = "";
	e = e.childNodes;
	
	for(var i=0; i<e.length; i++){
		if(e[i].nodeType == 8) continue;
		t += ( e[i].nodeType!=1 ) ? e[i].nodeValue : text(e[i]);
	}
	return t;
}

/* setOpacity */
function setOpacity(ele, value){
	if(typeof ele =='string') ele=document.getElementById(ele);
	ele.style.opacity = (value / 100);
	ele.style.filter = "alpha(opacity="+value+")";
}

/* position */
function posX(elem){ return parseInt(getStyle(elem, "left")); }
function posY(elem){ return parseInt(getStyle(elem, "top")); }
function setX(elem, pos){ elem.style.left = pos+"px"; }
function setY(elem, pos) { elem.style.top = pos +"px"; }

/* offset */
function pageX(elem){
    var p = 0;
    while ( elem.offsetParent ){
        p += elem.offsetLeft;
        elem = elem.offsetParent;
    }
    return p;
}
function pageY(elem){
    var p = 0;
    while ( elem.offsetParent ) {
        p += elem.offsetTop;
        elem = elem.offsetParent;
    }
    return p;
}
function parentX(elem){ return elem.parentNode == elem.offsetParent ? elem.offsetLeft : pageX(elem) - pageX(elem.parentNode); }
function parentY(elem){ return elem.parentNode == elem.offsetParent ? elem.offsetTop : pageY(elem) - pageY(elem.parentNode); }

function getX(e) { e = e || window.event; return e.pageX || (e.clientX + document.documentElement.scrollLeft || document.body.scrollLeft || 0); }
function getY(e) { e = e || window.event; return e.pageY || (e.clientY + document.documentElement.scrollTop || document.body.scrollTop || 0); }

function getElementX(e){ return ( e && e.layerX ) || window.event.offsetX; }
function getElementY(e){ return ( e && e.layerY ) || window.event.offsetY; }

function scrollX(){ var de = document.documentElement; return self.pageXOffset || ( de && de.scrollLeft ) || document.body.scrollLeft; }
function scrollY(){ var de = document.documentElement; return self.pageYOffset || ( de && de.scrollTop ) || document.body.scrollTop; }

function pageWidth(){ return document.body.scrollWidth; }
function pageHeight(){ return document.body.scrollHeight; }

function windowWidth(){ var de = document.documentElement; return self.innerWidth || ( de && de.clientWidth ) || document.body.clientWidth; }
function windowHeight(){ var de = document.documentElement; return self.innerHeight || ( de && de.clientHeight ) || document.body.clientHeight; }

function getHeight(elem){ return parseInt(getStyle(elem, "height")) }
function getWidth(elem) { return parseInt( getStyle(elem, "width")) }

function fullWidth(elem) {
    if (getStyle(elem, 'display') != 'none') return elem.offsetWidth || getWidth(elem);
	var old = resetCSS(elem, {display:'block', visibility: 'hidden', position: 'absolute'});
    var w = elem.clientWidth || getWidth(elem);
    restoreCSS(elem, old);
    return w;
}
function fullHeight(elem) {
    if (getStyle(elem, 'display') != 'none') return elem.offsetHeight || getHeight(elem);
	var old = resetCSS(elem, {display: 'block', visibility: 'hidden', position: 'absolute'});
    var h = elem.clientHeight || getHeight(elem);
    restoreCSS(elem, old);
    return h;
}

function resetCSS(elem, prop) {
    var old = {};
	for ( var i in prop ){
        old[i] = elem.style[i];
        elem.style[i] = prop[i];
    }
    return old;
}
function restoreCSS(elem, prop) {
    for ( var i in prop )
        elem.style[i] = prop[i];
}

/* getStyle */
function getStyle(ele, what){
	if(typeof ele == "string") var ele = document.getElementById(ele);
    if(ele.style[what]) return ele.style[what];
	
	var value = "";
	if(ele.currentStyle)
		value = ele.currentStyle[what];
	else if(document.defaultView.getComputedStyle)
		value = document.defaultView.getComputedStyle(ele,null)[what];
		
	return value;
}

/* insertCSS */
function insertCSS(str){
    var style = document.createElement("style");
    style.setAttribute("type","text/css");
    var css_code = str;
    if (style.styleSheet) {
		// Only For IE6, IE7, IE8
        style.styleSheet.cssText = css_code;
    } else {
        css_code = document.createTextNode(css_code);
        style.appendChild(css_code);
    }
    var head = document.getElementsByTagName("head")[0];
    head.appendChild(style);
}

// GNB
function gnbMenu(obj){
	var obj = document.getElementById(obj);

	// 메인메뉴
	var objLi = obj.getElementsByTagName("LI");
	var mainMenu = new Array;
	for(i=0; i<objLi.length; i++){
		if(objLi[i].className.indexOf("gnblist") != -1){
			mainBtn = objLi[i].getElementsByTagName("A")[0];
			mainMenu.push(mainBtn);
			for(j=0; j<mainMenu.length; j++){
				mainMenu[j].container = obj;
				mainMenu[j].cnt = j + 1;
				mainMenu[j].formList = document.getElementById("submenu_" +  mainMenu[j].cnt);
				mainMenu[j].Img = mainMenu[j].getElementsByTagName("IMG")[0];
				mainMenu[j].onmouseover = mainMenu[j].onfocus = function(){
					currentMenu = this.container.first;
					
					if(currentMenu){
						if(currentMenu.formList){
							currentMenu.formList.style.display = "none";
						}							
						if(currentMenu.Img){
							currentMenu.Img.src = currentMenu.Img.src.replace("_over.gif", ".gif");
						} else {
							removeClass(currentMenu.parentNode, "over");
						}
					}
					
					if(this.formList){
						this.formList.style.display = "";
					}					
					if(this.Img){
						this.Img.src = this.Img.src.replace(".gif", "_over.gif");
					} else {
						addClass(this.parentNode, "over");
					}

					this.container.first = this;
				}
			}
		}
	}
}


// GNB & LNB
function imgMenuOver(containderID) {
	var objwrap = document.getElementById(containderID);
	var imgMenu = objwrap.getElementsByTagName("img");
	for (i=0; i<imgMenu.length; i++) {
		if (imgMenu[i].src.indexOf("_over.gif") != -1 ) {
			continue;
		}
		imgMenu[i].onmouseover = function() {
			this.src = this.src.replace (".gif","_over.gif");
		}
		imgMenu[i].onmouseout = function() {
			this.src = this.src.replace ("_over.gif",".gif");
		}
	}
}

//GNB & LNB
function imgMenuOver2(containderID) {
	var objwrap = document.getElementById(containderID).getElementsByTagName('ul');
	var imgMenu = objwrap.getElementsByTagName("img");
	for (i=0; i<imgMenu.length; i++) {
		if (imgMenu[i].src.indexOf("_over.gif") != -1 ) {
			continue;
		}
		imgMenu[i].onmouseover = function() {
			this.src = this.src.replace (".gif","_over.gif");
		}
		imgMenu[i].onmouseout = function() {
			this.src = this.src.replace ("_over.gif",".gif");
		}
	}
}

// tab contents
function styleLinkCheck(){ /* css전혀 없으면 false를 돌려줌 */
	var ss = document.styleSheets[0];
	if(ss) return ss;
	else return false;
}

// h태그로 구현한 탭
function tabList(ele, active){
	if(styleLinkCheck() === false) return;

	var ele = document.getElementById(ele);
	if(active === undefined) active = 0;						
	
	// tabtit를 포함하는 제목 노드들 수집 
	var btn = ele.getElementsByTagName("*");
	for(var i=0; i<btn.length; i++){
		if(btn[i].className.indexOf('tabtit') != -1){
			btn = btn[i].nodeName;
			btn = ele.getElementsByTagName(btn);
			break;
		}
	}
	
	
	// 타이틀의 타겟 레이어 이름중 숫자만 뺀 영문만 tab1 중 tab만
	var layerName = btn[0].getElementsByTagName("A")[0].href.split("#")[1];
	layerName = layerName.slice(0, layerName.length-1);
	
	for(var i=0; i<btn.length; i++){
		ele["target" + i] = document.getElementById(layerName + (i+1)); // 노드저장 예) tab1, tab2, tab3
		ele["a" + i] = btn[i].getElementsByTagName("A")[0]; // 탭링크
		ele["img" + i] = btn[i].getElementsByTagName("IMG")[0]; // 이미지노드 저장
		btn[i].style.position = "absolute"; // 제목레이어 적용
		ele.getElementsByTagName("P")[i].style.position = "absolute"; // 더보기 레이어
	}
	
	/* 초기세팅 */
	var oldActive = active;
	for(var i=0; i<btn.length; i++){
		ele["a" + i].cnt = i;
		ele["a" + i].onclick = function menuActive(){
			ele["target" + oldActive].style.display = "none";
			ele["img" + oldActive].src = ele["img" + oldActive].src.replace("_over", "_out");
			
			ele["target" + this.cnt].style.display = "block";
			ele["img" + this.cnt].src = ele["img" + this.cnt].src.replace("_out", "_over");
			oldActive = this.cnt;
			return false;
		}
		
		if(active == i) continue; // 초기 활성화
		ele["target" + i].style.display = "none";
		ele["img" + i].src = ele["img" + i].src.replace("_over", "_out");

	}
}

// 영문 사이트 전체 조회하기
function searchCommon(form)
{		
	var searchValue	= form.SEARCHVALUE.value;
	if( searchValue == ""){
		alert("Please enter the keyword for category search.");
		form.SEARCHVALUE.focus();
		return false;
	}else if (containsChars(form.SEARCHVALUE,"~!@#$%^&*()+|`-=\\[]{};:'\",.<>/?")) {
		alert("You can not use special characters in the name of the field.");
		form.SEARCHVALUE.value="";
		return false;
	}else{
		return true;
	}
}

// 폰트 사이즈 조절
function fontSize(){
	
	var arr = new Array();
	arr[5] = '112.5%';
	arr[4] = '100%';
	arr[3] = '87.5%';
	arr[2] = '75%';
	arr[1] = '70%';
	arr[0] = '62.5%';

	this.getCookie = function(name){
		var allCookies = decodeURIComponent(document.cookie);
		var pos = allCookies.indexOf(name+"=");
		
		if(pos == -1) return undefined;
	
		var start = pos + (name.length+1);
		var end = allCookies.indexOf(';', start);
		if(end == -1) end = allCookies.length;
		var value = allCookies.substring(start, end);
		return value = decodeURIComponent(value);
	}
	
	this.setCookie = function(name, value, cPath){
		var pathStr = (cPath) ? "; path=" + cPath : "; path=/";
		document.cookie = encodeURIComponent(name) + "=" + encodeURIComponent(value) + pathStr;
	}

	var loop = this.getCookie('fontControl') || 2;
	document.body.style.fontSize = arr[loop];
	
	this.btnMinus = function(){
		if(loop > 0){
			loop--;
			document.body.style.fontSize = arr[loop];
			_root.setCookie('fontControl', loop);
		}
	}
	this.btnPlus = function(){
		if(loop < (arr.length - 1)){
			loop++;
			document.body.style.fontSize = arr[loop];
			_root.setCookie('fontControl', loop);
		}
	}
	
	var _root = this;
	
}

function goUrlOnSubmit(formEl) {			
	var homepage = formEl.sitelink.value;		
	if(homepage == "" || homepage == "http://"){
		return false;
	}else{
		formEl.action = homepage;
		return true;
	}
}
//png
//var clear="/images/front_eng/common/clear.gif"; //path to clear.gif

//document.write('<script type="text/javascript" id="ct" defer="defer" src="javascript:void(0)"><\/script>');var ct=document.getElementById("ct");ct.onreadystatechange=function(){pngfix()};pngfix=function(){var els=document.getElementsByTagName('*'),ip=/\.png/i,al="progid:DXImageTransform.Microsoft.AlphaImageLoader(src='",i=els.length,uels=new Array(),c=0;while(i-->0){if(els[i].className.match(/unitPng/)){uels[c]=els[i];c++;}}if(uels.length==0)pfx(els);else pfx(uels);function pfx(els){i=els.length;while(i-->0){var el=els[i],es=el.style,elc=el.currentStyle,elb=elc.backgroundImage;if(el.src&&el.src.match(ip)&&!es.filter){es.height=el.height;es.width=el.width;es.filter=al+el.src+"',sizingMethod='crop')";el.src=clear;}else{if(elb.match(ip)){var path=elb.split('"'),rep=(elc.backgroundRepeat=='no-repeat')?'crop':'scale',elkids=el.getElementsByTagName('*'),j=elkids.length;es.filter=al+path[1]+"',sizingMethod='"+rep+"')";es.height=el.clientHeight+'px';es.backgroundImage='none';if(j!=0){if(elc.position!="absolute")es.position='static';while(j-->0)if(!elkids[j].style.position)elkids[j].style.position="relative";}}}}};};














function getCookie(sName) {
	var ca = document.cookie.split(/\s*;\s*/);
	var re = new RegExp("^(\\s*"+sName+"\\s*=)");
	
	for(var i=0; i < ca.length; i++) {
		if (re.test(ca[i])) return unescape(ca[i].substr(RegExp.$1.length));
	}
	
	return null;
}

 function setCookie(sName, sValue, nDays, sDomain, sPath) {
	var sExpire = "";
	
	if (typeof nDays == "number") {
		sExpire = ";expires="+(new Date((new Date()).getTime()+nDays*1000*60*60*24)).toGMTString();
	}
	if (typeof sDomain == "undefined") sDomain = "";
	if (typeof sPath == "undefined") sPath = "/";
	
	document.cookie = sName+"="+escape(sValue)+sExpire+"; path="+sPath+(sDomain?"; domain="+sDomain:"");
	
	return this;
}

function removeCookie(sName, sDomain, sPath) {
	if (this.getCookie(sName) != null) this.setCookie(sName, "", -1, sDomain, sPath);	
	return this;
}

var aDefaultList=["mw_100103","mw_100113"];//News &amp; Notice,Press Release,Healthcare
var aCookieList=[];
var aCacheList=[];

$(function() {	
	var bCookie = getCookie("MWENGSERV");	
	if(bCookie==null||bCookie.length<1)
	{
		$("#fmenu").html("");	
		jQuery.each(aDefaultList,function(i){				
			var val = $("#"+aDefaultList[i]).val().split("|");
			$("<li><a href='"+val[0]+"'>" + val[2] + "</a></li>").appendTo("#fmenu");			
		});	
		removeCookie("MWENGSERV");		
		setCookie("MWENGSERV",aDefaultList.join("@"),365);
		aCacheList = aDefaultList.concat();
	}
	else
	{		
		$("#fmenu").html("");
		aCookieList=bCookie.split("@");
		jQuery.each(aCookieList,function(i){
			if(i<3){
				var val = $("#"+aCookieList[i]).val().split("|");				
				$("<li><a href='"+val[0]+"'>" + val[2] +"</a></li>").appendTo("#fmenu");
			}
		});	
		
		aCacheList = aCookieList.concat();
	}
/*
	$("input[name='setmenu']").click(function() {		
		if($("input[name='setmenu']:checked").size() > 3){
			alert("You can choose up to three menu items.");
			$(this).removeAttr("checked");
		}else{
			$("#fmenu").html("");
			var chcked_id= ($(this).attr("id"));
			if(!$(this).attr("checked")){
				jQuery.each(aCacheList,function(i){						
					if(chcked_id == aCacheList[i]){						
						aCacheList.splice(i,1);
					}						
				});				
			}else{
				aCacheList.push($(this).attr("id"));
			}
			jQuery.each(aCacheList,function(i){	
				var val = $("#"+aCacheList[i]).val().split("|");				
				$("<li><a href='"+val[0]+"'>" + val[2] +"</a></li>").appendTo("#fmenu");
			});
		}		
	});	*/
	$("input[name='setmenu']").click(function() {		
		if($("input[name='setmenu']:checked").size() > 3){
			alert("You can choose up to three menu items.");
			$(this).removeAttr("checked");
		}else{
			$("#fmenu").html("");
			jQuery.each($("input[name='setmenu']:checked"),function(i){	
				var chk = $("input[name='setmenu']:checked").eq(i);
				var val = $($("input[name='setmenu']:checked").eq(i)).val().split("|");				
				$("<li><a href='"+val[0]+"'>" + val[2] +"</a></li>").appendTo("#fmenu");
			});
		}		
	});
	$("#svcmore_h").click(function() {
		if($("#msetup_layer").css("display") == "none"){
			$("#svcmore_h img:first-child").attr("src", "/images/front_eng/main/menu_setup_on.gif");
			$("input[name='setmenu']:checkbox").each(function(chk){				
				$(this).removeAttr("checked");
			});
			var bCookie = getCookie("MWENGSERV");
			aCookieList=bCookie.split("@");			
			jQuery.each(aCookieList,function(i){				
				$("input[name='setmenu']:checkbox").each(function(chk){				
					if($(this).attr("id") == aCookieList[i]){					
						$(this).prop("checked","checked");
					}
				});
			});
		} else {
			$("#svcmore_h img:first-child").attr("src", "/images/front_eng/main/menu_setup.gif")
		}
		$("#msetup_layer").toggle();
		return false;
	});	
	
	$("#mymenu_default").click(function() {
		$("input[name='setmenu']:checkbox").each(function(chk){				
			$(this).removeAttr("checked");
		});			
		$("#fmenu").html("");
		jQuery.each(aDefaultList,function(i){				
			var val = $("#"+aDefaultList[i]).val().split("|");			
			$("<li><a href='"+val[0]+"'>" + val[2] +"</a></li>").appendTo("#fmenu");
			$("#"+aDefaultList[i]).prop("checked",'checked');	
		});		
		aCacheList =[];
		aCacheList = aDefaultList.concat();				
		return false;		
	});	
	$("#mymenu_cancel").click(function() {	
		$("#fmenu").html("");
		jQuery.each(aCookieList,function(i){				
			var val = $("#"+aCookieList[i]).val().split("|");			
			$("<li><a href='"+val[0]+"'>" + val[2] +"</a></li>").appendTo("#fmenu");
		});	
		removeCookie("MWENGSERV");		
		setCookie("MWENGSERV",aCookieList.join("@"),365);
		aCacheList = aCookieList.concat();
		$("#msetup_layer").hide();
		return false;
	});	
	$("#msbtn_close").click(function() {
		$("#fmenu").html("");
		jQuery.each(aCookieList,function(i){				
			var val = $("#"+aCookieList[i]).val().split("|");			
			$("<li><a href='"+val[0]+"'>" + val[2] + "</a></li>").appendTo("#fmenu");
		});	
		removeCookie("MWENGSERV");		
		setCookie("MWENGSERV",aCookieList.join("@"),365);
		aCacheList = aCookieList.concat();
		$("#msetup_layer").hide();
		return false;
	});	
	$("#mymenu_set").click(function() {
		removeCookie("MWENGSERV");		
		if(aCacheList.length < 1){
			alert("No menu item has been chosen. You will be returned to the initial menu setup.");				
			$("#fmenu").html("");
			jQuery.each(aDefaultList,function(i){
				var val = $("#"+aDefaultList[i]).val().split("|");				
				$("<li><a href='"+val[0]+"'>" + val[2] + "</a></li>").appendTo("#fmenu");
			});				
			setCookie("MWENGSERV",aDefaultList.join("@"),365);
			aCookieList = aDefaultList.concat();
			aCacheList = aDefaultList.concat();			
		}else{
			
			aCacheList =[];
			
			$.each($("input[name='setmenu']:checked"),function(i){	
				aCacheList.push($("input[name='setmenu']:checked").eq(i).attr('id'));
			});
			
			
			setCookie("MWENGSERV",aCacheList.join("@"),365);
		}		
		$("#msetup_layer").hide();
		return false;
	});		
});