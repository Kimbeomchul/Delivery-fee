<template>
    <v-flex xs12 sm6 md3>
        <v-text-field label="댓글을 입력해주세요." type="text" hide-details outlined dense v-model="message">
            <template v-slot:append>
                <v-fade-transition leave-absolute>
                    <v-progress-circular v-if="loading" size="24" color="info" indeterminate></v-progress-circular>
                    <img v-else width="24" height="24" src="../assets/btn.png" alt="btn" />
                </v-fade-transition>
            </template>
        </v-text-field>
    </v-flex>
</template>

<script>
export default {
    name: "comment-component",

    data: () => ({
        message: "",
        loading: false,
        dialog: false,
        //
    }),
};
</script>

<style scoped>
.v-text-field--outlined >>> fieldset {
    position: absolute;
    border-color: white;
    background-color: #e5e5e5;
    z-index: 0;
}
.v-text-field {
    border-radius: 12px;
}
.v-text-field >>> img {
    z-index: 1;
}
</style>
