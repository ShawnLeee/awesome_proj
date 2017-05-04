function setupLogin(){

    var userToken = $.cookie('token');
    if(userToken != undefined){
        var token = 'Token ' + userToken;
        userMessage(token, function(userprofile){
            showUser(true, userprofile);
        });
    }else{
        showUser(false);
    }

    $("#logoutbtn").click(function(){
        //清除cookie
        $.removeCookie('token');
        $.removeCookie('isLogin');
        showUser(false);
        location.reload();

    });

    $(".signin-form").on("submit",function(e){
        e.preventDefault();
        var formArray = $("#login-form").serializeArray();
        var name = formArray[0].value;
        var password = formArray[1].value;

        login(name, password, function(data){
            if(data.status == '0'){
                //把获取到的token写入cookie
                var token = data.user.token;
                $.cookie('token', token, { expires: 7});
                $.cookie('isLogin', true);
                //隐藏登录框
                $("#myModal").modal('hide');
                //显示用户信息
                showUser(true,data.user);
            }else{
                alert(data.error_msg);
            }
        });
    });
}


function userMessage(userToken, callback){
    $.ajax({
            url: 'http://127.0.0.1:8000/api/usermsg/',
            type: 'GET',
            headers: {
                "Authorization": userToken,
            },
            contentType:"application/x-www-form-urlencoded; charset=utf-8",
            dataType:"json",
            success: function(data){
                callback(data);
            },
        });
}

function showUser(show, userprofile){
    if(show){
        $(".login").removeClass("hidden");
        $(".logout").addClass("hidden");
        $(".userimg>img").attr("src", userprofile.avatar);
        $(".username").text(userprofile.username);
    }else{
        $(".logout").removeClass("hidden");
        $(".login").addClass("hidden");
    }
}

function login(name, password, callback)
{
    $.post("http://127.0.0.1:8000/api/login/", 
        { username: name, password: password },
        function(data){
            callback(data);
        }
    );
}
function getUserToken(){
    var userToken = $.cookie('token');
    var token = 'Token ' + userToken;
    return  token;
}