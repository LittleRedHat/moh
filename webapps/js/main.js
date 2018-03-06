/**
 * Created by 10975 on 2017/11/1.
 */
if(!window.sessionStorage.getItem('user')){
     window.location = '../login.html'
}



var server_base = 'http://47.97.96.152';

var nations_table;
var languages_table;
$.getJSON("../data/nations_list.json", function (data) {
    nations_table = data;
    //console.log(nations_table);
    //console.log(nations_table["cn"]);
});
$.getJSON("../data/language_list.json", function (data) {
    languages_table = data;
    //console.log(languages_table);
    //console.log(languages_table["en"], languages_table["a"] ? "a" : "b");
});

showWordCloud();
$('#search').click(function () {
    search();
});
$('#trans').click(function () {
    var inputs = $('.search-input');
    var keyWord = "";
    for (var i = 0; i < inputs.length; i++)
        if (inputs[i].value != "")
            keyWord += inputs[i].value + " ";
    //console.log(keyWord);
    if (keyWord == "")
        $('#trans-res').html("请输入关键字！");
    else {
        $('#trans-res').html("");
        keyWordTrans(keyWord);
    }
});
$('#show_lan_list_btn').click(function () {
    var display = $('#language_list').css("display");

    //console.log(display);
    if (display == "none") {
        $('#language_list').css("display", "block");
        $('#show_lan_list_btn').text("隐藏语言列表");
    }
    else{
        $('#language_list').css("display", "none");
        $('#show_lan_list_btn').text("显示语言列表");
    }
});
$('#show_nation_list_btn').click(function () {
    var display = $('#nation_list').css("display");

    //console.log(display);
    if (display == "none") {
        $('#nation_list').css("display", "block");
        $('#show_nation_list_btn').text("隐藏国家列表");
    }
    else{
        $('#nation_list').css("display", "none");
        $('#show_nation_list_btn').text("显示国家列表");
    }
});

function choose_lan(str) {
    //console.log(str);
    $('#language').val($('#language').val() + str + " " );
}

function choose_nation(str) {
    $('#nation').val($('#nation').val() + str + " ");
}

//展示地图
function map(searchRes) {
    $("#map").css({ "display": "block" });
    var worldJson;

    //获取地图数据
    $.ajaxSettings.async = false;
    $.getJSON("../data/world.json", function(data) {
        worldJson = data;
    });

    //echarts显示地图
    var map = echarts.init(document.getElementById('map'));
    echarts.registerMap('world', worldJson);
    var option = {
        title: {
            text: '热点地图'
        },
        backroundColor: '#404a59',
        series: [{
            name: '热度',
            type: 'scatter',
            coordinateSystem: 'geo',
            encode: {
                label: 2
            },
            data: convertToMapData(searchRes),
            symbol: 'pin',
            symbolSize: function(val) {
                var result = val[2] / 8;
                return result > 100 ? 100 : result;
            },
            label: {
                emphasis: {
                    show: true,
                    formatter: function (obj) {
                        //console.log(obj);
                        var name = obj.data.name;
                        var value = obj.data.value[2];
                        return name + "\n结果数量: " + value;
                    },
                    position: 'right'
                }
            }
        }, ],
        geo: {
            map: 'world',
            left: 0,
            top: 0,
            right: 0,
            bottom: 0,
            roam: false,
            itemStyle: {
                normal: {
                    //color: '#044161',
                    areaColor: '#004981',
                    borderColor: '#029fd4'
                },
                emphasis: {
                    areaColor: '#029fd4',
                    shadowOffsetX: 1,
                    shadowOffsetY: 1
                }
            }
        }

    }
    map.setOption(option);
}

//将返回结果转为地图上显示的数据
function convertToMapData(searchRes) {
    var country;
    var countryTable;
    $.ajaxSettings.async = false;

    //国家经纬度信息
    $.getJSON("../data/capitalLL.json", function(data) {
        country = data;
    });
    $.getJSON("../data/capitalTable.json", function(data) {
        countryTable = data;
    });
    for (x in searchRes){
        if(searchRes[x].key == 'int'){
            continue
        }
        country[countryTable[searchRes[x].key]].value[2] = searchRes[x].doc_count;
    }
       
    //console.log(country);
    return country;
}


