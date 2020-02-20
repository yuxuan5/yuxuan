<template>
    <aside id="side-nav" :class="collapsed ? 'menu-collapsed' : 'menu-expand' ">
        <el-menu defaultActive="2" class="el-menu-vertical-demo" v-show="!collapsed"
                 @open="handleOpen" @close="handleClose">
            <div class="line-search">
                <div class="section-header">
                    <span>线路搜索</span>
                </div>
                <el-input v-model="lineValue" placeholder="输入线路" icon="search" :on-icon-click="searchLine">
                </el-input>
            </div>
            <div class="tq-heat">
                <div class="section-header">
                    <span>台区搜索</span>
                </div>
                <el-input v-model="tgValue" placeholder="输入台区" icon="search" :on-icon-click="searchTg">
                </el-input>
            </div>
            <div class="analyze-select">
                <div class="section-header">
                    <span>用电行为分析</span>
                </div>
                <el-select v-model="analysis" placeholder="请选择分析方法" @change="analyzeChange">
                    <el-option v-for="item in analyzeOptions" :key="item.value"
                               :label="item.label" :value="item.value">
                    </el-option>
                </el-select>
            </div>

            <div class="params-input">
                <div style="margin-top: 15px">
                    <el-input v-model="cnum" size="small" placeholder="请输入聚类个数" v-show="enableCluster">
                    </el-input>
                </div>
                <div style="margin-top: 15px">
                    <el-button style="width: 100%" type="primary" size="large" v-show="enableCluster" @click="cluster">聚类</el-button>
                </div>
            </div>
        </el-menu>
        <ul class="el-menu el-menu-vertical-demo collapsed" v-show="collapsed" ref="enuCollapsed">
        </ul>
    </aside>
</template>

<script>
    import { mapState, mapActions } from 'vuex'

    export default {
        name: 'side-nav',
        data() {
            return {
                lineOptions: [],
                lineValue: '',
                tgValue: '',
                loading: false,
                tqOptions: [{
                    value: 'tq',
                    label: '台区'
                }, {
                    value: 'other',
                    label: 'other'
                }],
                tqValue: '',
                userOptions: [{
                    value: '00',
                    label: '所有类型'
                }, {
                    value: '01',
                    label: '高压用户'
                }, {
                    value: '02',
                    label: '低压非居民用户'
                }, {
                    value: '03',
                    label: '居民用户'
                }],
                userValue: '',
                analyzeOptions: [{
                    value: 'position',
                    label: '基于位置的分析'
                }, {
                    value: 'cluster',
                    label: '基于聚类的分析'
                }],
                analysis: '',
                cnum: '',
                param1: '',
                param2: '',
                param3: '',
                enablePosition: false,
                enableCluster: false,
                clusteringOptions: [{
                    value: 'k-means',
                    label: 'k-means'
                }, {
                    value: 'other',
                    label: 'other'
                }],
                clusteringValue: ''
            }
        },
        computed: {
            ...mapState([
                'collapsed'
            ])
        },
        watch: {
            collapsed: function (val) {
                console.log(val);
            }
        },
        methods: {
            ...mapActions([
                'searchLineAction',
                'searchTgAction',
                'updateUserTypeAction',
                'searchUserInShapeAction',
                'updateAlgorithmAction',
                'updateAnalyzeMethod',
                'clustering'
            ]),
            handleOpen(key, keyPath) {
                console.log(key, keyPath);
            },
            handleClose(key, keyPath) {
                console.log(key, keyPath);
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
            analyzeChange(param) {
                console.log(param);
                if (param === 'position') {
                    this.enablePosition = true;
                    this.enableCluster = false;
                } else if (param === 'cluster') {
                    this.enablePosition = false;
                    this.enableCluster = true;
                }
                this.updateAnalyzeMethod(param);
            },
            cluster() {
                let param = {cnum: this.cnum}
                this.clustering(param);
            },
            userTypeChange(param) {
                console.log(param);
                this.updateUserTypeAction(param);
            },
            clusteringChange(param) {
                console.log(param);
                this.updateAlgorithmAction(param);
            }
        }
    }
</script>

<style scoped lang="scss">
    aside {
        flex: 0 0 230px;
        width: 230px;

        .el-menu {
            height: 100%;
        }

        .line-search {
            width: 90%;
            margin: 0 auto;
            .section-header {
                height: 13px;
                border-bottom: 1px solid #ccc;
                text-align: center;
                margin: 20px auto 15px;
                span {
                    font-size: 16px;
                    color: #666;
                    background-color: #eef1f6;
                    padding: 0 10px;
                }
            }
        }

        .tq-heat {
            width: 90%;
            margin: 0 auto;
            .section-header {
                height: 13px;
                border-bottom: 1px solid #ccc;
                text-align: center;
                margin: 20px auto 15px;
                span {
                    font-size: 16px;
                    color: #666;
                    background-color: #eef1f6;
                    padding: 0 10px;
                }
            }
        }

        .user-heat {
            width: 90%;
            margin: 0 auto;
            .section-header {
                height: 13px;
                border-bottom: 1px solid #ccc;
                text-align: center;
                margin: 20px auto 15px;
                span {
                    font-size: 16px;
                    color: #666;
                    background-color: #eef1f6;
                    padding: 0 10px;
                }
            }
        }

        .analyze-select {
            width: 90%;
            margin: 0 auto;
            .section-header {
                height: 13px;
                border-bottom: 1px solid #ccc;
                text-align: center;
                margin: 20px auto 15px;
                span {
                    font-size: 16px;
                    color: #666;
                    background-color: #eef1f6;
                    padding: 0 10px;
                }
            }
        }

        .params-input {
            width: 90%;
            margin: 0 auto;
        }

        .clustering-setting {
            width: 90%;
            margin: 0 auto;
            .section-header {
                height: 13px;
                border-bottom: 1px solid #ccc;
                text-align: center;
                margin: 20px auto 15px;
                span {
                    font-size: 16px;
                    color: #666;
                    background-color: #eef1f6;
                    padding: 0 10px;
                }
            }
        }

        .collapsed {
            width: 60px;
            .item {
                position: relative;
            }
            .submenu {
                position: absolute;
                top: 0px;
                left: 60px;
                z-index: 99999;
                height: auto;
                display: none;
            }
        }
    }
    .menu-collapsed {
        flex: 0 0 60px;
        width: 60px;
    }
    .menu-expanded {
        flex: 0 0 230px;
        width: 230px;
    }
</style>