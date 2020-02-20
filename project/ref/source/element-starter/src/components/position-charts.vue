<template>
    <section class="chart-container">
        <el-row class="chart-container1">
            <el-col :span="24">
                <div id="multi-pie" class="chart"></div>
            </el-col>
        </el-row>
        <el-row class="chart-container2">
            <el-col :span="8">
                <div id="box-plot1" class="chart"></div>
            </el-col>
            <el-col :span="8">
                <div id="box-plot2" class="chart"></div>
            </el-col>
            <el-col :span="8">
                <div id="box-plot3" class="chart"></div>
            </el-col>
        </el-row>
    </section>
</template>

<script>
    import { mapState, mapActions } from 'vuex'
    import ECharts from 'echarts'
    import { multiPieOption, boxPlotOption1, boxPlotOption2, boxPlotOption3 } from '../config/posconfig'

    export default {
        data() {
            return {
                multiPieChart: null,
                multiPieOption: multiPieOption,
                boxPlotChart1: null,
                boxPlotOption1: boxPlotOption1,
                boxData1: [],
                boxPlotChart2: null,
                boxPlotOption2: boxPlotOption2,
                boxData2: [],
                boxPlotChart3: null,
                boxPlotOption3: boxPlotOption3,
                boxData3: []
            }
        },
        computed: {
            ...mapState([
                'userType',
                'searchUser',
                'searchUserResult',
            ])
        },
        watch: {
            searchUser: function () {
                let result = this.searchUserResult;
                let multiPieData = result.type_dist;  // {highV: 10, lowV: 10, resident: 10};
                let boxPlotData = result.type_box;  // {highV: [1, 2, 3, 4, 5], lowV: [1, 2, 3, 4, 5], resident: [1, 2, 3, 4, 5]};
                this.setMultiPieData(multiPieData);
                this.setBoxPlotData(boxPlotData);
            }
        },
        methods: {
            renderChart() {
                this.multiPieChart = ECharts.init(document.getElementById('multi-pie'));
                this.boxPlotChart1 = ECharts.init(document.getElementById('box-plot1'));
                this.boxPlotChart2 = ECharts.init(document.getElementById('box-plot2'));
                this.boxPlotChart3 = ECharts.init(document.getElementById('box-plot3'));
                this.multiPieChart.setOption(this.multiPieOption);
                this.boxPlotChart1.setOption(this.boxPlotOption1);
                this.boxPlotChart2.setOption(this.boxPlotOption2);
                this.boxPlotChart3.setOption(this.boxPlotOption3);
            },
            setMultiPieData(data) {
                let currentSeries = this.multiPieChart.getOption().series;
                let length = currentSeries.length;
                console.log(length);
                currentSeries.push(
                    {
                        type:'pie',
                        radius : 50,
                        center : [(2*length+1)*10+'%', '50%'],
                        // roseType : 'area',
                        label: {
                            normal: {
                                show: false
                            },
                            emphasis: {
                                show: true
                            }
                        },
                        labelLine: {
                            normal: {
                                show: false
                            },
                            emphasis: {
                                show: true
                            }
                        },
                        data:[
                            {value: data.highV, name:'高压用户'},
                            {value: data.lowV, name:'低压非居民用户'},
                            {value: data.resident, name:'居民用户'}
                        ]
                    }
                );
                this.multiPieChart.setOption({
                    series: currentSeries
                });
            },
            setBoxPlotData: function (data) {
                /*console.log(data);
                let seriesData = this.boxPlotChart1.getOption().series; // [0].data;
                console.log(seriesData);*/
                this.boxData1.push(data.highV);
                this.boxData2.push(data.lowV);
                this.boxData3.push(data.resident);

                this.boxPlotChart1.setOption({
                    series: {
                        data: this.boxData1
                    }
                });
                this.boxPlotChart2.setOption({
                    series: {
                        data: this.boxData2
                    }
                });
                this.boxPlotChart3.setOption({
                    series: {
                        data: this.boxData3
                    }
                });
            }
        },
        mounted: function () {
            this.renderChart();
        }
    }
</script>

<style scoped lang="scss">
    .chart-container {
        width: 100%;
        height: 100%;
        float: left;

        .chart-container1 {
            height: 30%;
            border: 1px solid;
            .el-col {
                width: 100%;
                height: 100%;
                .chart {
                    width: 100%;
                    height: 100%;
                    margin: 0 auto;
                }
            }
        }
        .chart-container2 {
            height: 70%;
            border: 1px solid;
            .el-col {
                height: 100%;
                .chart {
                    width: 100%;
                    height: 100%;
                    margin: 0 auto;
                }
            }
        }
    }
</style>