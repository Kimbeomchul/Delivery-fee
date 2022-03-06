import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

export default new Vuex.Store({
    plugins: [createPersistedState()],
    state: {
        kakaoAppkey: "2fe3c5d9478752a4437a5c9910028bc4",
        foodTags: ["한식", "분식", "카페", "일식", "양식", "치킨", "피자", "중국집", "패스트푸드", "야식"],
        userInfo: "",
        parties: [],
        party: [],
        comments: [],
    },
    mutations: {
        addUserInfo: function (state, payload) {
            return (state.userInfo = payload);
        },
        changeParties: function (state, payload) {
            return (state.parties = payload);
        },
        pushToParties: function (state, payload) {
            return state.parties.push(payload);
        },
        changeParty: function (state, payload) {
            return (state.party = payload);
        },
        changeComments: function (state, payload) {
            return (state.comments = payload);
        },
        pushToComments: function (state, payload) {
            return state.comments.push(payload);
        },
    },
    actions: {
        addUserInfo: function (context, payload) {
            return context.commit("addUserInfo", payload);
        },
        changeParties: function (context, payload) {
            return context.commit("changeParties", payload);
        },
        pushToParties: function (context, payload) {
            return context.commit("pushToParties", payload);
        },
        changeParty: function (context, payload) {
            return context.commit("changeParty", payload);
        },
        changeComments: function (context, payload) {
            return context.commit("changeComments", payload);
        },
        pushToComments: function (context, payload) {
            return context.commit("pushToComments", payload);
        },
    },
    modules: {},
    getters: {},
});
