$('#login').click(function () {
    var username = $('#username').text();
    var password = $('#password').text();

    var url = 'http://10.48.41.24:9000/moh/user/login';

    $.ajax({
        async: true,
        url: url,
        type: 'post',
        contentType: 'application/x-www-form-urlencoded',
        dataType: 'json',
        data: [username, password],
        success: function (data) {
            console.log(data);
            if (data['code'] == 200) {
                window.location = 'html/main.html';
            }
            else {
                $('#error').html('<b>账号或密码错误</b>');
            }
        }
    });
});