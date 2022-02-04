<template>
    <v-app>
        <!-- FIXME : 앱바 -> 공통 컴포넌트로 이동하기 -->
        <v-app-bar
            v-if="$route.name !== 'list' && $route.name !== 'home'"
            elevation="0"
            color="white"
            dense
            class="shrink"
        >
            <v-icon large @click="$router.go(-1)">mdi-chevron-left</v-icon>
            <v-spacer></v-spacer>
            <v-toolbar-title>배공파용</v-toolbar-title>

            <v-spacer></v-spacer>
            <v-menu bottom left>
                <template v-slot:activator="{ on, attrs }">
                    <v-btn icon v-bind="attrs" v-on="on">
                        <v-icon>mdi-dots-vertical</v-icon>
                    </v-btn>
                </template>

                <v-list>
                    <v-list-item v-for="(item, i) in items" :key="i">
                        <v-list-item-title @click.stop="dialog = true">
                            {{ item.title }}
                        </v-list-item-title>
                    </v-list-item>
                </v-list>
                <v-dialog v-model="dialog" max-width="300">
                    <v-card>
                        <v-card-title class="text-body2">
                            "근처 파티구해요"에 참가하시겠습니까?
                        </v-card-title>
                        <v-card-text class="text-caption">
                            참가를 진행할 경우 나가기 전까지 유지됩니다.
                        </v-card-text>
                        <v-divider></v-divider>

                        <v-card-actions>
                            <!-- HACK: 버튼만 누르면 앱이 뻗음 고쳐야함-->
                            <v-btn
                                class="text-h5"
                                color="green darken-1"
                                text
                                @click="dialog = false"
                            >
                                아니요
                            </v-btn>
                            <v-spacer></v-spacer>
                            <v-btn
                                class="text-h5 font-weight-bold"
                                color="green darken-1"
                                text
                                @click="dialog = false"
                            >
                                참가하기
                            </v-btn>
                        </v-card-actions>
                    </v-card>
                </v-dialog>
            </v-menu>
        </v-app-bar>

        <v-main>
            <!-- FIXME: 페이지 트랜지션 적용 변경해야함 css -->
            <transition name="fade">
                <router-view />
            </transition>
        </v-main>

        <!-- FIXME : 푸터 -> 공통 컴포넌트로 이동하기 -->
        <v-footer app color="white" v-if="$route.name === 'detail'">
            <v-text-field
                hide-details
                dense
                v-model="message"
                outlined
                clearable
                label="댓글"
                type="text"
            >
                <template v-slot:append>
                    <v-fade-transition leave-absolute>
                        <v-progress-circular
                            v-if="loading"
                            size="24"
                            color="info"
                            indeterminate
                        ></v-progress-circular>
                        <img
                            v-else
                            width="24"
                            height="24"
                            src="https://cdn.vuetifyjs.com/images/logos/v-alt.svg"
                            alt=""
                        />
                    </v-fade-transition>
                </template>
            </v-text-field>
        </v-footer>
    </v-app>
</template>

<script>
export default {
    name: "App",
    data: () => ({
        message: "",
        loading: false,
        dialog: false,
        items: [{ title: "삭제" }, { title: "수정" }, { title: "나가기" }, { title: "참가하기" }],
        //
    }),
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
