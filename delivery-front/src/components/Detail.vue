<template>
    <div>
        <div>
            <v-row>
                <v-col cols="8" class="text-right">
                    <div class="font-weight-black pt-4 pr-4" style="font-size: 1.2em">
                        {{ party.title }}
                    </div>

                    <div class="grey--text font-weight-bold pr-4" style="font-size: 0.8em; text-align: right">
                        {{ tagsToReadable(party.tags) }}
                    </div>

                    <div class="grey--text font-weight-bold pr-4" style="font-size: 0.8em; text-align: right">
                        제주도 제주시 해안동
                    </div>

                    <div class="grey--text font-weight-medium pr-4" style="font-size: 0.8em; text-align: right">
                        108m
                    </div>
                </v-col>
                <v-col cols="4" class="pt-4">
                    <v-img
                        class="rounded-lg"
                        width="100"
                        height="100"
                        src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
                    ></v-img>
                    <div class="text-center pt-1 font-weight-black">
                        {{ datetimeToReadable(party.order_time) }}
                    </div>
                </v-col>
            </v-row>
        </div>

        <div class="pt-1 font-weight-black" style="color: #52d4dc">내용</div>
        <v-text-field class="text-center" readonly :value="party.content"></v-text-field>

        <div class="pb-5 pt-1 font-weight-black" style="color: #52d4dc">댓글</div>
        <v-divider class="pb-5"></v-divider>

        <div class="pb-3 pl-3 pr-3" v-for="(comment, index) in comments" :key="index">
            <v-row>
                <v-col cols="10">
                    <div class="font-weight-black text-body-2">
                        {{ comment.user }} -> 임시로 유저 아이디
                        <span class="text-caption">· 43분전 </span>
                    </div>
                </v-col>
                <v-col cols="2">
                    <v-menu bottom left>
                        <template #activator="{ on, attrs }">
                            <v-btn icon v-bind="attrs" v-on="on">
                                <v-icon small>mdi-dots-vertical</v-icon>
                            </v-btn>
                        </template>

                        <v-list>
                            <v-list-item v-for="(item, i) in items" :key="i">
                                <v-list-item-title>{{ item.title }}</v-list-item-title>
                            </v-list-item>
                        </v-list>
                    </v-menu>
                </v-col>
            </v-row>
            <div class="pb-2 pl-5 pr-5 text-body-2">{{ comment.content }}</div>
        </div>
    </div>
</template>

<script>
import request from "@/request";
import dayjs from "dayjs";
import "dayjs/locale/ko";
dayjs.locale("ko");

export default {
    name: "detail-component",
    data: () => ({
        num: 7,
        items: [{ title: "Click Me" }, { title: "Click Me" }, { title: "Click Me" }, { title: "Click Me 2" }],
        comments: [],
        //
    }),
    created: function () {
        this.getPartyDetail();
        this.getCommentList();
    },
    mounted: function () {},
    computed: {
        party() {
            return this.$store.state.party;
        },
    },
    methods: {
        tagsToReadable(tags) {
            return "#" + tags.join(" #");
        },
        datetimeToReadable(time) {
            return dayjs(time).format("HH시 mm분");
        },
        getPartyDetail: async function () {
            try {
                const result = await request(`/parties/${this.$route.params.partyId}/`, "GET");
                if (result.status === 200) {
                    this.$store.commit("changeParty", result.data);
                } else {
                    console.log(result);
                }
            } catch (error) {
                console.log(error);
            }
        },
        getCommentList: async function () {
            try {
                const result = await request(`/parties/${this.$route.params.partyId}/comments/`, "GET");
                if (result.status === 200) {
                    this.comments = result.data;
                    console.log(this.comments);
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
