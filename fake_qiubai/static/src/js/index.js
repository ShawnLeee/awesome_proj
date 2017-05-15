$(document).ready(function(){
    var navbar = new NavBar();
    $("#content").before(navbar);
    setupPage();
    // $("#firstpage").css("background", "#FFAB24");
    // $(".xpagination > li").each(function(i,item){
    //     $(item).click(function(){
    //         goto_page(this);
    //     });
    // });
});

function setupPage()
{
    window.currentPage = 0;
    setDropload();
    setupLogin();
}

function loadPosts(params, callback){
    $.ajax({
        // url:"http://127.0.0.1:8000/api/posts/",
        url:"http://127.0.0.1:8000/api/recent/",
        type:"GET",
        data:params,
        contentType: "application/x-www-form-urlencoded; charset=utf-8",
        dataType:"json",
        success: function(data){
            callback(data);
        }
    });
}
function setupPostsData(posts){
    posts.forEach(function(cellData){
        var articleBox = new ArticleCell(cellData);
        articleBox.appendTo("#col1");
    });
}
function loadNewData(newPage, callback){
    var params = {page: newPage};

    loadPosts(params, function(data){
        callback();
        if(data.length == 0){
            return;
        }
        setupPostsData(data.posts);
        currentPage = newPage;
    });
}

function setDropload(){
    $("body").dropload({
        scrollArea:window,
        loadDownFn: function(me){
            loadNewData(currentPage + 1, function(){
                me.resetload();
            });
        },
        loadUpFn: function(me){
            // me.resetload();
        }
    });
}


function goto_page(aDom){
    pageindex = parseInt(aDom.innerText);
    if (isNaN(pageindex))
    {
        return;
    }
    $(".xpagination > li").each(function(i,item){
        pagenum = parseInt(item.innerText);
        if(pagenum == pageindex){
            $(item).css("background", "#FFAB24");
        }else{
            $(item).css("background", "#fff");
        }
    });
    pageurl = "http://127.0.0.1:8000/api/posts/" + "?page=" + pageindex;
    $.get(pageurl, function(data){
        if(data.length > 0){
            $('.article').remove();

            data.forEach(function(cellData){
                var articleBox = new ArticleCell(cellData);
                articleBox.appendTo("#col1");
            });
            scroll(0,0);
        }
    });

}

