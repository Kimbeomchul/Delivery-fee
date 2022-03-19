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
        isFullyLoadedComments: false,
    },
    mutations: {
        addUserInfo: function (state, payload) {
            return (state.userInfo = payload);
        },
        pushParticipationStatus: function (state, payload) {
            return (state.userInfo.participated = payload);
        },
        popParticipationStatus: function (state) {
            return state.userInfo.splice("participated");
        },
        changeParties: function (state, payload) {
            return (state.parties = payload);
        },
        pushToParties: function (state, payload) {
            return payload.infinite ? state.parties.push(...payload) : state.parties.push(payload);
        },
        changeParty: function (state, payload) {
            return (state.party = payload);
        },
        editComment: function (state, payload) {
            console.log(payload);
            return (state.comments[payload["index"]].content = payload.content);
        },
        changeComments: function (state, payload) {
            return (state.comments = payload);
        },
        pushToComments: function (state, payload) {
            if (payload.infinite) {
                return state.comments.push(...payload);
            } else {
                if (!state.isFullyLoadedComments) state.comments.pop();
                state.comments.unshift(payload);
            }
        },
        popToComments: function (state, payload) {
            return state.comments.splice(payload, 1);
        },
        logout: function (state) {
            state.userInfo = "";
            state.parties = [];
            state.party = [];
            state.comments = [];
        },
        changeLoadingStatusComments: function (state, payload) {
            return (state.isFullyLoadedComments = payload);
        },
    },
    actions: {
        addUserInfo: function (context, payload) {
            return context.commit("addUserInfo", payload);
        },
        pushParticipationStatus: function (context, payload) {
            return context.commit("pushParticipationStatus", payload);
        },
        popParticipationStatus: function (context) {
            return context.commit("pushParticipationStatus");
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
        editComment: function (context, payload) {
            return context.commit("editComment", payload);
        },
        changeComments: function (context, payload) {
            return context.commit("changeComments", payload);
        },
        pushToComments: function (context, payload) {
            return context.commit("pushToComments", payload);
        },
        popToComments: function (context, payload) {
            return context.commit("popToComments", payload);
        },
        logout: function (context) {
            return context.commit("logout");
        },
        changeLoadingStatusComments: function (context, payload) {
            return context.commit("changeLoadingStatusComments", payload);
        },
    },
    modules: {},
    getters: {},
});
