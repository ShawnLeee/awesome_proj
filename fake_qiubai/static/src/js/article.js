var currentPage = 0;
$(document).ready(function(){
    var navbar = new NavBar();
    $("#main-content").before(navbar);
    setupLogin();
    var articleId = getParameterByName('articleid');

    if(articleId){
        window.articleid = articleId;
        postDetail(articleId,function(articleData){
            var articleBox = new ArticleCell(articleData);
            $(".comments-wrap").before(articleBox);
            $("#comments-num").text("评论 " + "(" + articleData.comment_count + ")");
        });
    }
    loadArticeComments();
    setupComment();
    setupCommentPosition();
    setupLoadMoreComments();
});

function loadArticeComments(){
    loadreplies();
}

function loadreplies(params){
    if(!params){
        params = {articleid: window.articleid, page: window.currentPage + 1};
    }
    $.ajax({
        url: "http://127.0.0.1:8000/api/postreplies/",
        method: "GET",
        data: params,
        contentType: "application/x-www-form-urlencoded; charset=utf-8",
        dataType: "json",
        success: function(replydata){
            if(replydata.data.length == 0){
                return;
            }
            window.currentPage += 1;
            replydata.data.forEach(function(commentData){
                var commentCell = new CommentCell(commentData);
                commentCell.appendTo("#comment-list");
            });
            $("#comments-num").text("评论 " + "(" + replydata.reply_msg.total_reply + ")");
        }
    });
}

function setupLoadMoreComments(){
    $("#loadmore").click(function(e){
        loadreplies();
    });
}

function setupComment(){
    $(".comment-submit").click(function(e){
        e.preventDefault();
        var commentContent = $(".comment-area").val();
        comment(commentContent, function(data){
            location.reload();
        });
    });
}

function comment(commentContent, callback){
    userToken = $.cookie("token");
    authorizeToken = "Token " + userToken;
    $.ajax({
        url: "http://127.0.0.1:8000/api/reply/",
        method: "POST",
        headers: {Authorization: authorizeToken},
        data: {articleid: window.articleid, content:commentContent},
        contentType: "application/x-www-form-urlencoded; charset=utf-8",
        dataType: "json",
        success: function(data){
            callback(data);
        }
    });
}
function setupCommentPosition(){
    window.onscroll = function(){
        var commentWrap = $("#comment-wrap");
        var distanceToTop = $(commentWrap).offset().top;
        var toBottom = document.documentElement.clientHeight - distanceToTop;

    };
}

