<template>
  <div id="app">
    <qbheader></qbheader>
    <router-view :currentModule="currentModule"></router-view>
  </div>
</template>

<script>
import NavBar from './Navbar.vue';
import Posts from './Posts.vue';
import { modules } from './config/module.config.js';
import QBHeader from './components/Header.vue';
export default {
  name: 'app',
  data () {
    return {
        currentModule:'hotttttt',
        modules: modules,
    }
  },
  components:{
    navbar: NavBar,
    posts: Posts,
    qbheader: QBHeader
  },
  mounted:function(){
  }
}
</script>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  // margin-top: 60px;
}
body, h1, h2
{
    margin: 0;
    padding: 0;
}
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
div, ul {
    text-align: left;
}
</style>
