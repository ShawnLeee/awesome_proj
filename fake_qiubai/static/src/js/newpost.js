$(document).ready(function(){
    var navbar = new NavBar();
    $("#content").before(navbar);
    setupLogin();
    setupPost();
});

function setupPost(){
    var userToken = getUserToken();
    $("#postbtn").click(function(){
        var content = $("#post-text").val();
        var picfile = $("#postpicture").prop("files")[0];
        var formdata = new FormData();
        formdata.append('pic', picfile);
        formdata.append('content', content);

        $.ajax({
            url: "http://127.0.0.1:8000/api/post/create/",
            type: "POST",
            cache: false,
            data: formdata,
            headers: {
                "Authorization": userToken,
            },
            contentType: false,
            processData: false,
            dataType: "json",
            success: function(data){
                if(data.status == 0){
                    location.href = "/";
                }
            }
        });
    });
}