<template>
  <div>
    <div style="width: 250px" class="line-search">
        <div class="section-header">
            <span>线路搜索</span>
        </div>
        <el-input v-model="lineValue" placeholder="输入线路" icon="search" :on-icon-click="searchLine">
        </el-input>
    </div>
    <div style="width: 250px" class="tq-heat">
        <div class="section-header">
            <span>光缆搜索</span>
        </div>
        <el-input v-model="tgValue" placeholder="输入光缆" icon="search" :on-icon-click="searchTg">
        </el-input>
    </div>
   <h2>我是侧边栏</h2>
   <div style="width: 250px" >
     <button@click = 'sendAjax'>查找站点测试</button>
  </div>
  </div>

</template>

<script>
  import axios from 'axios';
  export default{
    name: 'side-nav',
    data(){
      return {
        stationlist:[],
      }
    },
  methods:{
     sendAjax(){
       axios.get('http://127.0.0.1:8888/station/find/all')
      .then(res=>{
        console.log(res.data[0]);
        this.stationlist = res.data[0];
       })
      .catch(err=>{
        console.log(err)
       })
       this.$bus.$emit('globalEvent',this.stationlist)
     },
     searchLine() {
       let lid = this.lineValue;
       console.log(lid);
       this.searchLineAction(lid);
     },
     searchTg() {
       let tgno = this.tgValue;
       console.log(tgno);
       this.searchTgAction(tgno);
     },
  }
 }
</script>

<style>
</style>
