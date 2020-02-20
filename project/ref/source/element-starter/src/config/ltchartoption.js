/**
 * Created by storm on 2017/5/19.
 */
export const rankChartOption = {
    animation: true,
    animationDuration: 1000,
    animationEasing: 'cubicInOut',
    animationDurationUpdate: 1000,
    animationEasingUpdate: 'cubicInOut',
    title: {
        id: 'statistic',
        left: 'center',
        text: 'Top台区用电量',
        textStyle: {
            fontSize: 16
        }
    },
    toolbox: {
        iconStyle: {
            normal: {
                borderColor: '#444'
            },
            emphasis: {
                borderColor: '#b1e4ff'
            }
        }
    },
    tooltip : {
        trigger: 'item'
    },
    grid: {
        left: 80,
        top: 80
    },
    yAxis: {
        type: 'value',
        name: '用电量/W·kv·h',
        nameLocation: 'end',
        scale: true,
        boundaryGap: false,
        splitLine: {show: false},
        axisLine: {show: true, lineStyle: {color: '#444'}},
        axisTick: {show: false},
        axisLabel: {show: true, margin: 2, textStyle: {color: '#444'}}
    },
    xAxis: {
        type: 'category',
        nameGap: 16,
        axisLine: {show: true, lineStyle: {color: '#444'}},
        axisTick: {show: false, lineStyle: {color: '#444'}},
        axisLabel: {interval: 0, rotate: 45, textStyle: {color: '#444'}},
        data: []
    },
    series : [
        {
            id: 'bar',
            type: 'bar',
            symbol: 'none',
            itemStyle: {
                normal: {
                    color: '#ddb926'
                }
            },
            data: []
        }
    ]
};

let base = +new Date(2015, 1, 1);
let oneDay = 24 * 3600 * 1000;
let date = [];
for (let i = 0; i < 365; i++) {
    let now = new Date(base += oneDay);
    date.push([now.getFullYear(), now.getMonth()+1, now.getDay()].join('/'));
}
export const curveChartOption = {
    title: [
        {
            id: 'statistic',
            left: 'center',
            text: '用电曲线',
            textStyle: {
                fontSize: 16
            }
        }
    ],
    toolbox: {
        iconStyle: {
            normal: {
                borderColor: '#444'
            },
            emphasis: {
                borderColor: '#b1e4ff'
            }
        }
    },
    tooltip : {
        trigger: 'item'
    },
    grid: {
        left: 80,
        top: 80
    },
    dataZoom: [{
        type: 'inside',
        realtime: true,
        start: 0,
        end: 100
    }],
    xAxis: {
        type: 'category',
        boundaryGap: false,
        nameGap: 16,
        axisLine: {onZero: false, show: true, lineStyle: {color: '#444'}},
        axisTick: {show: false, lineStyle: {color: '#444'}},
        axisLabel: {textStyle: {color: '#444'}},
        data: date
    },
    yAxis: {
        type: 'value',
        name: '用电量/W·kv·h',
        nameLocation: 'end',
        scale: true,
        boundaryGap: false,
        splitLine: {show: false},
        axisLine: {show: true, lineStyle: {color: '#444'}},
        axisTick: {show: false},
        axisLabel: {show: true, margin: 2, textStyle: {color: '#444'}}
    },
    series : [
        {
            id: 'line',
            type: 'line',
            symbol: 'none',
            itemStyle: {
                normal: {
                    color: '#ddb926'
                }
            },
            data: []
        }
    ]
};