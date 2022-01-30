<template>
    <v-container class="spacing-playground pa-6 text-center">
        <v-row style="height:200px;"> </v-row>
        <img src="../assets/logo2.png" alt="logo" />
        <v-row style="height:40px;"> </v-row>

        <v-row>
            <v-col cols="9" sm="6">
                <v-text-field dense clearable placeholder="휴대폰번호를 입력하세요"></v-text-field>
            </v-col>
            <v-col cols="2" sm="6">
                <v-btn elevation="1" small>인증하기</v-btn>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="9" sm="6">
                <v-text-field dense clearable placeholder="휴대폰번호를 입력하세요"></v-text-field>
            </v-col>
            <v-col cols="2" sm="6">
                <v-btn elevation="1" small>인증확인</v-btn>
            </v-col>
        </v-row>
        <v-row style="height:40px;"> </v-row>

        <v-btn block x-large rounded color="#52D4DC" dark>
            시작하기
        </v-btn>
    </v-container>
</template>
