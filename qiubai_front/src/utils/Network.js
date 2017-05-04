/*jshint esversion: 6 */
import Vue from 'vue';

function getPosts(page=1,callback=null) {
    Vue.http.get('http://127.0.0.1:8000/api/posts/', {'page':page}).then(function(res){
        if(callback){
            callback(res);
        }
    });
}

function postDetail(postId, callback){
    let params = {
        params:{
            articleid: postId
        }
    };
    Vue.http.get('http://127.0.0.1:8000/api/postdetail/', params).then(function(res){
        console.log(postId);
        if(callback){
            callback(res);
        }
    });
}
function gethot(param){
    var page = param.page;
    var callback = param.callback;
    if (!page){
        page = 1;
    }
    Vue.http.get('http://127.0.0.1:8000/api/hotpost/',{page:page}).then(function(res){
        if(callback){
            callback(res);
        }
    });
}
function gethots(page, callback){
    var the_page = page;
    if (!the_page){
        the_page = 1;
    }
    Vue.http.get('http://127.0.0.1:8000/api/hotpost/',{page:the_page}).then(function(res){
        if(callback){
            callback(res.data);
        }
    });
}

export { getPosts , postDetail, gethot , gethots};