<template>
    <el-row class="chart-container">
        <el-col :span="12" class="chart-container2">
            <div id="userChart" class="chart">1</div>
        </el-col>
        <el-col :span="12" class="chart-container2">
            <div id="barChart" class="chart">1</div>
        </el-col>
        <el-col :span="24" class="chart-container2">
            <div id="countChart" class="chart">1</div>
        </el-col>
    </el-row>
</template>

<script>
    import ECharts from 'echarts'
    import { userChartOption, barChartOption, countChartOption } from '../config/mainchartoption'

    export default {
        name: 'main-chart',
        data() {
            return {
                userChart: null,
                userChartOption: userChartOption,
                barChart: null,
                barChartOption: barChartOption,
                countChart: null,
                countChartOption: countChartOption
            };
        },
        computed: {

        },
        watch: {

        },
        methods: {
            renderChart() {
                this.userChart = ECharts.init(document.getElementById('userChart'));
                this.userChart.setOption(this.userChartOption);

                this.barChart = ECharts.init(document.getElementById('barChart'));
                this.barChart.setOption(this.barChartOption);

                this.countChart = ECharts.init(document.getElementById('countChart'));
                this.countChart.setOption(this.countChartOption);
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