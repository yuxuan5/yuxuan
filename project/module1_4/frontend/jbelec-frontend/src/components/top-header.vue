<template>
    <div class="page">
        <div class="header">
            <div class="title">
                冀北电力数据可视化系统
            </div>
            <div class="title-bottom">
                <div class="bottom-sidebar"></div>
            </div>
        </div>

       
  </div>
</template>

<script>

    export default {
        name: 'top-header',
        data() {
            return {
                sysName: '电力数据可视化系统',
                userName: 'DMGroup'
            };
        },
    }
</script>

 <style scoped>
        .header {
            margin: 4px;
        }
    
        .header .title {
            font-size: 24px;
            color: #fff;
    
        }
    
        .title-bottom {
            height: 30px;
            justify-content: center;
            display: flex;
    
        }
    
        .bottom-sidebar {
            width: 100%;
            height: 100%;
            opacity: 1;
            background-image: url("~@/assets/images/bottombar.gif");
            background-size: 100%;
            background-repeat: no-repeat;
            background-position: center center;
            width: 400px;
        }
    
        .bottom-line {
            width: 100%;
            height: 30px;
            background-image: url("~@/assets/images/bottomline.png");
            background-size: 100%;
            background-repeat: no-repeat;
            background-position: center center;
        }
    
        .box-content {
            display: block;
            line-height: 1.42857143;
            -webkit-transition: border 0.2s ease-in-out;
            -o-transition: border 0.2s ease-in-out;
            transition: border 0.2s ease-in-out;
        }
    
        .box-content.shadow {
            box-shadow: 1px 2px 8px 0px #888;
    
        }
    
        .statistic-item {
            display: flex;
            margin-bottom: 10px;
            align-items: center;
            overflow: hidden;
        }
    
        .statistic-item .icon-content {
            width: 50px;
            min-width: 50px;
            height: 50px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #3b4e82;
            border-radius: 50%;
        }
    
        .icon-content .iconfont {
            font-size: 24px;
            color: #fff;
        }
    
        .text-content {
            margin-left: 10px;
            overflow: hidden;
        }
    
        .statistic-item .text {
            font-size: 26px;
            color: #fff;
        }
    
        .statistic-item .sub-title {
            font-size: 14px;
            text-align: left;
            color: rgb(154, 168, 212);
        }
    
        .chart {
            height: 300px;
        }
    
        .echart {
            width: 500px;
            height: 500px;
        }
    
    
    
        .table-container {
            width: 400px;
            padding: 20px;
        }
    
        .table {
            width: 100%;
            background-color: transparent;
            color: #666;
            border-width: 1px;
            border-style: solid;
            border-color: #e6e6e6;
        }
    
        .table.darkblue {
            border-color: rgba(130, 157, 248, 0.705);
        }
    
        .table.darkblue td {
            border: none;
        }
    
        .table.darkblue tr .th {
            color: rgb(154, 168, 212);
        }
    
        .table.darkblue tr td {
            color: rgb(229, 233, 247);
    
        }
    
        .table tr {
            transition: all .3s;
            -webkit-transition: all .3s;
        }
    
        .table td.border_bottom_none {
            border-bottom: none;
        }
    
        .table td.td_2 {
            padding: 0;
        }
    
        .table td,
        .table th {
            position: relative;
            padding: 9px 15px;
            min-height: 20px;
            line-height: 20px;
            font-size: 14px;
            border-width: 1px;
            border-style: solid;
            border-color: #e6e6e6;
            padding: 5px 10px;
            border-top: none;
            border-left: none
        }
    
        .table td:last-child {
            border-right: none;
        }
    
        .table tr:last-child {
            border-bottom: none;
        }
    
        .table td.padding_none {
            padding: 0;
        }
    
        .width_half {
            width: 50%;
        }
    
        .td_2_table tr:last-child td:last-child {
            border-bottom: none;
        }
    
        .td_right {
            text-align: right;
        }
    
        .chart-container {
            height: 200px;
        }
    
    
        .box-content .caption {
            text-align: left;
            color: #fff;
        }
    
        small.number {
            color: #0b8603;
            font-weight: bold;
        }
    
        .warning {
            color: red;
        }
    </style>
