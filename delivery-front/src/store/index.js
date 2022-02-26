import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

export default new Vuex.Store({
    plugins: [createPersistedState()],
    state: {
        kakaoAppkey: "2fe3c5d9478752a4437a5c9910028bc4",
        foodTags: [
            "한식",
            "분식",
            "카페",
            "일식",
            "양식",
            "치킨",
            "피자",
            "중국집",
            "패스트푸드",
            "야식",
        ],
        userInfo: "",
        parties: [],
    },
    mutations: {
        addUserInfo: function(state, payload) {
            return (state.userInfo = payload);
        },
        getPartyList: function(state, payload) {
            return (state.parties = payload);
        },
    },
    actions: {},
    modules: {},
    getters: {},
});
