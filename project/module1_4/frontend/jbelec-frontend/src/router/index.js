import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import index from '@/components/pages/index'
import test from '@/components/pages/test'
import MiddleMap from '@/components/middle-map'
import mainchart from '@/components/mainchart'
import TopHeader from '@/components/top-header'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'mainchart',
      component: mainchart
    },
    {
      path: '/index',
      name: 'index',
      component: index
    },
    {
      path: '/HelloWorld',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
        path: '/test',
        name: 'test',
        component: test
      },
    {
        path: '/mymap',
        name: 'MiddleMap',
        component: MiddleMap
    },
    
  ]
})