var unicode2utf8 = function(unicode) {
    return unicode.replace(/%u([0-9a-fA-F]+)/g, function(match, hex) {
      var utf8CharCodes = [];
      c = parseInt(hex, 16);
      if (c < 128) {
        utf8CharCodes.push(c);
      } else if (c < 2048) {
        utf8CharCodes.push((c >> 6) | 192, (c & 63) | 128);
      } else if (c < 65536) {
        utf8CharCodes.push((c >> 12) | 224, ((c >> 6) & 63) | 128, (c & 63) | 128);
      } else {
        utf8CharCodes.push((c >> 18) | 240, ((c >> 12) & 63) | 128, ((c >> 6) & 63) | 128, (c & 63) | 128);
      }
      for (var i=utf8CharCodes.length-1;i>=0;i--) {
        utf8CharCodes[i] = '%' + utf8CharCodes[i].toString(16);
      }
      return utf8CharCodes.join('');
    });
};

//翻译关键字
function keyWordTrans(keyWord) {
    var languageName = {
        'en': '英文',
        'jp': '日文',
        'kor': '朝鲜文',
        'fra': '法文',
        'spa': '西班牙文',
        'th': '泰国语',
        'ara': '阿拉伯文',
        'ru': '俄文',
        'pt': '葡萄牙文',
        'de': '德文',
        'it': '意大利文',
        'el': '希腊文',
        'nl': '荷兰文',
        'pl': '波兰文',
        'bul': '保加利亚文',
        'est': '爱沙尼亚文',
        'dan': '丹麦文',
        'fin': '芬兰文',
        'cs': '捷克语',
        'rom': '罗马尼亚文',
        'slo': '斯洛文尼亚文',
        'swe': '瑞典文',
        'hu': '匈牙利语',
        'vie': '越南文'
    };
    var result = "";
    $("#trans-res").html("");
    var appid = '2015063000000001';
    var key = '12345678';
    var salt = (new Date).getTime();
    var query = unicode2utf8(keyWord);
    // 多个query可以用\n连接  如 query='apple\norange\nbanana\npear'
    var from = 'auto';
    var to = ['en', 'jp', 'kor', 'fra', 'spa', 'th', 'ara', 'ru', 'pt', 'de', 'it', 'el', 'nl',
        'pl', 'bul', 'est', 'dan', 'fin', 'cs', 'rom', 'slo', 'swe', 'hu', 'vie'
    ];
    var str1 = appid + query + salt + key;
    var sign = MD5(str1);
    // f1的任务代码
    for (x in to) {
        trans(x);
    }
    

    function trans(x) {
        //console.log(x)
        $.ajax({
            async: false,
            url: 'http://api.fanyi.baidu.com/api/trans/vip/translate',
            type: 'get',
            dataType: 'jsonp',
            data: {
                q: query,
                appid: appid,
                salt: salt,
                from: from,
                to: to[x],
                sign: sign
            },
            success: function(data) {
                //console.log(data);
                $("#trans-res").html($("#trans-res").html() + languageName[to[x]] + ": " + data.trans_result[0].dst + '  ----  ');
            }
        });
    }

}

//词云图
function wordCloud(data) {
    var option = {
        title: {
            text: '搜索历史',
            x: 'center',
            textStyle: {
                fontSize: 23
            }
        },
        backgroundColor: '#F7F7F7',
        series: [{
            name: '搜索历史',
            type: 'wordCloud',
            sizeRange: [12, 80],
            rotationRange: [-45, 90],
            textPadding: 0,
            autoSize: {
                enable: true,
                minSize: 6
            },
            textStyle: {
                normal: {
                    color: function() {
                        return 'rgb(' + [
                            Math.round(Math.random() * 160),
                            Math.round(Math.random() * 160),
                            Math.round(Math.random() * 160)
                        ].join(',') + ')';
                    }
                },
                emphasis: {
                    shadowBlur: 10,
                    shadowColor: '#333'
                }
            },
            data: data
        }]
    };
    var wordCloud = echarts.init(document.getElementById('wordCloud'));
    wordCloud.setOption(option);
}

