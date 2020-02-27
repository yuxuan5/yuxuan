<template>
  <div>
  <h1>我是右边栏</h1>
  <h2>{{stationlist}}</h2>
  </div>

</template>

<script>
  export default{
    name: 'right-nav',
    data(){
      return {
        stationlist:[],
      }
    },
    created(){
         // 绑定全局事件globalEvent事件，
        this.$bus.$on('globalEvent',(val)=>{
             this.stationlist = val;
             console.log(this.stationlist);
        })
    }
 }
</script>

<style>
</style>
