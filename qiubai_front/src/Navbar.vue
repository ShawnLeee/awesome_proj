<template>
<div>
<ol>
<!-- <li><router-link :to="{name:'posts', params: {module:'hot'}}">热门</router-link></li>-->
<li v-for="module in modules"><router-link :to="module.routeData">{{module.moduleName}}</router-link></li>
</ol>
</div>
</template>
<script>

import Vue from 'vue';
    export default{
        name: "NavBar",
        data() {
            return{
                msg: "Hello Vue",
            }
        },
        props: ['modules']
    }
</script>
<style>
    ol
    {
        /*background: green;*/
        width: 600px;
    }
    .router-link-active
    {
        background: #333;
    }
</style>