//词云图显示
function showWordCloud() {
    var url = server_base+'/api/moh/history';

    $.ajax({
        async: true,
        url: url,
        type: 'get',
        dataType: 'json',
        success: function(data) {
            var wordCloudData = [];
            var key;
            //console.log(data);
            for (key in data)
                wordCloudData.push({ "name": key, "value": data[key] });
            wordCloud(wordCloudData);
        }
    });
}

//整合请求信息
function createRequestData(from, should) {
    var sort = $("#sort option:selected").val();
    var type = $("#attachment option:selected").val();
    var title_content = $('#title_content option:selected').val();
    var date_start = $('#date_start').val();
    var date_end = $('#date_end').val();
    //console.log("start:" + date_start + " end: " + date_end);
    var nation = [];
    var language = [];
    var size = $('#size').val();

    if ($('#nation').val() == "")
        nation.push("all");
    else
        nation = getNation($('#nation').val());

    if ($('#language').val() == "")
        language.push("all");
    else
        language = trans_languagecode(getLanguage($('#language').val(), false));

    var requestData = {
        "should": should,
        "size": size,
        "from": from,
        "sort": sort,
        "by": title_content,
        "filters": [
            {"name": "type", "value": [type]},
            {"name": "nation", "value": nation},
            {"name": "language", "value": language},
            {"name": "publish", "value": [date_start, date_end]}
            ]
    };
    console.log(requestData);
    return JSON.stringify(requestData);
}

//递交搜索请求，得到结果后分页显示
function searchRes(searchDataJson) {
    var url = server_base+'/api/moh/es/search';
    //var num = 20;
    //console.log(searchData);
    var searchData = JSON.parse(searchDataJson);


    $.ajax({
        async: true,
        url: url,
        contentType: 'application/json',
        type: 'post',
        dataType: 'json',
        data: JSON.stringify(searchData),
        success: function(requestRes) {
            var mapData = requestRes['nation_distribution'];
            //var data = requestRes['records'];
            var pageNum = Math.ceil(requestRes['total'] / searchData['size']);
            pageNum = pageNum < 1 ? 1 : pageNum;
            //console.log(mapData);
            map(mapData);

            var showData = function(currentPage) {
                currentPage = (currentPage - 1) * searchData['size'];
                searchData.from = currentPage;
                console.log(searchData);

                $.ajax({
                    async: true,
                    url: url,
                    type: 'post',
                    contentType: 'application/json',
                    dataType: 'json',
                    data: JSON.stringify(searchData),
                    success: function(requestRes_2) {
                        var data = requestRes_2['records'];
                        //console.log(createRequestData(num, currentPage));
                        console.log(requestRes_2);
                        var str = '';

                        for (var i = 0; i < data.length; i++) {
                            var title = (data[i]['type'] == 'html'?data[i]['title']:data[i]['attachment']['title'])
                            str += '<tr class="row">';
                            str += '<th><a target="_blank" href="'+ server_base +'/'+ data[i]['local_url'] +
                                '">' + title + '</a></th>';
                            str += '<th id="trans' + i + '"></th>';
                            str += '<th><a target="_blank" href="' + data[i]['url'] + '">原地址</a></th>';
                            str += '<th>' + (nations_table[data[i]['nation']] ?
                                nations_table[data[i]['nation']] : data[i]['nation']) + '</th>';

                            var language = data[i]['language'].split('-')
                            if(language.length >0){
                                language = language[0].toLowerCase()
                            }

                            str += '<th>' + transLan(language) + '</th>';
                            str += '<th>' + data[i]['publish'] + '</th>';
                            str += '</tr>';
                        }
                        $('#data_table').html(str);
                        str = '';
                        for (var i = 0; i < data.length; i++) {
                            tranTitle(i);
                        }(i);

                        function tranTitle(i) {
                            var appid = '2015063000000001';
                            var key = '12345678';
                            var salt = (new Date).getTime();
                            var query = data[i]['title'].replace(/\r|\t|\n/g, "");
                            var from = 'auto';
                            var to = 'zh';
                            var str1 = appid + query + salt + key;
                            var sign = MD5(str1);
                            //console.log(query);
                            $.ajax({
                                url: 'http://api.fanyi.baidu.com/api/trans/vip/translate',
                                type: 'get',
                                dataType: 'jsonp',
                                data: {
                                    q: query,
                                    appid: appid,
                                    salt: salt,
                                    from: from,
                                    to: to,
                                    sign: sign
                                },
                                success: function(data) {
                                    //console.log(data)
                                    $("#trans" + i).html(data.trans_result[0].dst);
                                }
                            });
                        }
                    }
                });
            }

            laypage({
                cont: 'laypage',
                pages: pageNum,
                jump: function(obj) {
                    showData(obj.curr);
                    //console.log(obj);
                }
            });
        }

    });
}

