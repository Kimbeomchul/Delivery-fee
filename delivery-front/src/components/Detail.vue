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
                    <v-menu bottom left v-if="userId == comment.user">
                        <template #activator="{ on, attrs }">
                            <v-btn icon v-bind="attrs" v-on="on">
                                <v-icon small>mdi-dots-vertical</v-icon>
                            </v-btn>
                        </template>

                        <v-list>
                            <v-list-item v-for="(item, i) in items" :key="i">
                                <v-list-item-title v-text="item.title" @click.stop="handleItemAction(item.title)">
                                </v-list-item-title>
                            </v-list-item>
                        </v-list>

                        <v-dialog v-model="deleteDialog" max-width="300">
                            <v-card>
                                <v-card-title class="text-body2"> 댓글을 삭제하시겠습니까? </v-card-title>
                                <v-divider></v-divider>

                                <v-card-actions>
                                    <v-btn class="text-h5" color="#52D4DC" text @click="deleteDialog = false">
                                        아니요
                                    </v-btn>
                                    <v-spacer></v-spacer>
                                    <v-btn
                                        class="text-h5 font-weight-bold"
                                        color="#52D4DC"
                                        text
                                        @click="deleteCommeent(comment.id, index)"
                                    >
                                        삭제하기
                                    </v-btn>
                                </v-card-actions>
                            </v-card>
                        </v-dialog>
                        <v-dialog v-model="editDialog" max-width="300">
                            <v-card>
                                <v-card-title class="text-body2"> 파티를 수정하시겠습니까? </v-card-title>
                                <v-card-text class="text-caption">
                                    주문하고 싶은 시간은 현재시간 이후로만 설정할 수 있습니다.
                                </v-card-text>
                                <v-divider></v-divider>

                                <v-card-actions>
                                    <v-btn class="text-h5" color="green darken-1" text @click="editDialog = false">
                                        아니요
                                    </v-btn>
                                    <v-spacer></v-spacer>
                                    <v-btn
                                        class="text-h5 font-weight-bold"
                                        color="green darken-1"
                                        text
                                        @click="goWrite()"
                                    >
                                        수정하기
                                    </v-btn>
                                </v-card-actions>
                            </v-card>
                        </v-dialog>
                    </v-menu>
                </v-col>
            </v-row>
            <div class="pb-2 pl-5 pr-5 text-body-2">{{ comment.content }}</div>
        </div>
        <infinite-loading @infinite="infiniteHandler" spinner="waveDots">
            <div slot="no-more"></div>
            <div slot="no-results">아직 파티가 없습니다. 파티를 생성해보세요.</div>
        </infinite-loading>
        <br />
        <br />
    </div>
</template>

<script>
import request from "@/request";
import InfiniteRequest from "@/infinite-request";
import InfiniteLoading from "vue-infinite-loading";
import dayjs from "dayjs";
import "dayjs/locale/ko";
dayjs.locale("ko");

export default {
    name: "detail-component",
    components: {
        InfiniteLoading,
    },
    data: () => ({
        num: 7,
        page: "",
        deleteDialog: false,
        editDialog: false,
        items: [{ title: "삭제" }, { title: "수정 (수정을 어느 창에서 해야할지?)" }],
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
        comments() {
            return this.$store.state.comments;
        },
        userId() {
            return this.$store.state.userInfo.user_id;
        },
    },
    methods: {
        tagsToReadable(tags) {
            return tags ? "#" + tags.join(" #") : "#";
        },
        datetimeToReadable(time) {
            return dayjs(time).format("HH시 mm분");
        },
        getPartyDetail: async function () {
            try {
                const result = await request(`/parties/${this.$route.params.partyId}/`, "GET");
                if (result.status === 200) {
                    this.$store.dispatch("changeParty", result.data);
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
                    if (result.data["next"]) {
                        this.page = 2;
                    }
                    this.$store.dispatch("changeComments", result.data["results"]);
                } else {
                    console.log(result);
                }
            } catch (error) {
                console.log(error);
            }
        },
        handleItemAction(title) {
            switch (title) {
                case "수정":
                    this.editDialog = true;
                    break;
                case "삭제":
                    this.deleteDialog = true;
                    break;
            }
        },
        deleteCommeent: async function (commentId, commentIndex) {
            console.log(commentIndex);
            try {
                const result = await request(`/parties/${this.$route.params.partyId}/comments/${commentId}/`, "DELETE");
                if (result.status === 204) {
                    this.deleteDialog = false;
                    this.$store.dispatch("popToComments", commentIndex);
                } else {
                    this.deleteDialog = false;
                }
            } catch (error) {
                console.log(error);
            }
        },
        infiniteHandler: async function ($state) {
            await InfiniteRequest(
                $state,
                `/parties/${this.$route.params.partyId}/comments/`,
                this.page,
                "pushToComments"
            );
        },
    },
};
</script>
