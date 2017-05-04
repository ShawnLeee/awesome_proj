<template>
<div>
    <h1>{{id}}</h1>
    <PostCell :post="post" v-if="ready"></PostCell>
</div>
</template>

<script>
import { postDetail } from './utils/Network.js';
import PostCell from './PostCell.vue';
export default {
    data() {
        return {
            id:'',
            ready:false,
            post:{},
        }
    },
    components:{
        PostCell: PostCell,
    },
    methods:{
        loadPostDetail: function(postId){
            this.id = postId;
            var post = this.post;
            let params = { params:{ articleid: postId} };
            this.$http.get('http://127.0.0.1:8000/api/postdetail/', params).then(function(res){
                this.post = res.data;
                this.ready = true;
            }).bind(this);
        }
    },
    mounted: function () {
        let postId = this.$route.params.id;
        this.loadPostDetail(postId);
    }
}
</script>
<style>
    
</style>