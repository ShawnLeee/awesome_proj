function getParameterByName(name, url){
    if (!url) {
      url = window.location.href;
    }
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

function postDetail(articleid, callback){
    $.ajax({
        url:"http://127.0.0.1:8000/api/postdetail/",
        type:"GET",
        data:{articleid: articleid },
        contentType: "application/x-www-form-urlencoded; charset=utf-8",
        dataType: "json",
        success:function(data){
            callback(data);
        }
    });
}
function ArticleCell(cellData){
    author_data = cellData.author;
    var articleBox = $('<div>').addClass("article").addClass("block").addClass("mb15");
    var author = $('<div>').addClass("author").addClass("clearfix").appendTo(articleBox);
    var author_href = $('<a>').attr('href', author_data.avatar).attr('rel', 'nofollow').appendTo(author);
    $('<img>').attr("src",author_data.avatar).appendTo(author_href);
    $('<a>').attr("href", '#').text(author_data.username).appendTo(author);
    $('<div>').addClass("articleGender").addClass("womenIcon").text("99").appendTo(author);
    var artciel_detail = 'article.html' + '?articleid=' + cellData.post_id;

    var article_content = $("<div>").appendTo(articleBox);
    $('<a>').attr('href', artciel_detail).text(cellData.content).appendTo(article_content);
    if(cellData.img){
        $('<img>').attr("src", cellData.img).addClass("post-img").appendTo(article_content);
    }

    var stats = $("<div>").addClass("stats").appendTo(articleBox);
    var stats_vote = $('<span>').addClass("stats-vote").text("好笑").appendTo(stats);
    $('<i>').addClass("number").text(cellData.up_vote).appendTo(stats_vote);
    var stats_comments = $('<span>').addClass("stats-comments").appendTo(stats);
    $('<span>').addClass("dash").text(" . ").appendTo(stats_comments);
    var comment_href = $('<a>').attr("href","#").text("评论").appendTo(stats_comments);
    $('<i>').addClass("number").text(cellData.comment_count).appendTo(comment_href);

    var stats_buttons = $('<div>').addClass("stats-buttons").addClass("bar").appendTo(articleBox);
    var button_ul = $('<ul>').addClass("clearfix").appendTo(stats_buttons);

    var up_li = $('<li>').addClass("up").appendTo(button_ul);
    var up_a = $('<a>').attr('href', '#').appendTo(up_li);
    $('<i>').appendTo(up_a);

    var down_li = $('<li>').addClass("down").appendTo(button_ul);
    var down_a = $('<a>').attr('href', '#').appendTo(down_li);
    $('<i>').appendTo(down_a);

    var comments_li = $('<li>').addClass("comments").appendTo(button_ul);
    var comments_a = $('<a>').attr('href', '#').appendTo(comments_li);
    $('<i>').appendTo(comments_a);


    var single_share = $('<div>').addClass("single-share").appendTo(articleBox);
    var single_clear = $('<div>').addClass("single-clear").appendTo(articleBox);

    return articleBox;
}
function CommentCell(commentData){
    var commentBox = $("<div>").addClass("comment-block");
    var avatar = $("<div>").addClass("avatar").addClass("fleft").appendTo(commentBox);
    var avatarhref = $("<a>").appendTo(avatar);
    $("<img>").attr("src", commentData.user.avatar).appendTo(avatarhref);
    var reply = $("<div>").addClass("reply").addClass("fleft").appendTo(commentBox);
    $("<a>").text(commentData.user.username).addClass("fleft").appendTo(reply);
    var report = $("<div>").addClass("report").addClass("fright").text(commentData.floor).appendTo(reply);
    $("<div>").addClass("body").text(commentData.content).appendTo(reply);
    return commentBox;
}
