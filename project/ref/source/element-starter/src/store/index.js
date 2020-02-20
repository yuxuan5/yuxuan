/**
 * Created by storm on 2017/5/3.
 */
import Vue from 'vue'
import Vuex from 'vuex'
import actions from './actions'
import types from './mutation-types'
import mapStyle from '../assets/map-type'
import { getLineHeat, getTgHeat, getUserInShape, getTgEq, getCluster } from '../api/api'


Vue.use(Vuex);

const state = {
    collapsed: false,
    mapStyle: mapStyle,
    searchLine: false,
    searchLineResult: undefined,
    searchTg: false,
    searchTgResult: undefined,
    userType: '',
    searchUser: false,
    searchUserResult: undefined,
    algorithmType: '',
    analyzeMethod: '',
    clusterResult: undefined,
    tgEqs: undefined
};

const mutations = {
    [types.UPDATE_COLLAPSED] (state) {
        state.collapsed = !state.collapsed;
    },
    [types.SEARCH_LINE] (state, params) {
        getLineHeat(params).then((res) => {
            state.searchLine = !state.searchLine;
            state.searchLineResult = res.data;
        });
    },
    [types.SEARCH_TG] (state, params) {
        getTgHeat(params).then((res) => {
            state.searchTg = !state.searchTg;
            state.searchTgResult = res.data;
        });
    },
    [types.UPDATE_ANALYZE_METHOD] (state, params) {
        state.analyzeMethod = params;
    },
    [types.CLUSTERING] (state, params) {
        getCluster(params).then((res) => {
            state.clusterResult = res.data;
        });
    },
    [types.UPDATE_USER_TYPE] (state, params) {
        state.userType = params;
    },
    [types.SEARCH_USER_IN_SHAPE] (state, params) {
        getUserInShape(params).then((res) => {
            state.searchUser = !state.searchUser;
            state.searchUserResult = res.data;
        });
    },
    [types.UPDATE_ALGORITHM] (state, params) {
        state.algorithmType = params;
    },
    [types.GET_TG_EQ] (state, params) {
        getTgEq(params).then((res) => {
            state.tgEqs = res.data.eqs;
        });
    }
};

export default new Vuex.Store({
    state,
    mutations,
    actions
});
