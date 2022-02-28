import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
    {
        path: "/",
        name: "home",
        component: () => import("../views/Home.vue"),
    },
    {
        path: "/login",
        name: "login",
        component: () => import("../views/Login.vue"),
    },
    {
        path: "/list",
        name: "list",
        component: () => import("../views/ListWrite.vue"),
    },
    {
        path: "/write",
        name: "write",
        component: () => import("../views/Write.vue"),
    },
    {
        path: "/detail/:partyId",
        name: "detail",
        component: () => import("../views/Detail.vue"),
    },
    {
        path: "/map",
        name: "map",
        component: () => import("../views/Map.vue"),
    },
];

const router = new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes,
    scrollBehavior() {
        return { x: 0, y: 0 };
    },
});

export default router;
