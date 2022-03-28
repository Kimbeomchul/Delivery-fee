<template>
    <div>
        <v-app-bar elevation="0" color="white" dense class="shrink">
            <v-row>
                <v-col cols="2" class="pl-0 pr-0 d-flex justify-start">
                    <v-btn v-if="$route.name !== 'list'" @click="$router.go(-1)" color="#52D4DC" icon>
                        <v-icon large>mdi-chevron-left </v-icon>
                    </v-btn>
                </v-col>
                <v-col class="d-flex justify-space-around">
                    <v-toolbar-title class="pt-3">닉네임 설정</v-toolbar-title>
                </v-col>
                <v-col cols="2" class="pl-0 pr-0 d-flex justify-end"> </v-col>
            </v-row>
        </v-app-bar>
        <v-container class="spacing-playground pa-4">
            <v-form ref="form" v-model="valid" lazy-validation>
                <v-text-field v-model="nickname" :counter="10" :rules="nicknameRules" label="닉네임" required clearable>
                </v-text-field>
            </v-form>
            <v-btn
                v-if="!$route.query.edit"
                block
                x-large
                rounded
                color="#52D4DC"
                dark
                class="font-weight-bold mt-5"
                style="font-size: 1.02em"
                @click="editNickname()"
            >
                설정하기
            </v-btn>
        </v-container>
    </div>
</template>
<script>
import request from "@/request";

export default {
    name: "myinfo-component",
    data: () => ({
        valid: true,
        nickname: "",
        nicknameRules: [
            (value) => !!value || "닉네임은 필수 입력 항목입니다.",
            (value) => (value && value.length <= 10) || "닉네임은 10자까지 입력할 수 있습니다.",
        ],
    }),
    created: function () {
        this.nickname = this.userInfo.nickname;
    },
    computed: {
        userInfo() {
            return this.$store.state.userInfo;
        },
    },
    methods: {
        editNickname: async function () {
            const validate = this.$refs.form.validate();
            if (!validate) return;

            const data = {
                nickname: this.nickname,
            };
            try {
                const result = await request(`/users/${this.$store.state.userInfo.user_id}/`, "PATCH", data);

                if (result.status === 200) {
                    this.$store.dispatch("editNickname", result.data.nickname);
                    this.$router.go(-1);
                } else if (result.status === 400) {
                    this.$toast.error("이미 존재하는 닉네임입니다. 다른 닉네임을 입력해주세요.");
                } else {
                    console.log(result);
                }
            } catch (error) {
                console.log(error);
            }
        },
    },
};
</script>
