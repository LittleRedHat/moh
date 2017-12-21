$('#login').click(function () {
    var username = $('#username').val();
    var password = $('#password').val();

    var url = 'http://47.97.96.152/api/moh/user/login';

    $.ajax({
        url: url,
        type: 'post',
        contentType: 'application/x-www-form-urlencoded',
        dataType: 'json',
        data:{
            username:username,
            password:password,
        },
        success: function (data) {
            console.log(data);
            if (data['code'] == 200) {
                window.sessionStorage.setItem('user',data['user']['id'])
                window.location = 'html/main.html';
            }
            else {
                $('#error').html('<b>账号或密码错误</b>');
            }
        }
    });
});