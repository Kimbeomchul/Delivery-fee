<template>
    <div>
        <v-bottom-sheet v-model="sheet">
            <template v-slot:activator="{ on, attrs }">
                <v-btn
                    fixed
                    bottom
                    right
                    absoluteclass="mx-2"
                    fab
                    dark
                    color="#52D4DC"
                    v-bind="attrs"
                    v-on="on"
                >
                    <v-icon dark>
                        mdi-plus
                    </v-icon>
                </v-btn>
            </template>
            <v-sheet class="pa-6 rounded-lg" height="700px">
                <div class="font-weight-black" style="color:#52D4DC">
                    제목
                </div>
                <v-text-field v-model="title" placeholder="제목을 입력해주세요."></v-text-field>
                <div class="font-weight-black" style="color:#52D4DC">
                    종류
                </div>
                <v-item-group multiple max="3" v-model="selectedTags">
                    <v-item
                        v-for="(item, index) in tags"
                        :key="index"
                        :value="item"
                        v-slot="{ active, toggle }"
                    >
                        <v-chip
                            small
                            class="ma-1"
                            active-class="blue--text"
                            :input-value="active"
                            @click="toggle"
                        >
                            # {{ item }}
                        </v-chip>
                    </v-item>
                </v-item-group>
                <br />
                <div class="font-weight-black" style="color:#52D4DC">
                    주문하고 싶은 시간대를 선택해주세요
                </div>
                <div class="text-right text-caption" v-text="timerSlider.val + '분후'">분후</div>
                <v-slider
                    v-model="timerSlider.val"
                    :thumb-color="timerSlider.color"
                    :thumb-label="true"
                    step="10"
                    max="120"
                    ticks
                    dense
                    hide-details
                ></v-slider>
                <div class="font-weight-black text-right text-body2">
                    {{ OrderTime.format("A HH시 mm분") }}
                </div>

                <div class="font-weight-black" style="color:#52D4DC">
                    내용
                </div>
                <v-textarea
                    name="input-7-1"
                    rows="6"
                    filled
                    no-resize
                    placeholder="내용을 입력해주세요."
                    v-model="content"
                ></v-textarea>
                <v-row>
                    <v-col cols="3">
                        <div class="font-weight-black" style="color:#52D4DC">
                            내위치
                        </div>
                    </v-col>
                    <v-col cols="9">
                        <div class="text-caption font-weight-black text-right">
                            경기도 과천시 관문로 106 104동 1010호
                        </div>
                    </v-col>
                </v-row>
                <br />
                <v-btn
                    bottom
                    block
                    x-large
                    rounded
                    color="#52D4DC"
                    dark
                    class="font-weight-bold"
                    style="font-size:1.02em"
                    @click="createParty()"
                >
                    작성하기
                </v-btn>
            </v-sheet>
        </v-bottom-sheet>
    </div>
</template>

<script>
import request from "@/request";
import dayjs from "dayjs";
import "dayjs/locale/ko";
dayjs.locale("ko");

export default {
    name: "write-component",
    data: () => ({
        title: "",
        content: "",
        sheet: false,
        selectedTags: "",
        timerSlider: { val: 0, color: "#52D4DC" },
    }),
    computed: {
        tags() {
            return this.$store.state.foodTags;
        },
        userInfo() {
            return this.$store.state.userInfo.user_id;
        },
        OrderTime() {
            const date = dayjs().add(this.timerSlider.val, "minute");
            return date;
        },
    },
    methods: {
        createParty: async function() {
            const data = {
                title: this.title,
                tags: this.selectedTags,
                order_time: this.OrderTime.format(),
                content: this.content,
                // HACK: user에 대한 정보를 소셜 로그인 성공 후 vuex에 넣어버려야함. 어케해야돼
                user: this.userInfo,
            };
            console.log(typeof this.userInfo);
            console.log(data);
            try {
                const result = await request("/parties/", "POST", data);

                if (result.status === 200) {
                    console.log("제대로 들어감");
                } else {
                    console.log(result);
                }
            } catch (error) {
                console.log(error);
            }

            // console.log(this.title);
            // console.log(this.content);
            // console.log(this.selectedTags);
            // console.log(this.OrderTime.format());
            this.sheet = !this.sheet;
        },
    },
};
</script>
