<template>
    <section class="chart-container">
        <el-row class="chart-container1">
            <el-col :span="24">
                <div id="hh" class="chart"></div>
            </el-col>
        </el-row>
        <el-row class="chart-container2">
            <el-col :span="6">
                <div id="box-plot" class="chart"></div>
            </el-col>
            <el-col :span="16">
                <div id="series-pie" class="chart"></div>
            </el-col>
            <el-col :span="2">
                <div id="bar" class="chart"></div>
            </el-col>
        </el-row>
    </section>
</template>

<script>
    import { mapState, mapActions } from 'vuex'
    import ECharts from 'echarts'
    import { boxPlotOption, seriesPieOption, barOption } from '../config/userchartoption'

    export default {
        data() {
            return {
                boxPlotChart: null,
                boxPlotOption: boxPlotOption,
                seriesPieChart: null,
                seriesPieOption: seriesPieOption,
                barChart: null,
                barOption: barOption
            }
        },
        computed: {
            ...mapState([
                'analyzeMethod',
                'clusterResult'
            ])
        },
        watch: {
            clusterResult: function (val) {
                console.log(val);
                let boxData = [];
                for (let i = 0; i < val.length; i++) {
                    boxData.push(val[i].box);
                }
                console.log(boxData);
                let pieData = [];
                for (let i = 0; i < val.length; i++) {
                    pieData.push(val[i].series);
                }
                console.log(pieData);
                let barData = []; // [3, 7, 4, 6, 2, 8];
                for (let i = 0; i < val.length; i++) {
                    barData.push(val[i].num);
                }
                console.log(barData);
                this.setBoxPlotSeriesData(boxData);
                this.setPieData(pieData);
                this.setBarSeriesData(barData);
                // this.setPieSeriesData();
            }
        },
        methods: {
            renderChart() {
                this.boxPlotChart = ECharts.init(document.getElementById('box-plot'));
                this.seriesPieChart = ECharts.init(document.getElementById('series-pie'));
                this.barChart = ECharts.init(document.getElementById('bar'));
                this.boxPlotChart.setOption(this.boxPlotOption);
                this.seriesPieChart.setOption(this.seriesPieOption);
                this.barChart.setOption(this.barOption);
            },
            setBoxPlotSeriesData(data) {
                this.boxPlotChart.setOption({
                    series: {
                        data: data
                    }
                });
            },
            setPieData(data) {
                let pieSeries = [];
                for (let i = 0; i < data.length; i++) {
                    let cluster_i = data[i];
                    for (let j = 0; j < 12; j++) {
                        let month_j = cluster_i[j];
                        let center = this.seriesPieChart.convertToPixel({
                            xAxisIndex: 0,
                            yAxisIndex: 0
                        }, [j, i]);
                        let dayOfConsum = month_j['unused'];
                        pieSeries.push({
                            type: 'pie',
                            center: center,
                            label: {
                                normal: {
                                    show: false
                                }
                            },
                            radius: month_j.total/1600000,
                            data: [{
                                name: '峰',
                                value: month_j.eq1,
                                itemStyle: {
                                    normal: {
                                        color: 'yellow'
                                    }
                                }
                            }, {
                                name: '平',
                                value: month_j.eq2,
                                itemStyle: {
                                    normal: {
                                        color: 'skyblue'
                                    }
                                }
                            }, {
                                name: '尖',
                                value: month_j.eq3,
                                itemStyle: {
                                    normal: {
                                        color: 'orange'
                                    }
                                }
                            }, {
                                name: '谷',
                                value: month_j.eq3,
                                itemStyle: {
                                    normal: {
                                        color: 'green'
                                    }
                                }
                            }]
                        }, {
                            type: 'pie',
                            center: center,
                            label: {
                                normal: {
                                    show: false
                                }
                            },
                            radius: [10, 12],
                            data: [{
                                name: '工作',
                                value: 30-dayOfConsum,
                                itemStyle: {
                                    normal: {
                                        color: '#888888'
                                    }
                                }
                            }, {
                                name: '休息',
                                value: dayOfConsum,
                                itemStyle: {
                                    normal: {
                                        color: '#dddddd'
                                    }
                                }
                            }]
                        });
                    }
                }
                this.seriesPieOption.series = pieSeries;
                this.seriesPieChart.setOption(this.seriesPieOption);
                /*
                this.seriesPieChart.setOption({
                    series: pieSeries // [...heatSeries, ...pieSeries]
                }, true);
                */
            },
            setPieSeriesData() {
                let heatData = [];
                let monthHeatColor = [
                    {normal: {color: {type: 'linear', x: 0, x2: 1, colorStops: [{offset: 0, color: 'rgba(255, 58, 0, 0.1)'}, {offset: 0.5, color: 'rgba(255, 0, 0, 0.1)'}, {offset: 1, color: 'rgba(255, 55, 0, 0.1)'}]}}},
                    {normal: {color: {type: 'linear', x: 0, x2: 1, colorStops: [{offset: 0, color: 'rgba(255, 55, 0, 0.1)'}, {offset: 0.5, color: 'rgba(255, 112, 0, 0.1)'}, {offset: 1, color: 'rgba(255, 166, 0, 0.1)'}]}}},
                    {normal: {color: {type: 'linear', x: 0, x2: 1, colorStops: [{offset: 0, color: 'rgba(255, 166, 0, 0.1)'}, {offset: 0.5, color: 'rgba(255, 224, 0, 0.1)'}, {offset: 1, color: 'rgba(240, 238, 0, 0.1)'}]}}},
                    {normal: {color: {type: 'linear', x: 0, x2: 1, colorStops: [{offset: 0, color: 'rgba(240, 238, 0, 0.1)'}, {offset: 0.5, color: 'rgba(224, 253, 0, 0.1)'}, {offset: 1, color: 'rgba(170, 225, 0, 0.1)'}]}}},
                    {normal: {color: {type: 'linear', x: 0, x2: 1, colorStops: [{offset: 0, color: 'rgba(170, 225, 0, 0.1)'}, {offset: 0.5, color: 'rgba(112, 196, 0, 0.1)'}, {offset: 1, color: 'rgba(184, 210, 0, 0.1)'}]}}},
                    {normal: {color: {type: 'linear', x: 0, x2: 1, colorStops: [{offset: 0, color: 'rgba(184, 210, 0, 0.1)'}, {offset: 0.5, color: 'rgba(255, 224, 0, 0.1)'}, {offset: 1, color: 'rgba(255, 170, 0, 0.1)'}]}}},
                    {normal: {color: {type: 'linear', x: 0, x2: 1, colorStops: [{offset: 0, color: 'rgba(255, 170, 0, 0.1)'}, {offset: 0.5, color: 'rgba(255, 112, 0, 0.1)'}, {offset: 1, color: 'rgba(255, 58, 0, 0.1)'}]}}},
                    {normal: {color: {type: 'linear', x: 0, x2: 1, colorStops: [{offset: 0, color: 'rgba(255, 58, 0, 0.1)'}, {offset: 0.5, color: 'rgba(255, 0, 0, 0.1)'}, {offset: 1, color: 'rgba(255, 54, 0, 0.1)'}]}}},
                    {normal: {color: {type: 'linear', x: 0, x2: 1, colorStops: [{offset: 0, color: 'rgba(255, 54, 0, 0.1)'}, {offset: 0.5, color: 'rgba(255, 112, 0, 0.1)'}, {offset: 1, color: 'rgba(255, 166, 0, 0.1)'}]}}},
                    {normal: {color: {type: 'linear', x: 0, x2: 1, colorStops: [{offset: 0, color: 'rgba(255, 166, 0, 0.1)'}, {offset: 0.5, color: 'rgba(255, 224, 0, 0.1)'}, {offset: 1, color: 'rgba(240, 238, 0, 0.1)'}]}}},
                    {normal: {color: {type: 'linear', x: 0, x2: 1, colorStops: [{offset: 0, color: 'rgba(240, 238, 0, 0.1)'}, {offset: 0.5, color: 'rgba(224, 253, 0, 0.1)'}, {offset: 1, color: 'rgba(239, 186, 0, 0.1)'}]}}},
                    {normal: {color: {type: 'linear', x: 0, x2: 1, colorStops: [{offset: 0, color: 'rgba(239, 186, 0, 0.1)'}, {offset: 0.5, color: 'rgba(255, 112, 0, 0.1)'}, {offset: 1, color: 'rgba(255, 58, 0, 0.1)'}]}}}
                ];
                for (let i = 0; i < 12; i++) {
                    for (let j = 0; j < 6; j++) {
                        heatData.push({value: [i, j, 1], itemStyle: monthHeatColor[i]});
                    }
                }
                let heatSeries = [{
                    name: 'series-pie',
                    type: 'heatmap',
                    coordinateSystem: 'cartesian2d',
                    blurSize: 6,
                    data: heatData
                }];

                let pieSeries = [];
                let userClassWeight = [{
                    // 空置房
                    all: 1, peak: 1, ave: 1, extreme: 1, valley: 1,
                    monthWeight: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    cyclical: [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
                }, {
                    // 正常低用电量用户
                    all: 3, peak: 1, ave: 1, extreme: 1, valley: 3,
                    monthWeight: [3, 2, 1, 1, 1, 2, 2.5, 3, 1, 1, 2, 2.5],
                    cyclical: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                }, {
                    // 正常高用电量用户
                    all: 4, peak: 1, ave: 1, extreme: 1, valley: 3,
                    monthWeight: [3, 2, 1, 1, 1, 2, 2.5, 3, 1, 1, 2, 2.5],
                    cyclical: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                }, {
                    // 春节回家
                    all: 3, peak: 1, ave: 1, extreme: 1, valley: 3,
                    monthWeight: [3, 2, 1, 1, 1, 2, 2.5, 3, 1, 1, 2, 2.5],
                    cyclical: [1, 0.3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                }, {
                    // 全年无波动，且用电量大
                    all: 4, peak: 4, ave: 3, extreme: 4, valley: 3,
                    monthWeight: [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                    cyclical: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                }, {
                    // 全年无波动，用电量小
                    all: 2, peak: 4, ave: 3, extreme: 4, valley: 1,
                    monthWeight: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    cyclical: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                }];
                for (let i = 0; i < 6; i++) {
                    let userWeight = userClassWeight[i];
                    for (let j = 0; j < 12; j++) {
                        let center = this.seriesPieChart.convertToPixel({
                            xAxisIndex: 0,
                            yAxisIndex: 0
                        }, [j, i]);
                        let dayOfConsum = userWeight.cyclical[j] * 30;
                        pieSeries.push({
                            type: 'pie',
                            center: center,
                            label: {
                                normal: {
                                    show: false
                                }
                            },
                            radius: userWeight.all * userWeight.monthWeight[j],
                            data: [{
                                name: '峰',
                                value: Math.round(userWeight.peak * userWeight.monthWeight[j]),
                                itemStyle: {
                                    normal: {
                                        color: 'yellow'
                                    }
                                }
                            }, {
                                name: '平',
                                value: Math.round(userWeight.ave * userWeight.monthWeight[j]),
                                itemStyle: {
                                    normal: {
                                        color: 'skyblue'
                                    }
                                }
                            }, {
                                name: '尖',
                                value: Math.round(userWeight.extreme * userWeight.monthWeight[j]),
                                itemStyle: {
                                    normal: {
                                        color: 'orange'
                                    }
                                }
                            }, {
                                name: '谷',
                                value: Math.round(userWeight.valley * userWeight.monthWeight[j]),
                                itemStyle: {
                                    normal: {
                                        color: 'green'
                                    }
                                }
                            }]
                        }, {
                            type: 'pie',
                            center: center,
                            label: {
                                normal: {
                                    show: false
                                }
                            },
                            radius: [10, 12],
                            data: [{
                                name: '工作',
                                value: dayOfConsum,
                                itemStyle: {
                                    normal: {
                                        color: '#888888'
                                    }
                                }
                            }, {
                                name: '休息',
                                value: 30-dayOfConsum,
                                itemStyle: {
                                    normal: {
                                        color: '#dddddd'
                                    }
                                }
                            }]
                        });
                    }
                }
                this.seriesPieChart.setOption({
                    series: pieSeries // [...heatSeries, ...pieSeries]
                });
            },
            setBarSeriesData(data) {
                this.barChart.setOption({
                    xAxis: {
                        max: Math.max(data),
                    },
                    series: {
                        data: data
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

        /*.chart {
            width: 100%;
            height: 500px;
        }*/
    }
</style>