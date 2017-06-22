/*jshint esversion: 6 */
import Posts from '../Posts.vue';
import PostDetail from '../PostDetail.vue';
import chart from '../chart.vue';
var routes=
[
        {
            path:'/',
            component: Posts,
        },
        {
            path:'/hot',
            component: Posts,
        },
        {
            path:'/24',
            component: Posts,
        },
        {
            path:'/post/:id',
            component: PostDetail,
        },
        {
            path: '/posts/:module',
            name: 'posts',
            component: Posts
        },
        {
            path: '/userList',
            component: chart
        }
];
export { routes };