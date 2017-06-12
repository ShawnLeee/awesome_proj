/*jshint esversion: 6 */
import Vue from 'vue';
import VueResource from 'vue-resource';
import VueRouter from 'vue-router';
import Mint from 'mint-ui';
import App from './App.vue';
import Posts from './Posts.vue';
import PostCell from './PostCell.vue';
import PostDetail from './PostDetail.vue';
import { routes }from './config/route.config.js';

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'

Vue.use(ElementUI)

Vue.use(VueResource);
Vue.use(VueRouter);
Vue.use(Mint);

const router = new VueRouter({
    routes:routes,
});

var app = new Vue({
    router,
    el: '#app',
    render: h => h(App),
});
