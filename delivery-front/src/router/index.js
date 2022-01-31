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
        component: () => import("../views/List.vue"),
    },
    {
        path: "/detail",
        name: "detail",
        component: () => import("../views/Detail.vue"),
    },
    {
        path: "/maps",
        name: "maps",
        component: () => import("../views/Map.vue"),
    },
    {
        path: "/detail2",
        name: "detail2",
        component: () => import("../views/Detail2.vue"),
    },
];

const router = new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes,
});

export default router;
