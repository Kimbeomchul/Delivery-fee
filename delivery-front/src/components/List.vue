<template>
    <div>
        <v-btn :to="{ name: 'map' }" outlined color="#52D4DC" elevation="1" large block class="xl rounded-lg">
            <v-icon small>mdi-crosshairs-gps</v-icon>
            <v-spacer></v-spacer>
            <div class="black--text font-weight-black" style="font-size: 1.2em">경기도 과천시</div>
            <v-spacer></v-spacer>
        </v-btn>

        <div class="black--text font-weight-black pt-6 pb-2" style="font-size: 1.2em">참여중</div>
        <v-divider class="pb-5"></v-divider>

        <div class="pt-5 pb-3" v-if="userInfo.participated">
            <v-card
                :to="{ name: 'detail', params: { partyId: userInfo.participated.party.id } }"
                class="rounded-lg"
                elevation="10"
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
                            {{ datetimeToReadable(userInfo.participated.party.order_time) }}
                        </div>
                    </v-col>

                    <v-col class="text-left">
                        <div class="font-weight-black pr-4 text-right" style="font-size: 1.2em">
                            {{ userInfo.participated.party.title }}
                        </div>

                        <div class="grey--text font-weight-bold pr-4" style="font-size: 0.8em; text-align: right">
                            {{ tagsToReadable(userInfo.participated.party.tags) }}
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

        <div v-for="(party, index) in parties" :key="index" class="pt-5 pb-3">
            <v-card
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
                            {{ tagsToReadable(party.tags) }}
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
        <infinite-loading @infinite="infiniteHandler" spinner="waveDots"></infinite-loading>
    </div>
</template>

<script>
import request from "@/request";
import dayjs from "dayjs";
import "dayjs/locale/ko";
dayjs.locale("ko");
import InfiniteLoading from "vue-infinite-loading";

export default {
    name: "list-component",
    components: {
        InfiniteLoading,
    },
    data: () => ({
        num: 7,
        page: 2,
        //
    }),
    created: function () {
        this.addUserInfo();
        this.getPartyList();
    },
    mounted: function () {},
    computed: {
        userInfo() {
            return this.$store.state.userInfo;
        },
        parties() {
            return this.$store.state.parties;
        },
    },
    methods: {
        tagsToReadable(tags) {
            return tags ? "#" + tags.join(" #") : "#";
        },
        datetimeToReadable(time) {
            return dayjs(time).format("HH시 mm분");
        },
        addUserInfo() {
            if (!this.$store.state.userInfo) {
                this.$store.dispatch("addUserInfo", this.$route.query);

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
                const result = await request("/parties/", "GET");

                if (result.status === 200) {
                    this.$store.dispatch("changeParties", result.data["results"]);
                } else {
                    console.log(result);
                }
            } catch (error) {
                console.log(error);
            }
        },
        infiniteHandler($state) {
            console.log("1231");
            const EACH_LEN = 30;
            const baseURL = "http://localhost:8000/api/v1";

            fetch(`${baseURL}/parties/?page=` + this.page, {
                method: "get",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Bearer ${this.userInfo.access_token}`,
                },
            })
                .then((resp) => {
                    return resp.json();
                })
                .then((data) => {
                    setTimeout(() => {
                        if (data["count"] >= 0) {
                            // this.topicData = this.topicData.concat(data);
                            // this.$store.dispatch("concatToParties", data["results"]);
                            this.$store.dispatch("pushToParties", data["results"]);
                            console.log(data["results"]);
                            console.log(this.parties);
                            $state.loaded();
                            this.page += 1;

                            $state.complete();
                            // 끝 지정(No more data) - 데이터가 EACH_LEN개 미만이면
                            // if (data["count"] < EACH_LEN) {
                            //     $state.complete();
                            // }
                        } else {
                            // 끝 지정(No more data)
                            $state.complete();
                        }
                    }, 1000);
                })
                .catch((err) => {
                    console.error(err);
                });
        },
    },
};
</script>
