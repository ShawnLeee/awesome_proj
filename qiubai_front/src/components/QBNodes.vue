<template>
<div class="nodes-container">
    <router-link v-for="(module, index) in modules" :to="module.routeData" :key="index">
        <div :class="module.classValues">{{module.moduleName}}</div>
    </router-link>
</div>
</template>
<script>
import { modules } from '../config/module.config.js';
export default {
    data(){
        return{
            modules: modules,
        }
    }

}
</script>
<style>
.router-link-active .qb-node
{
    color: #f93;
    font-weight: 700;
}
.nodes-container
{
    padding: 10px 0;
    background: #fff;
    overflow: hidden;
}
.qb-node
{
    float: left;
    font-size: 18px;
    font-weight: 400;
    color: #514331;
    padding: 4px 0;
    width: 20%;
    height: 30px;
    line-height: 30px;
    text-align: center;
    background-image: url(../assets/images/colline.png);
    background-repeat: no-repeat;
    background-position: right center;
}
.endline
{
    background-image: none;
}
</style>