import Vue from 'vue';
import VueRouter from 'vue-router'
import routes from './router/route.config'
import App from './App.vue';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-default/index.css';
import 'font-awesome/css/font-awesome.min.css';
import 'leaflet/dist/leaflet.css';
import store from './store/index';
import AMap from 'vue-amap';

Vue.use(ElementUI);
Vue.use(VueRouter);
Vue.use(AMap);

const router = new VueRouter({
    routes
});

AMap.initAMapApiLoader({
    key: '4e5950fb8cb1dcca4333686a8b4e2159',
    plugin: ['AMap.Autocomplete', 'AMap.PlaceSearch', 'AMap.Scale',
             'AMap.OverView', 'AMap.ToolBar', 'AMap.MapType',
             'AMap.PolyEditor', 'AMap.CircleEditor']
});

new Vue({
    store,
    router,
    render: h => h(App)
}).$mount('#app');
