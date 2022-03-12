<template>
    <div>
        <v-row justify="center">
            <v-col cols="2">
                <v-avatar color="grey lighten-2" size="45"><v-icon size="55">mdi-account-circle</v-icon></v-avatar>
            </v-col>
            <v-col cols="10">
                <p class="text-h5 text-right">거친 빽뺵도요님</p>
            </v-col>
        </v-row>
        <v-divider class="mt-3 mb-3"></v-divider>
        <div class="text-body-1 text--primary"><v-icon>mdi-account</v-icon> 프로필 설정</div>
        <v-divider class="mt-3 mb-3"></v-divider>
        <div class="text-body-1 text--primary"><v-icon>mdi-file-sign</v-icon> 약관 및 정책</div>
        <v-divider class="mt-3 mb-3"></v-divider>
        <div class="text-body-1 text--primary"><v-icon>mdi-logout</v-icon> 로그아웃</div>
        <v-divider class="mt-3 mb-3"></v-divider>
        <div class="text-body-1 text--primary"><v-icon>mdi-account-off</v-icon> 회원탈퇴</div>
        <v-divider class="mt-3 mb-3"></v-divider>
    </div>
</template>

<script>
export default {
    name: "profile-component",
    data: () => ({
        //
    }),
    created: function () {},
    mounted: function () {},
    computed: {},
    methods: {},
};
</script>
