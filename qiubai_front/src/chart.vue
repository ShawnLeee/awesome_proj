<template>
    <div id="main-container">
    </div>
</template>
<script>
import option from './chartdemo.js';
let echarts = require('echarts');
    export default{
        name: "chart",
        mounted(){
            let chart = echarts.init(document.getElementById('main-container'));
            chart.setOption(option);

        }
    }
</script>
<style lang="scss" scoped="true">
    #main-container
    {
        width: 400px;
        height: 400px;
    }
</style>