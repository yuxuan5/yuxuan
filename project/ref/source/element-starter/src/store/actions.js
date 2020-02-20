/**
 * Created by storm on 2017/5/4.
 */
import types from './mutation-types'

export default {
    updateCollapsed: ({ commit }) => commit(types.UPDATE_COLLAPSED),
    searchLineAction: ({ commit }, params) => commit(types.SEARCH_LINE, params),
    searchTgAction: ({ commit }, params) => commit(types.SEARCH_TG, params),
    updateAnalyzeMethod: ({ commit }, params) => commit(types.UPDATE_ANALYZE_METHOD, params),
    clustering: ({ commit }, params) => commit(types.CLUSTERING, params),
    updateUserTypeAction: ({ commit }, params) => commit(types.UPDATE_USER_TYPE, params),
    searchUserInShapeAction: ({ commit }, params) => commit(types.SEARCH_USER_IN_SHAPE, params),
    updateAlgorithmAction: ({ commit }, params) => commit(types.UPDATE_ALGORITHM, params),
    updateTgEqCurve: ({ commit }, params) => commit(types.GET_TG_EQ, params)
};
