/**
 * Created by storm on 2017/6/16.
 */
export const boxPlotOption = {
    title: {},
    color: ['#19a15f', '#277fc4'],
    tooltip: {
        trigger: 'item',
        formatter: function (param) {
            return [
                '类别' + param.name + ': ',
                'upper: ' + param.data[5],
                'Q3: ' + param.data[4],
                'median: ' + param.data[3],
                'Q1: ' + param.data[2],
                'lower: ' + param.data[1]
            ].join('<br/>');
        }
    },
    grid: {
        top: 20
    },
    xAxis: {
        type: 'value',
        name: 'kW·h',
        position: 'top',
        splitArea: {
            show: false
        },
        splitLine: {
            show: false
        }
    },
    yAxis: {
        type: 'category',
        data: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        boundaryGap: true,
        inverse: true,
        nameGap: 30,
        splitArea: {
            show: false
        },
        splitLine: {
            show: false
        },
        axisLabel: {
            formatter: '类别{value}',
            show: false
        },
        axisTick: {
            show: false
        },
        axisLine: {
            show: false
        }
    },
    series: {
        name: 'boxplot',
        type: 'boxplot',
        tooltip: {
            trigger: 'item',
            formatter: function (param) {
                return [
                    '类别' + param.name + ': ',
                    'upper: ' + param.data[5],
                    'Q3: ' + param.data[4],
                    'median: ' + param.data[3],
                    'Q1: ' + param.data[2],
                    'lower: ' + param.data[1]
                ].join('<br/>');
            }
        }
    }
};

let months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

export const seriesPieOption = {
    title: {},
    color: ['#19a15f', '#277fc4'],
    grid: {
        left: 0,
        top: 20,
        right: 5
    },
    visualMap: {
        show: false,
        min: 0,
        max: 1,
        dimension: 2
    },
    xAxis: {
        type: 'category',
        data: months,
        position: 'top',
        splitArea: {
            show: false
        },
        splitLine: {
            show: false
        }
    },
    yAxis: {
        show: false,
        inverse: true,
        type: 'category',
        data: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        axisLabel: {
            formatter: '类别{value}'
        },
        splitArea: {
            show: false
        },
        splitLine: {
            show: false
        }
    },
    series: []
};

export const barOption = {
    title: {},
    color: ['#19a15f', '#277fc4'],
    grid: {
        left: 0,
        top: 20
    },
    xAxis: {
        type: 'value',
        position: 'top',
        max: 10,
        splitLine: {
            show: false
        }
    },
    yAxis: {
        type: 'category',
        inverse: true,
        data: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        axisLabel: {
            formatter: '类别{value}'
        },
        axisLine: {
            lineStyle: {
                color: '#888'
            }
        },
        splitArea: {
            show: false
        }
    },
    tooltip: {
        trigger: 'item',
        formatter: '{c}'
    },
    series: {
        type: 'bar'
    }
};
