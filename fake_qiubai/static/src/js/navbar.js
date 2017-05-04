function NavBar(){
    // var navbar2 = $("<div> <div class=\"modal fade\" id=\"myModal\" tabindex=\"-1\" role=\"dialog\" aria-labelledby=\"myModalLabel\"> <div class=\"modal-dialog\" role=\"document\"> <div class=\"modal-content\"> <div class=\"modal-body\"> <div id=\"modelBody\"> <div class=\"signin-account\"> <h4 id=\"account-header\">社交账号登录</h4> <div class=\"accountlogin\"><a href=\"\" class=\"account-weixin\">使用 微信 账号</a> </div> <div class=\"accountlogin\"><a href=\"\" class=\"account-weibo\">使用 微博 账号</a></div> <div class=\"accountlogin\"><a href=\"\" class=\"account-QQ\">使用 QQ 账号</a></div> </div> <div class=\"signin-form\"> <h4 id=\"login-header\">糗事百科账号登录</h4> <form action=\"\" id=\"login-form\"> <div class=\"signin-action\"> <input id=\"login\" class=\"form-input\" type=\"text\" name=\"name\" placeholder=\"昵称或邮箱\"> <input id=\"password\" class=\"form-input\" type=\"password\" name=\"passsword\" placeholder=\"密码\"> </div> <button type=\"submit\" class=\"form-submit\">登录</button> </form> </div> <div class=\"signin-footer\"></div> </div> </div> </div> </div> </div> <div class=\"navbar navbar-default head navbar-fixed-top\"> <div class=\"container-fluid\"> <div class=\"header\"> <div class=\"content-block\"> <div id=\"hd_log\" class=\"logo\"> <a href=\"/\"> <h1>糗事百科</h1> </a> </div> <div id=\"menu\" class=\"menu menu-bar\"> <a href=\"\\\">热门</a> <a href=\"\\\">24小时</a> <a href=\"\\\">热图</a> <a href=\"\\\">穿越</a> <a href=\"\\\">糗图</a> <a href=\"\\\">新鲜</a> <a href=\"test.html\">投稿</a> </div> <div class=\"userbar\" rel=\"nofollow\"> <div class=\"login hidden\"> <a id=\"logoutbtn\" class=\"fright\">登出</a> <a class=\"username fright\" href=\"\">我是谁</a> <a class=\"userimg fright\" href=\"\"><img src=\"http://pic.qiushibaike.com/system/avtnew/3276/32765046/medium/2017032423042351.JPEG\" alt=\"\"></a> </div> <div class=\"logout hidden\"> <a id=\"logintop\" rel=\"nofollow\" href=\"javascript:void(0);\" data-toggle=\"modal\" data-target=\"#myModal\">登录</a> <button id=\"registerbtn\" data-target=\"#myModal\" data-toggle=\"modal\" >注册</button></div> </div> </div> </div> </div> </div> </div>");
    var navbar = $("<div>");
    var loginModal = $("<div>").addClass("modal").addClass("fade").attr({
        "id": "myModal",
        "tabindex": "-1",
        "role": "dialog",
        "aria-labelledby": "myModalLabel",
    }).appendTo(navbar);
    var modalDialog = $("<div>").addClass("modal-dialog").attr("role", "document").appendTo(loginModal);
    var modalContent = $("<div>").addClass("modal-content").appendTo(modalDialog);
    var modalBody = $("<div>").addClass("modal-body").appendTo(modalContent);
    var body = $("<div>").attr("id", "modelBody").appendTo(modalBody);

    var accountlogin = $("<div>").addClass("signin-account").appendTo(body);
    $("<h4>").attr("id", "account-header").text("社交账号登录").appendTo(accountlogin);
    var weixin = $("<div>").addClass("accountlogin").appendTo(accountlogin);
    $("<a>").addClass("account-weixin").text("使用 微信 账号").appendTo(weixin);
    var weibo = $("<div>").addClass("accountlogin").appendTo(accountlogin);
    $("<a>").addClass("account-weibo").text("使用 微博 账号").appendTo(weibo);
    var qq = $("<div>").addClass("accountlogin").appendTo(accountlogin);
    $("<a>").addClass("account-QQ").text("使用 QQ 账号").appendTo(qq);

    var signinForm = $("<div>").addClass("signin-form").appendTo(body);
    $("<h4>").attr("id", "login-header").text("糗事百科账号登录").appendTo(signinForm);
    var form = $("<form>").attr("id", "login-form").appendTo(signinForm);
    var formbody = $("<div>").addClass("signin-action").appendTo(form);
    $("<input>").attr({"id": "login",
                       "class": "form-input",
                       "type": "text",
                       "name": "name",
                       "placeholder": "昵称或邮箱"}).appendTo(formbody);
    $("<input>").attr({"id": "password",
                       "class": "form-input",
                       "type": "password",
                       "name": "password",
                       "placeholder": "密码"}).appendTo(formbody);
    $("<button>").attr({"type": "submit", "class" : "form-submit"}).text("登录").appendTo(form);

    var signinFooter = $("<div>").appendTo(body);

    //Header

    var header = $("<div>").attr("class", "navbar navbar-default head navbar-fixed-top").appendTo(navbar);
    var headContainer = $("<div>").addClass("container-fluid").appendTo(header);
    var headerContent = $("<div>").addClass("header").appendTo(headContainer);
    var headerContentBlock = $("<div>").addClass("content-block").appendTo(headerContent);
    var logo = $("<div>").attr({"id": "hd_log", "class": "logo"}).appendTo(headerContentBlock);
    var logohref = $("<a>").attr("href", "/").appendTo(logo);
    $("<h1>").text("糗事百科").appendTo(logohref);

    var menu = $("<div>").attr({"id": "menu", "class": "menu menu-bar"}).appendTo(headerContentBlock);
    $("<a>").attr("href", "/").text("热门").appendTo(menu);
    $("<a>").attr("href", "/").text("24小时").appendTo(menu);
    $("<a>").attr("href", "/").text("热图").appendTo(menu);
    $("<a>").attr("href", "/").text("穿越").appendTo(menu);
    $("<a>").attr("href", "/").text("糗图").appendTo(menu);
    $("<a>").attr("href", "/").text("新鲜").appendTo(menu);
    $("<a>").attr("href", "newpost.html").text("投稿").appendTo(menu);
    var userbar = $("<div>").attr({"class": "userbar", "rel": "nofollow"}).appendTo(headerContentBlock);

    var loginbar = $("<div>").addClass("login").appendTo(userbar);
    $("<a>").attr({"id": "logoutbtn", "class": "fright"}).text("登出").appendTo(loginbar);
    $("<a>").attr("class","username fright").appendTo(loginbar);
    var userhref = $("<a>").attr("class", "userimg fright").appendTo(loginbar);
    $("<img>").appendTo(userhref);

    var logoutbar = $("<div>").addClass("logout").appendTo(userbar);
    var lastloginbtn = $("<a>").attr({"id": "logintop",
                                      "rel": "nofollow",
                                      "href": "javascript:void(0);",
                                      "data-toggle": "modal",
                                      "data-target": "#myModal"}).text("登录").appendTo(logoutbar);
    $("<button>").attr({"id": "registerbtn",
                        "data-toggle": "modal",
                        "data-target": "#myModal"}).text("注册").appendTo(logoutbar);

    return navbar ;
}
