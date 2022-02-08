<!-- HACK: 아직까지 컴포넌트로 뺴야할지 말지 고민중 -->
<template>
    <v-app-bar elevation="0" color="white" dense class="shrink">
        <v-app-bar-nav-icon></v-app-bar-nav-icon>
        <v-spacer></v-spacer>
        <v-toolbar-title>배공파용</v-toolbar-title>

        <v-spacer></v-spacer>
        <v-btn icon>
            <v-icon>mdi-dots-vertical</v-icon>
        </v-btn>
    </v-app-bar>
</template>

<script>
export default {
    name: "appbar-component",
};
</script>
