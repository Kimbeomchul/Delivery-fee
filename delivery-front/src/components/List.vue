<template>
    <div>
        <v-btn
            router-link
            :to="{ name: 'map' }"
            outlined
            color="#52D4DC"
            elevation="1"
            large
            block
            class="xl rounded-lg"
        >
            <div class="black--text font-weight-black" style="font-size: 1.2em">경기도 과천시</div>
        </v-btn>

        <div class="black--text font-weight-black pt-10 pb-2" style="font-size: 1.2em">참여중</div>
        <v-divider class="pb-5"></v-divider>

        <div class="pt-5 pb-3">
            <v-card class="rounded-lg" elevation="2" outline height="150">
                <v-row>
                    <v-col class="pt-4 pl-8">
                        <v-img
                            class="rounded-lg"
                            width="100"
                            height="100"
                            src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
                        ></v-img>
                        <div class="pl-4 pt-1 font-weight-black">10시 35분</div>
                    </v-col>

                    <v-col class="text-left">
                        <div class="font-weight-black pr-4 text-right" style="font-size: 1.2em">근처 파티 구해요</div>

                        <div class="grey--text font-weight-bold pr-4" style="font-size: 0.8em; text-align: right">
                            #치킨 #피자 #짜장면
                        </div>

                        <div class="grey--text font-weight-bold pr-4 pt-3" style="font-size: 0.8em; text-align: right">
                            제주도 제주시 해안동
                        </div>

                        <div class="grey--text font-weight-medium pr-4" style="font-size: 0.8em; text-align: right">
                            108m
                        </div>
                    </v-col>
                </v-row>
            </v-card>
        </div>

        <div class="black--text font-weight-black pt-5 pb-2" style="font-size: 1.2em">대기중</div>
        <v-divider class="pb-5"></v-divider>

        <div v-for="(party, index) in parties" v-bind:key="index" class="pt-5 pb-3">
            <v-card
                router-link
                :to="{ name: 'detail', params: { partyId: party.id } }"
                class="rounded-lg"
                elevation="2"
                outline
                height="150"
            >
                <v-row>
                    <v-col class="pt-4 pl-8">
                        <v-img
                            class="rounded-lg"
                            width="100"
                            height="100"
                            src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
                        ></v-img>
                        <div class="pl-4 pt-1 font-weight-black">
                            {{ datetimeToReadable(party.order_time) }}
                        </div>
                    </v-col>

                    <v-col class="text-left">
                        <div class="font-weight-black pr-4 text-right" style="font-size: 1.2em">
                            {{ party.title }}
                        </div>

                        <div class="grey--text font-weight-bold pr-4" style="font-size: 0.8em; text-align: right">
                            {{ party.tags }}
                        </div>

                        <div class="grey--text font-weight-bold pr-4 pt-3" style="font-size: 0.8em; text-align: right">
                            제주도 제주시 해안동
                        </div>

                        <div class="grey--text font-weight-medium pr-4" style="font-size: 0.8em; text-align: right">
                            108m
                        </div>
                    </v-col>
                </v-row>
            </v-card>
        </div>
    </div>
</template>

<script>
import request from "@/request";
import dayjs from "dayjs";
import "dayjs/locale/ko";
dayjs.locale("ko");

export default {
    name: "list-component",
    data: () => ({
        num: 7,
        //
    }),
    created: function () {
        this.addUserInfo();
        this.getPartyList();
    },
    mounted: function () {},
    computed: {
        parties() {
            return this.$store.state.parties;
        },
    },
    methods: {
        datetimeToReadable(time) {
            return dayjs(time).format("HH시 mm분");
        },
        addUserInfo() {
            if (!this.$store.state.userInfo) {
                this.$store.commit("addUserInfo", this.$route.query);

                // clear query param
                this.$router.push(this.$route.path).catch((err) => {
                    // Ignore the vuex err regarding  navigating to the page they are already on.
                    if (
                        err.name !== "NavigationDuplicated" &&
                        !err.message.includes("Avoided redundant navigation to current location")
                    ) {
                        // But print any other errors to the console
                        console.log(err);
                    }
                });
                // this.$router.replace({ query: null });
            }
        },
        getPartyList: async function () {
            try {
                const result = await request("/parties", "GET");

                if (result.status === 200) {
                    this.$store.commit("changeParties", result.data);
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
