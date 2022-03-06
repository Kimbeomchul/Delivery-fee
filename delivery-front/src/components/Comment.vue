<template>
    <v-flex xs12 sm6 md3>
        <v-text-field label="댓글을 입력해주세요." type="text" hide-details outlined dense v-model="comment">
            <template #append>
                <v-fade-transition leave-absolute>
                    <v-btn class="pt-1" icon x-small elevation="0" @click="postComment"
                        ><img width="24" height="24" src="@/assets/btn.png" alt="btn" />
                    </v-btn>
                </v-fade-transition>
            </template>
        </v-text-field>
    </v-flex>
</template>

<script>
import request from "@/request";

export default {
    name: "comment-component",

    data: () => ({
        comment: "",
        loading: false,
        dialog: false,
        //
    }),
    created: function () {},
    mounted: function () {},
    computed: {
        userId() {
            return this.$store.state.userInfo.user_id;
        },
    },
    methods: {
        postComment: async function () {
            const data = {
                content: this.comment,
                party: this.$route.params.partyId,
                user: this.userId,
            };
            try {
                const result = await request(`/parties/${this.$route.params.partyId}/comments/`, "POST", data);

                if (result.status == 201) {
                    this.$store.dispatch("pushToComments", result.data);
                    this.comment = "";
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
