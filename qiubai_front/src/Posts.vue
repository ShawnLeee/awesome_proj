<template>
    <div class="main">
        <!-- <div class="content-left">
            <PostCell v-for="post in arrdata" v-bind:post="post" :key="post.post_id"></PostCell>
        </div> -->
        <mt-loadmore :bottom-method="loadBottom" ref="loadmore">
         <div class="content-left">
            <PostCell v-for="post in arrdata" v-bind:post="post" :key="post.post_id"></PostCell>
        </div>   
        </mt-loadmore>
    </div>
</template>

<script>
import { Loadmore } from 'mint-ui';
import Vue from 'vue';
import PostCell from './PostCell.vue';
import {getPosts as postsData, gethot , gethots} from './utils/Network.js';

Vue.component(Loadmore.name, Loadmore);

export default {
        props: ['currentModule'],
        data() {
            return {
                currentPage:0,
                page:{
                    currentPage: 0,
                    totalPages: 0,
                },
                module:'hot',
                arrdata: [],
            }
        },
        components: {
            PostCell: PostCell,
        },
        methods: {
            getPosts: function(page){
                gethots(page, function(res){
                    this.currentPage = page;
                    this.page.currentPage = res.current_page;
                    this.page.totalPages = res.total_pages;
                    res.posts.forEach(function(data){
                        this.arrdata.push(data);
                    }.bind(this))
                }.bind(this));
            },
            loadBottom(){//Load more data.

                if(this.page.currentPage < this.page.totalPages){
                    this.currentPage += 1;
                    gethots(this.currentPage,function(res){
                        console.log('load page ' + this.currentPage)
                        this.page.currentPage += 1;
                        res.posts.forEach(function(data){
                            this.arrdata.push(data);
                        }.bind(this))
                        this.$refs.loadmore.onBottomLoaded();
                    }.bind(this));
                }
            },
        },
        mounted: function(){
            this.getPosts(1);
        },
        updated: function(){
            // console.log(this.currentModule);
        },
        watch: {
            module: function(newValue, oldVale){
                console.log('About to load ' + newValue + '\'s data');
                // this.getPosts(2);
            }
        },
        beforeRouteUpdate(to, from, next){
            this.arrdata = []
            this.getPosts(1);
            this.module = to.params.module;
            next();
        },
}
</script>
<style>
    .main{
        width: 100%;
        margin: 0 auto;
        overflow: hidden;
    }
    .content-left
    {
        width: 100%;
        float: left;
        margin: 20px 20px 0 0;
    }
    .mint-loadmore-text
    {
        display: block;
        margin: auto;
        text-align: center;
    }
</style>