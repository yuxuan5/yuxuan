/**
 * Created by storm on 2017/8/6.
 */
export const multiPieOption = {
    tooltip : {
        trigger: 'item',
        formatter: "{b}: <br/>{c} ({d}%)"
    },
    color: ['red', 'orange', 'green'],
    legend: {
        x : 'center',
        y : 'bottom',
        data:['高压用户','低压非居民用户','居民用户']
    },
    toolbox: {
        show : true,
        feature : {
            mark : {show: true},
            dataView : {show: true, readOnly: false},
            magicType : {
                show: true,
                type: ['pie', 'funnel']
            },
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
    calculable : true,
    series : []
};

export const boxPlotOption1 = {
    title: {
        text: '高压用户',
        x:'center'
    },
    color: ['red'],
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
        top: 50,
        left: 5,
    },
    xAxis: {
        type: 'value',
        name: '万度',
        position: 'top',
        nameGap: 0,
        nameTextStyle: {
            fontWeight: 10
        },
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

export const boxPlotOption2 = {
    title: {
        text: '低压非居民用户',
        x:'center'
    },
    color: ['orange'],
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
        top: 50,
        left: 5
    },
    xAxis: {
        type: 'value',
        name: '万度',
        position: 'top',
        nameGap: 0,
        nameTextStyle: {
            fontWeight: 5
        },
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

export const boxPlotOption3 = {
    title: {
        text: '居民用户',
        x:'center'
    },
    color: ['green'],
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
        top: 50,
        left: 5
    },
    xAxis: {
        type: 'value',
        name: '度',
        position: 'top',
        nameGap: 0,
        nameTextStyle: {
            fontWeight: 5
        },
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
