# JBElectric 开发项目

JBElectric 的原型系统开发，基于光缆、光路及之上承载的业务数据

## 项目功能

1. 在地图上可视化光缆、光路及业务，在界面上具有查询具体信息的交互功能；
2. 在某几个站点失效的情况下具备动态路由的功能，并且在站点恢复时重新规划或者恢复原有的路由；
3. 在站点失效的同时能发出切换路由的工单以及修复失效站点的工单，且能及时获取站点信息并启动恢复原有路由的功能；
4. 在现有的光缆、光路数据的基础上能绘制出相应的拓扑图；

## 技术选型

### 前端

- js 运行环境：node.js 12.14.1 [下载地址](https://nodejs.org/en/)
- js 工具库：Vue 2.6.11 
  [安装及教程](https://www.runoob.com/vue2/vue-install.html)
- 界面 UI 工具库：Element UI 2.0.11 
  [安装及教程](https://element.eleme.cn/#/zh-CN/component/installation)

### 可视化

- 可视化工具：echarts
- 地图接口：[高德地图](http://webapi.amap.com)、[百度地图](http://api.map.baidu.com)

### 后端

- 开发语言：Java 1.8
- 后端框架：SpringBoot 1.5.9
- 数据库：MongoDB 4.2.2（暂定）

### 大数据组件

- 内存计算：spark 2.3.0
