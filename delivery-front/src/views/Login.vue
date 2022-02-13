<template>
    <v-container class="spacing-playground pa-6 text-center">
        <v-row style="height:200px;"> </v-row>
        <img src="../assets/logo2.png" alt="logo" />
        <v-row style="height:40px;"> </v-row>

        <v-row class="pr-3">
            <v-col cols="9" xs="6">
                <v-text-field
                    class="pl-3"
                    dense
                    clearable
                    placeholder="휴대폰번호를 입력하세요"
                    v-model="phoneNumber"
                ></v-text-field>
            </v-col>
            <v-col cols="2" xs="6" class="pa-4">
                <v-btn outlined color="#52D4DC" rounded elevation="1" small>인증하기</v-btn>
            </v-col>
        </v-row>
        <v-row class="pr-3">
            <v-col cols="9" xs="6">
                <v-text-field
                    class="pl-3"
                    dense
                    clearable
                    placeholder="인증번호를 입력하세요"
                    v-model="CertificationNumber"
                ></v-text-field>
            </v-col>
            <v-col cols="2" xs="6" class="pa-4">
                <v-btn outlined color="#52D4DC" rounded elevation="1" small>인증확인</v-btn>
            </v-col>
        </v-row>
        <v-row style="height:40px;"> </v-row>

        <v-btn
            @click="signUpGoogle"
            block
            x-large
            rounded
            color="#52D4DC"
            dark
            class="font-weight-bold"
            style="font-size:1.02em"
        >
            Google로 시작하기
        </v-btn>
        <br />
        <v-btn
            @click="signUpKakao"
            block
            x-large
            rounded
            color="#52D4DC"
            dark
            class="font-weight-bold"
            style="font-size:1.02em"
        >
            카카오톡으로 시작하기
        </v-btn>
    </v-container>
</template>

<script>
import request from "@/request";

export default {
    name: "Login",
    data: () => ({
        phoneNumber: "asdfasdf",
        CertificationNumber: "",
        //
    }),
    methods: {
        signUpGoogle: async function() {
            // 문제 1: 버튼을 2번 눌러야 이동함, href가 2번째 이벤트부터 제대로 값이 들어가 동작하는 듯?
            // 문제 2: 아직 백엔드 구현이 덜됨
            try {
                let result = await request("/auth/google/login/", "GET");

                if (result.status === 200) {
                    console.log(result.data.url);
                    // FIXME: window.location.href를 이용 하는데 좋은 방법인지 고려
                    // 리다이렉트, location.href 가 정상적인 방법인가?
                    // 1. 뷰 -> 장고 백엔드서버로 주소 이동
                    // 2. 장고에서 회원가입 처리 후 -> redirect(localhost:8080/list)
                    window.location.href = result.data.url;
                }
            } catch (error) {
                console.log(error);
            }
        },
        signUpKakao: async function() {
            // 문제 1: 버튼을 2번 눌러야 이동함, href가 2번째 이벤트부터 제대로 값이 들어가 동작하는 듯?
            // 문제 2: 아직 백엔드 구현이 덜됨
            try {
                let result = await request("/auth/kakao/login/", "GET");

                if (result.status === 200) {
                    console.log(result.data.url);
                    // FIXME: window.location.href를 이용 하는데 좋은 방법인지 고려
                    // 리다이렉트, location.href 가 정상적인 방법인가?
                    // 1. 뷰 -> 장고 백엔드서버로 주소 이동
                    // 2. 장고에서 회원가입 처리 후 -> redirect(localhost:8080/list)
                    window.location.href = result.data.url;
                }
            } catch (error) {
                console.log(error);
            }
        },
    },
};
</script>