//逆波兰式解析字符串至数组
function textToArr(text) {
    var start = 0;
    var end;
    var stringArr = [];
    var stack = [];
    var postfix = [];
    var result = [];
    for (var i = 0; i < text.length; i++) {
        if (text.charAt(i) == '&' || text.charAt(i) == ' ') {
            end = i;
            stringArr.push(text.substring(start, end));
            stringArr.push(text.charAt(i));
            start = i + 1;
        }
    }
    stringArr.push(text.substring(start, text.length));
    //return stringArr;
    for (var i = 0; i < stringArr.length; i++) {
        if (stringArr[i] == '&' || stringArr[i] == ' ') {
            if (stack.length == 0)
                stack.push(stringArr[i]);
            else {
                while (compare(stack[stack.length - 1], stringArr[i])) {
                    postfix.push(stack.pop());
                }
                stack.push(stringArr[i]);
            }
        } else
            postfix.push(stringArr[i]);
    }
    while (stack.length > 0) {
        postfix.push(stack.pop());
    }
    //return postfix;

    for (var i = 0; i < postfix.length; i++) {
        if (postfix[i] == '&') {
            var tmp1 = stack.pop();
            var tmp2 = stack.pop();
            if (tmp1 instanceof Array && tmp2 instanceof Array)
                stack.push(tmp1.concat(tmp2));
            else if (tmp1 instanceof Array) {
                tmp1.push(tmp2);
                stack.push(tmp1);
            } else if (tmp2 instanceof Array) {
                tmp2.push(tmp1);
                stack.push(tmp2);
            } else
                stack.push([tmp2, tmp1]);
        } else if (postfix[i] == ' ') {} else
            stack.push(postfix[i]);
    }
    for (var i = 0; i < stack.length; i++) {
        if (!(stack[i] instanceof Array))
            stack[i] = [stack[i]];
    }
    //console.log(stringArr);
    //console.log(postfix);
    //console.log(stack);
    return stack;

    //比较符号优先级
    function compare(a, b) {
        if (a == '&' && b == '&' || a == '&' && b == ' ' || a == ' ' && b == ' ')
            return true;
        else if (a == ' ' && b == '&')
            return false;
    }
}

//将输入的搜索词组分割，返回包含字符串数组的数组
function toSearchWordsArr() {
    var inputs = $('.search-input');
    var result = [];

    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].value != "")
            result.push(((String)(inputs[i].value)).split("&"));
    }

    return result;
}

