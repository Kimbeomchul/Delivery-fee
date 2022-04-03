<template>
    <div>
        <div>
            <v-row>
                <v-col cols="8" class="text-right">
                    <div class="font-weight-black pr-4" style="font-size: 1.2em">
                        {{ party.title }}
                    </div>

                    <div
                        class="grey--text text--darken-1 font-weight-bold pr-4 pt-2"
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
                        class="grey--text text--darken-1 font-weight-medium pr-4 pt-1"
                        style="font-size: 0.8em; text-align: right"
                    >
                        {{ party.user_name }}, 108m
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
                        {{ comment.user_name }}
                        <span class="text-caption">· {{ computeHowmanyTimeAgo(comment.created_at) }}</span>
                    </div>
                </v-col>
                <v-col cols="2">
                    <v-menu bottom left v-if="userInfo.user_id == comment.user">
                        <template #activator="{ on, attrs }">
                            <v-btn icon v-bind="attrs" v-on="on">
                                <v-icon small>mdi-dots-vertical</v-icon>
                            </v-btn>
                        </template>

                        <v-list>
                            <v-list-item v-for="(item, i) in items" :key="i">
                                <v-list-item-title
                                    v-text="item.title"
                                    @click.stop="handleItemAction(item.title, comment.content)"
                                >
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

                        <!-- edit comment dialog part -->

                        <v-dialog
                            v-model="editCommentDialog"
                            fullscreen
                            hide-overlay
                            transition="dialog-bottom-transition"
                        >
                            <v-card>
                                <v-toolbar elevation="0" dense>
                                    <v-btn icon style="color: #52d4dc" @click="editCommentDialog = false">
                                        <v-icon color="black">mdi-close</v-icon>
                                    </v-btn>
                                    <v-spacer></v-spacer>
                                    <v-toolbar-title class="font-weight-black" style="color: #52d4dc"
                                        >댓글 수정
                                    </v-toolbar-title>
                                    <v-spacer></v-spacer>
                                    <v-toolbar-items>
                                        <v-btn
                                            class="pt-1 ml-3"
                                            icon
                                            x-small
                                            elevation="0"
                                            @click="editComment(comment.content, comment.id, index)"
                                            ><img width="24" height="24" src="@/assets/btn.png" alt="btn" />
                                        </v-btn>
                                    </v-toolbar-items>
                                </v-toolbar>

                                <v-form ref="form" v-model="valid" lazy-validation>
                                    <v-textarea
                                        name="input-7-1"
                                        rows="8"
                                        filled
                                        no-resize
                                        v-model="editableComment"
                                        :rules="contentRules"
                                        placeholder="댓글을 입력해주세요."
                                    >
                                    </v-textarea>
                                </v-form>
                            </v-card>
                        </v-dialog>
                    </v-menu>
                </v-col>
            </v-row>
            <div class="pb-2 pl-5 pr-5 text-body-2">{{ comment.content }}</div>
        </div>
        <infinite-loading @infinite="infiniteHandler" spinner="waveDots">
            <div slot="no-more"></div>
            <div slot="no-results"></div>
        </infinite-loading>
        <br />
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
    name: "detail-component",
    components: {
        InfiniteLoading,
    },
    data: () => ({
        num: 7,
        page: 2,
        isNeedPagination: false,
        editableComment: "",
        deleteDialog: false,
        editCommentDialog: false,
        items: [{ title: "삭제" }, { title: "수정" }],
        contentRules: [(value) => !!value || "댓글을 입력해 주세요."],
        valid: true,
    }),
    created: function () {
        this.getPartyDetail();
        this.getCommentList();

        this.$store.dispatch("changeLoadingStatusComments", false);
    },
    mounted: function () {},
    computed: {
        party() {
            return this.$store.state.party;
        },
        comments() {
            return this.$store.state.comments;
        },
        userInfo() {
            return this.$store.state.userInfo;
        },
    },
    methods: {
        tagsToReadable(tags) {
            return tags ? "#" + tags.join(" #") : "#";
        },
        datetimeToReadable(time) {
            return dayjs(time).format("HH시 mm분");
        },
        computeHowmanyTimeAgo(time) {
            const nowDate = dayjs();
            let diffMinute = nowDate.diff(time, "minute");

            if (diffMinute >= 60 && diffMinute < 1440) {
                diffMinute = Math.floor(diffMinute / 60);
                return diffMinute + "시간전";
            } else if (diffMinute >= 1440) {
                console.log("asdf");
                diffMinute = Math.floor(diffMinute / 1440);
                return diffMinute + "일전";
            }

            return diffMinute + "분전";
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
                        this.isNeedPagination = true;
                    }
                    this.$store.dispatch("changeComments", result.data["results"]);
                } else {
                    console.log(result);
                }
            } catch (error) {
                console.log(error);
            }
        },
        handleItemAction(title, content) {
            switch (title) {
                case "수정":
                    this.editableComment = content;
                    this.editCommentDialog = true;
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
            // await InfiniteRequest(
            //     $state,
            //     `/parties/${this.$route.params.partyId}/comments/`,
            //     this.page,
            //     "pushToComments"
            // );
            // await InfiniteRequest($state, "/parties/", this.page, "pushToParties");
            if (!this.isNeedPagination) {
                $state.complete();
                return;
            }
            this.computePageOnRefresh();

            const baseURL = "http://localhost:8000/api/v1";
            const action = `/parties/${this.$route.params.partyId}/comments/`;

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
                            this.$store.dispatch("pushToComments", data["results"]);
                            $state.loaded();

                            this.page += 1;

                            if (!data["next"]) {
                                this.$store.dispatch("changeLoadingStatusComments", true);
                                $state.complete();
                            }
                        } else {
                            this.$store.dispatch("changeLoadingStatusComments", true);
                            // 끝 지정(No more data)
                            $state.complete();
                        }
                    }, 500);
                })
                .catch((err) => {
                    console.error(err);
                });
        },
        editComment: async function (content, id, index) {
            const validate = this.$refs.form[0].validate();
            if (!validate) return;

            const data = {
                content: this.editableComment,
            };
            try {
                const result = await request(`/parties/${this.$route.params.partyId}/comments/${id}/`, "PATCH", data);

                if (result.status == 200) {
                    this.$store.dispatch("editComment", { index: index, content: this.editableComment });
                    this.editCommentDialog = false;
                } else {
                    console.log(result);
                }
            } catch (error) {
                console.log(error);
            }
        },
        computePageOnRefresh() {
            if (this.page > 2) {
                const pageSize = 30;
                this.page = Math.ceil(this.comments.length / pageSize) + 1;
            }
        },
    },
};
</script>
