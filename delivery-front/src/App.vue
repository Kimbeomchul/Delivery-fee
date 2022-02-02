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
            <v-app-bar-nav-icon></v-app-bar-nav-icon>
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
                        <v-list-item-title>{{ item.title }}</v-list-item-title>
                    </v-list-item>
                </v-list>
            </v-menu>
        </v-app-bar>

        <v-main>
            <router-view />
        </v-main>

        <!-- FIXME : 푸터 -> 공통 컴포넌트로 이동하기 -->
        <v-footer color="white" v-if="$route.name === 'detail'">
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
        items: [
            { title: "Click Me" },
            { title: "Click Me" },
            { title: "Click Me" },
            { title: "Click Me 2" },
        ],
        //
    }),
};
</script>