//对关键字进行翻译，然后进行搜索
function search() {
    var wordsArr = toSearchWordsArr();
    var result = [];

    var languageStr = $('#language').val();
    var to = getLanguage(languageStr, true);

    var appid = '2015063000000001';
    var key = '12345678';
    var salt = (new Date).getTime();
    var from = 'auto';
    var str, sign;
    var request = 0;
    var response = 0;

    for (var i = 0; i < wordsArr.length; i++) {
        (function(i) {
            for (var k = 0; k < to.length; k++) {
                (function(k) {
                    var tmp = [];
                    for (var j = 0; j < wordsArr[i].length; j++) {
                        (function(j) {
                            if (wordsArr[i][j] != '') {
                                request++;
                                str = appid + wordsArr[i][j] + salt + key;
                                sign = MD5(str);
                                $.ajax({
                                    async: true,
                                    url: 'http://api.fanyi.baidu.com/api/trans/vip/translate',
                                    type: 'get',
                                    dataType: 'jsonp',
                                    data: {
                                        q: wordsArr[i][j],
                                        appid: appid,
                                        salt: salt,
                                        from: from,
                                        to: to[k],
                                        sign: sign
                                    },
                                    success: function(data) {
                                        //console.log(data);
                                        response++;
                                        tmp.push({"q": data.trans_result[0].dst,
                                            "language": trans_language_code_single(to[k])});
                                        if (response == request) {
                                            //result.push(tmp);
                                            for (var i = 0; i < result.length; i++) {
                                                if (result[i].length === 0) {
                                                    remove(result, i);
                                                    i--;
                                                }
                                            }
                                            //console.log(result);
                                            searchRes(createRequestData(0, result));
                                        }
                                    }
                                });
                            }
                        })(j);
                    }
                    result.push(tmp);
                })(k);
            }
            //result.push(wordsArr[i]);
        })(i);
    }

    //setTimeout()

    //return result;
}

//根据languageStr得到要求语言种类（百度翻译语言简写码），forTran表示函数是否用于翻译
function getLanguage(languageStr, forTran) {
    var to_all = ['zh', 'en', 'jp', 'kor', 'fra', 'spa', 'th', 'ara', 'ru', 'pt', 'de', 'it', 'el', 'nl',
        'pl', 'bul', 'est', 'dan', 'fin', 'cs', 'rom', 'slo', 'swe', 'hu','vie'];
    var to = [];
    if (languageStr == "")
        to = to_all;
    else {
        to = languageStr.split(" ");
        //console.log(to);

        for (var i = 0; i < to.length; i++) {
            if ($.inArray(to[i], to_all) < 0) {
                remove(to, i);
                i--;
            }
        }

        if (to.length === 0) {
            if (forTran)
                to = to_all;
            else
                to.push("all");
        }
    }

    return to;
}
//将to的语言语言缩写码转为国际通用码
function trans_languagecode(to) {
    for (var i = 0; i < to.length; i++) {
        switch (to[i]) {
            case "zh": to[i] = "zh-cn"; break;
            case "jp": to[i] = "ja"; break;
            case "kor": to[i] = "ko"; break;
            case "fra": to[i] = "fr"; break;
            case "spa": to[i] = "es"; break;
            case "ara": to[i] = "ar"; break;
            case "bul": to[i] = "bg"; break;
            case "est": to[i] = "et"; break;
            case "dan": to[i] = "da"; break;
            case "fin": to[i] = "fi"; break;
            case "rom": to[i] = "ro"; break;
            case "slo": to[i] = "sl"; break;
            case "swe": to[i] = "sv"; break;
            case "vie": to[i] = "vi"; break;
            default: break;
        }
    }
    return to;
}

function trans_language_code_single(lan) {
    switch (lan) {
        case "zh": return "zh-cn";
        case "jp": return "ja";
        case "kor": return "ko";
        case "fra": return "fr";
        case "spa": return "es";
        case "ara": return "ar";
        case "bul": return "bg";
        case "est": return "et";
        case "dan": return "da";
        case "fin": return "fi";
        case "rom": return "ro";
        case "slo": return "sl";
        case "swe": return "sv";
        case "vie": return "vi";
        default: return lan;
    }
}

function getNation(nationStr) {
    var all_nations = [];
    var nations;

    $.ajaxSettings.async = false;
    $.getJSON("../data/capitalTable.json", function (data) {
        var nationsArr = data;
        for (var nation in nationsArr)
            all_nations.push(nation);
        //console.log(all_nations);
    });

    nations = nationStr.split(" ");
    for (var i = 0; i < nations.length; i++) {
        if ($.inArray(nations[i], all_nations) < 0 && nations[i] != "int") {
            remove(nations, i);
            i--;
        }
    }


    if (nations.length == 0)
        nations.push("all");
    return nations;
}

function remove(arr, i) {
    for (var j = i; j < arr.length - 1; j++)
        arr[j] = arr[j + 1];
    arr.pop();
}

function transLan(lanStr) {
    var lan = lanStr.substring(0, 2);
    return languages_table[lan] ? languages_table[lan] : lan;
}