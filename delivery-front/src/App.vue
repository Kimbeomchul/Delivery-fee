<template>
    <v-app>
        <appbar-component></appbar-component>
        <v-main>
            <!-- FIXME: 페이지 트랜지션 적용 변경해야함 css -->
            <transition name="fade">
                <router-view />
            </transition>
        </v-main>

        <v-footer app color="white">
            <comment-component v-if="$route.name === 'detail'"></comment-component>
        </v-footer>
    </v-app>
</template>

<script>
import AppbarComponent from "./components/AppBar.vue";
import CommentComponent from "./components/Comment.vue";

export default {
    name: "App",
    components: { AppbarComponent, CommentComponent },
};
</script>

<style>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.3s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
    opacity: 0;
}
</style>
