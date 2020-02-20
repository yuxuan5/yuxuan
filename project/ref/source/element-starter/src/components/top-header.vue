<template>
    <el-col :span="24" class="header">
        <el-col :span="10" class="logo" :class="collapsed ? 'logo-collapse-width' : 'logo-width'">
            {{ collapsed ? '' : sysName }}
        </el-col>
        <el-col :span="10">
            <div class="tools" @click="updateCollapsed">
                <i class="fa fa-align-justify"></i>
            </div>
        </el-col>
        <el-col :span="4" class="userinfo">
            <el-dropdown trigger="hover">
                <span class="el-dropdown-link userinfo-inner">
                    {{ userName }}
                </span>
                <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item>我的消息</el-dropdown-item>
                    <el-dropdown-item>设置</el-dropdown-item>
                    <el-dropdown-item divided>退出</el-dropdown-item>
                </el-dropdown-menu>
            </el-dropdown>
        </el-col>
    </el-col>
</template>

<script>
    import { mapState, mapActions } from 'vuex'

    export default {
        name: 'header',
        data() {
            return {
                sysName: 'VisEB',
                userName: 'hx'
            };
        },
        computed: {
            ...mapState([
                'collapsed'
            ])
        },
        methods: {
            ...mapActions([
                'updateCollapsed'
            ])
        }
    }
</script>

<style scoped lang="scss">
    .header {
        height: 40px;
        line-height: 40px;
        background: #20a0ff;
        color: #fff;
        .logo {
            height: 40px;
            font-size: 20px;
            padding-left: 20px;
            padding-right: 20px;
            border-color: rgba(238, 241, 146, 0.3);
            border-right-width: 1px;
            border-right-style: solid;
        }
        .logo-width {
            width: 230px;
        }
        .logo-collapse-width {
            width: 60px;
        }
        .tools {
            padding: 0 23px;
            width: 14px;
            height: 40px;
            line-height: 40px;
            cursor: pointer;
        }
        .userinfo {
            text-align: right;
            padding-right: 35px;
            float: right;
            .userinfo-inner {
                cursor: pointer;
                color: #fff
            }
        }
    }
</style>