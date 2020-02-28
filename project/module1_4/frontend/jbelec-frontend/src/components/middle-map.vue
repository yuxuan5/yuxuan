<template>
    <div>
<div class="chart" id="mapChart"></div>
    </div>
</template>
<script>
    import geoJson from '@/assets/Echarts/NBmap.json'

export default{
    data() {
            return {

            }
            },

    methods:{
        drawMapChart(){
             //初始化echarts实例

             this.$echarts.registerMap('NBmap', geoJson,{})
             var myChart = this.$echarts.init(document.getElementById('mapChart'));
             var option = {

                 tooltip: {
                     trigger: 'item'
                 },

                 series: [
                     {
                     	name: '北京河北五市',
                         type: 'map',
                         mapType: 'NBmap',
                         aspectScale: 0.85,  //地图长度比
                         label: {
                             normal: {
                                 show: true,
                                 textStyle: {
                                     color: '#fff'
                                 }
                             },
                             emphasis: {
                                 show: true,
                                 textStyle: {
                                     color: '#fff'
                                 }
                             }
                         },
                         itemStyle: {
                             normal: {
                                 areaColor: 'transparent',
                                 borderColor: '#3fdaff',
                                 borderWidth: 2,
                                 shadowColor: 'rgba(63, 218, 255, 0.5)',
                                 shadowBlur: 30
                             },
                             emphasis: {
                                 areaColor: '#2B91B7',
                                 color: '#fff'
                             }
                         },
                         data: []
                     }
                 ],
             };

             myChart.setOption(option);
      }
    },
    mounted(){
      this.drawMapChart();
    }
}
</script>
<style>
.chart{
    height:500px;
}</style>
