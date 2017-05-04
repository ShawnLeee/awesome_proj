<template>
<div>
<mt-header fixed title="">
    <router-link to="/hot" slot="left">
        <mt-button class="header-btn">
            <img src="../assets/images/logo-new-0410.png" width="auto" height="33">
        </mt-button>
    </router-link>


    <router-link class="fright" to="/more" slot="left">
        <mt-button class='add-btn'>
        <div class="icon-more icon-qiushi"></div>
        </mt-button>
    </router-link>

    <router-link class="fright" to="/add" slot="left">
        <mt-button class='add-btn'>
            <div class="icon-add icon-qiushi"></div>
        </mt-button>
    </router-link>
</mt-header>
<qb-nodes></qb-nodes>
</div>
</template>
<script>

import { Header, Button } from 'mint-ui';
import Vue from 'vue';
import QBNodes from './QBNodes.vue';

Vue.component(Header.name, Header);
Vue.component(Button.name, Button);
Vue.component('qb-nodes', QBNodes);

export default {
}
</script>
<style>
.mint-header
{
    background: #FFBB27;
}
.header-btn
{
    padding-left: 10px;
}
.icon-qiushi
{
    margin: 4px;
    background-size: 150px;
    background-image: url(../assets/images/qiushi_iphone.png);
    background-repeat: no-repeat;
    border-style: none;
    border-width: 0;
    width: 24px;
    height: 24px;
}
.icon-more
{
    background-position: 0 0;
}
.icon-add
{
    background-position: -24px 0;
}
.add-btn
{
    text-decoration: none;
}
img[src=""]
{
    /*opacity: 0;*/
    overflow: hidden;
    border: 0;
    vertical-align: middle;
}
.fright
{
    float: right;
}
a
{
    text-decoration: none;
}
</style>
