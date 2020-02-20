<template>
    <div id="app">
        <el-row class="container">
            <top-header></top-header>
            <el-col :span="24" class="main">
                <side-nav></side-nav>
                <section class="content-container">
                    <el-col :span="10" class="map">
                        <leaflet-map></leaflet-map>
                    </el-col>
                    <el-col :span="14" class="chart">
                        <router-view></router-view>
                    </el-col>
                </section>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import { mapState } from 'vuex'
    import TopHeader from './components/top-header.vue';
    import SideNav from './components/side-nav.vue';
    import LeafletMap from './components/leaflet-map.vue'

    export default {
        name: 'app',
        components: {
            TopHeader,
            SideNav,
            LeafletMap
        },
        computed: {
            ...mapState([
                'searchLine',
                'searchTg',
                'userType',
                'algorithmType',
                'analyzeMethod'
            ])
        },
        watch: {
            searchLine: function (val) {
                console.log(val);
                this.$router.push({path: '/ltCharts'});
            },
            searchTg: function (val) {
                console.log(val);
                this.$router.push({path: '/ltCharts'});
            },
            userType: function (val) {
                console.log(val);
                this.$router.push({path: '/ltCharts'});
            },
            algorithmType: function (val) {
                console.log(val);
                this.$router.push({path: '/userCharts'});
            },
            analyzeMethod: function (val) {
                if (val === 'position') {
                    this.$router.push({path: '/positionCharts'});
                } else if (val === 'cluster') {
                    this.$router.push({path: '/userCharts'});
                }
            }
        },
        mounted: function () {
            this.$router.push({path: '/mainCharts'});
        }
    }
</script>

<style scoped lang="scss">
    // @import "../node_modules/leaflet/dist/leaflet.css";
    body {
        margin: 0;
        padding: 0;
    }

    #app {
        position: absolute;
        top: 0px;
        bottom: 0px;
        width: 100%;

        .container {
            position: absolute;
            top: 0px;
            bottom: 0px;
            width: 100%;

            .main {
                display: flex;
                position: absolute;
                top: 45px;
                bottom: 0px;
                overflow: hidden;

                .content-container {
                    flex: 1;
                    overflow-y: scroll;
                    padding-left: 10px ;

                    .map {
                        height: 100%;
                    }
                    .chart {
                        height: 100%;
                    }
                }
            }
        }
    }
</style>
