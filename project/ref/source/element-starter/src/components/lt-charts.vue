<template>
    <!-- section class="chart-container" -->
        <el-row class="chart-container">
            <el-col :span="24" class="chart-container2">
                <div id="rankChart" class="chart"></div>
            </el-col>
            <el-col :span="24" class="chart-container2">
                <div id="curveChart" class="chart"></div>
            </el-col>
        </el-row>
    <!--/section-->
</template>

<script>
    import ECharts from 'echarts'
    import { mapState, mapActions } from 'vuex'
    import _ from 'underscore'
    import { getTopTqData, getTgEq } from '../api/api'
    import { rankChartOption, curveChartOption } from '../config/ltchartoption'

    export default {
        name: 'lt-charts',
        data() {
            return {
                title: 'lt-charts',
                rankChart: null,
                rankChartOption: rankChartOption,
                curveChart: null,
                curveChartOption: curveChartOption,
                currentType: null
            };
        },
        computed: {
            ...mapState([
                'searchLine',
                'searchLineResult',
                'searchTg',
                'searchTgResult',
                'searchUser',
                'searchUserResult',
                'tgEqs',
                'clustering'
            ])
        },
        watch: {
            searchLine: function () {
                this.currentType = 'tg';
                let rankData = this.searchLineResult.rank_data;
                let curveData = this.searchLineResult.tg_eq_curve;
                let barData = [];
                for (let i = 0; i < rankData.bar_data.length; i++) {
                    barData.push({
                        name: rankData.tgno[i],
                        value: rankData.bar_data[i]
                    });
                }
                let rankOption = {
                    title: {
                        text: 'Top台区用电量'
                    },
                    xAxis: {
                        data: rankData.category_data
                    },
                    series: {
                        id: 'bar',
                        data: barData  // rankData.bar_data
                    }
                };
                let curveOption = {
                    series: {
                        id: 'line',
                        data: curveData[0]
                    }
                };
                this.rankChart.setOption(rankOption);
                this.curveChart.setOption(curveOption);
            },
            searchTg: function () {
                this.currentType = 'user';
                let rankData = this.searchTgResult.rank_data;
                let curveData = this.searchTgResult.user_eq_curve;
                console.log(curveData);
                let rankOption = {
                    title: {
                        text: 'Top用户用电量'
                    },
                    xAxis: {
                        data: rankData.category_data
                    },
                    series: {
                        id: 'bar',
                        data: rankData.bar_data
                    }
                };
                let curveOption = {
                    series: {
                        id: 'line',
                        data: curveData
                    }
                };
                this.rankChart.setOption(rankOption);
                this.curveChart.setOption(curveOption);
            },
            searchUser: function () {
                let rankData = this.searchUserResult.rank_data;
                let curveData = this.searchUserResult.user_eq_curve;
                let rankOption = {
                    xAxis: {
                        data: rankData.category_data
                    },
                    series: {
                        id: 'bar',
                        data: rankData.bar_data
                    }
                };
                let curveOption = {
                    series: {
                        id: 'line',
                        data: curveData[0]
                    }
                };
                this.rankChart.setOption(rankOption);
                this.curveChart.setOption(curveOption);
            },
            tgEqs: function (val) {
                let curveOption = {
                    series: {
                        id: 'line',
                        data: val
                    }
                };
                this.curveChart.setOption(curveOption);
            }
        },
        methods: {
            ...mapActions([
                'updateTgEqCurve'
            ]),
            renderCurve(params) {
                let no = '';
                if (this.currentType === 'tg') {
                    no = params.data.name;
                } else if (this.currentType === 'user') {
                    no = params.name;
                }
                let getParam = {type: this.currentType, no: no};
                getTgEq(getParam).then((res) => {
                    let curveOption = {
                        series: {
                            id: 'line',
                            data: res.data.eqs
                        }
                    };
                    console.log(res.data.eqs);
                    this.curveChart.setOption(curveOption);
                });
            },
            renderRankChart() {
                this.rankChart = ECharts.init(document.getElementById('rankChart'));
                this.rankChart.setOption(this.rankChartOption);
                this.rankChart.on('click', this.renderCurve);

                this.curveChart = ECharts.init(document.getElementById('curveChart'));
                this.curveChart.setOption(this.curveChartOption);
            },
            renderTopData(topk) {
                console.log(topk);
            }
        },
        mounted: function () {
            this.renderRankChart();
        }
    }
</script>

<style scoped lang="scss">
    .chart-container {
        width: 100%;
        height: 100%;
        float: left;
        .chart-container2 {
            height: 50%;
            .chart {
                width: 90%;
                height: 100%;
                margin: 0 auto;
            }
        }
    }
</style>
