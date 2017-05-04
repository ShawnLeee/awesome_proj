<template>
<div class="article block mb15">
    <div class="author clearfix">
        <a :href="post.author.avatar" rel="nofollow"><img :src="post.author.avatar"></a>
        <a href="#">{{post.author.username}}</a>
        <div class="articleGender womenIcon">99</div>
    </div>
    <div>
        <!-- <a :href="postDetailUrl" :title="postDetailUrl">{{post.content}}</a> -->
        <!-- <hr> -->
        <router-link :to="postLink">{{post.content}}</router-link>
    </div>
    <div class="stats">
    <span class="stats-vote">好笑<i class="number">{{post.up_vote}}</i></span>
    <span class="stats-comments"><span class="dash"> . </span>
    <a href="#">评论<i class="number">{{post.comment_count}}</i></a></span>
    </div>
    <div class="stats-buttons bar">
        <ul class="clearfix">
            <li class="up"><a href="#"><i></i></a></li>
            <li class="down"><a href="#"><i></i></a></li>
            <li class="comments"><a href="#"><i></i></a></li>
        </ul>
    </div>
    <div class="single-share"></div>
    <div class="single-clear"></div>
</div>
</template>
<script>
    export default {
        name: "PostCell",
        props: ['post'],
        data(){
            return{
                postDetailUrl: '',
            }
        },
        computed:{
            postLink: function () {
                return '/post/' + this.post.post_id;
            }
        }

    }
</script>
<style lang="scss">
    // @import "./assets/css/bootstrap.min.css";
    @import "./assets/css/main.css";
    @import "./assets/css/index.css";

    $article-width : 100%;
    .article {
        width: $article-width;
        padding: 18px 10px;
        -webkit-box-sizing: border-box; /* Safari/Chrome, other WebKit */
        -moz-box-sizing: border-box;    /* Firefox, other Gecko */
        box-sizing: border-box;         /* Opera/IE 8+ */
    }
    .clearfix
    {
        clear: both;
        overflow: hidden;
    }
    .router-link-active
    {
        background: none;
    }
    li .router-link-active
    {
        background: #333;
    }
</style>