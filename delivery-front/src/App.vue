<template>
    <v-app>
        <v-app-bar elevation="0" color="white" dense class="shrink">
            <v-app-bar-nav-icon></v-app-bar-nav-icon>
            <v-spacer></v-spacer>
            <v-toolbar-title>배공파용</v-toolbar-title>

            <v-spacer></v-spacer>
            <v-btn icon>
                <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>
        </v-app-bar>

        <v-main>
            <router-view />
        </v-main>
    </v-app>
</template>

<script>
export default {
    name: "App",
    data: () => ({
        //
    }),
};
</script>
