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
                    <v-col cols="4" class="pt-3 pl-6 pr-0">
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

                    <v-col cols="8" class="text-left">
                        <div class="font-weight-black pr-4 text-right" style="font-size: 1.2em">
                            {{ userInfo.participated.party.title }}
                        </div>

                        <div
                            class="grey--text text--darken-1 font-weight-bold pr-4 pt-2"
                            style="font-size: 0.8em; text-align: right"
                        >
                            {{ tagsToReadable(userInfo.participated.party.tags) }}
                        </div>

                        <div
                            class="grey--text text--darken-1 font-weight-bold pr-4 pt-1"
                            style="font-size: 0.8em; text-align: right"
                        >
                            <v-icon color="#52D4DC" small>mdi-map-marker-radius-outline</v-icon>
                            제주도 제주시 해안동
                        </div>
                        <br />
                        <div
                            class="grey--text text--darken-1 font-weight-medium pr-4"
                            style="font-size: 0.8em; text-align: right"
                        >
                            {{ userInfo.participated.party.user_name }}, 108m
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
                    <v-col cols="4" class="pt-3 pl-6 pr-0">
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

                    <v-col cols="8" class="text-left">
                        <div class="font-weight-black pr-4 text-right" style="font-size: 1.2em">
                            {{ party.title }}
                        </div>

                        <div
                            class="grey--text text--darken-1 font-weight-bold pr-4 pt-1"
                            style="font-size: 0.8em; text-align: right"
                        >
                            {{ tagsToReadable(party.tags) }}
                        </div>

                        <div
                            class="grey--text text--darken-1 font-weight-bold pr-4 pt-1"
                            style="font-size: 0.8em; text-align: right"
                        >
                            <v-icon color="#52D4DC" small>mdi-map-marker-radius-outline</v-icon>
                            제주도 제주시 해안동
                        </div>
                        <br />
                        <div
                            class="grey--text text--darken-1 font-weight-medium pr-4"
                            style="font-size: 0.8em; text-align: right"
                        >
                            {{ party.user_name }}, 108m
                        </div>
                    </v-col>
                </v-row>
            </v-card>
        </div>
        <infinite-loading @infinite="infiniteHandler" spinner="waveDots">
            <div slot="no-more"></div>
            <div slot="no-results">아직 파티가 없습니다. 파티를 생성해보세요.</div>
        </infinite-loading>
    </div>
</template>

<script>
import request from "@/request";
// import InfiniteRequest from "@/infinite-request";
import InfiniteLoading from "vue-infinite-loading";
import dayjs from "dayjs";
import "dayjs/locale/ko";
dayjs.locale("ko");

export default {
    name: "list-component",
    components: {
        InfiniteLoading,
    },
    data: () => ({
        num: 7,
        page: 2,
        isNeedPagination: false,
        //
    }),
    created: function () {
        this.addUserInfo();
        this.addParticipatedInfo();
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
            if (this.$store.state.userInfo) return;

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
        },
        getPartyList: async function () {
            try {
                const result = await request("/parties/", "GET");

                if (result.status === 200) {
                    if (result.data["next"]) {
                        this.isNeedPagination = true;
                    }
                    this.$store.dispatch("changeParties", result.data["results"]);
                } else {
                    console.log(result);
                }
            } catch (error) {
                console.log(error);
            }
        },
        infiniteHandler: async function ($state) {
            // await InfiniteRequest($state, "/parties/", this.page, "pushToParties");

            if (!this.isNeedPagination) {
                $state.complete();
                return;
            }
            this.computePageOnRefresh();

            const baseURL = "http://localhost:8000/api/v1";
            const action = "/parties/";

            await fetch(`${baseURL}${action}?page=` + this.page, {
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
                        if (data["results"]) {
                            data["results"]["infinite"] = true;
                            this.$store.dispatch("pushToParties", data["results"]);
                            $state.loaded();
                            this.page += 1;

                            if (!data["next"]) {
                                this.$store.dispatch("changeLoadingStatusParties", true);
                                $state.complete();
                            }
                        } else {
                            this.$store.dispatch("changeLoadingStatusParties", true);
                            // 끝 지정(No more data)
                            $state.complete();
                        }
                    }, 500);
                })
                .catch((err) => {
                    console.error(err);
                });
        },
        computePageOnRefresh() {
            if (this.page > 2) {
                const pageSize = 30;
                this.page = Math.ceil(this.parties.length / pageSize) + 1;
            }
        },
        addParticipatedInfo: async function () {
            if (this.$store.state.userInfo.participant) return;

            try {
                const result = await request(`/users/${this.userInfo.user_id}/`, "GET");
                if (result.status === 200) {
                    if (result.data.participant) {
                        const { id, party } = result.data.participant;
                        this.$store.dispatch("pushParticipationStatus", { id: id, party: party });
                    }
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
