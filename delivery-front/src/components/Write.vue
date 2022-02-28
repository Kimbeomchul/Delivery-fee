<template>
    <div>
        <div class="font-weight-black" style="color: #52d4dc">제목</div>
        <v-text-field v-model="title" placeholder="제목을 입력해주세요."></v-text-field>
        <div class="font-weight-black" style="color: #52d4dc">종류</div>
        <v-item-group multiple max="3" v-model="selectedTags">
            <v-item v-for="(item, index) in tags" :key="index" :value="item" v-slot="{ active, toggle }">
                <v-chip small class="ma-1" active-class="blue--text" :input-value="active" @click="toggle">
                    # {{ item }}
                </v-chip>
            </v-item>
        </v-item-group>
        <br />
        <div class="font-weight-black" style="color: #52d4dc">주문하고 싶은 시간대를 선택해주세요</div>
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
            {{ orderTime.format("A HH시 mm분") }}
        </div>

        <div class="font-weight-black" style="color: #52d4dc">내용</div>
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
                <div class="font-weight-black" style="color: #52d4dc">내위치</div>
            </v-col>
            <v-col cols="9">
                <div class="text-caption font-weight-black text-right">경기도 과천시 관문로 106 104동 1010호</div>
            </v-col>
        </v-row>
        <br />
        <v-btn
            v-if="!$route.query.edit"
            bottom
            block
            x-large
            rounded
            color="#52D4DC"
            dark
            class="font-weight-bold"
            style="font-size: 1.02em"
            @click="createParty()"
        >
            작성하기
        </v-btn>
        <v-btn
            v-else
            bottom
            block
            x-large
            rounded
            color="#52D4DC"
            dark
            class="font-weight-bold"
            style="font-size: 1.02em"
            @click="editParty()"
        >
            수정하기
        </v-btn>
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
        selectedTags: "",
        timerSlider: { val: 0, color: "#52D4DC" },
        editTimerSlider: { val: 0, color: "#52D4DC" },
    }),
    created: function () {
        this.allowEditParty();
    },
    mounted: function () {},
    computed: {
        tags() {
            return this.$store.state.foodTags;
        },
        userInfo() {
            return this.$store.state.userInfo.user_id;
        },
        orderTime() {
            if (this.isBefore && this.isEdit) {
                return dayjs(this.party.order_time).add(this.timerSlider.val - this.editTimerSlider.val, "minute");
            } else {
                return dayjs().add(this.timerSlider.val, "minute");
            }
        },
        party() {
            return this.$store.state.party;
        },
        isBefore() {
            return !dayjs().isAfter(this.party.order_time);
        },
        isEdit() {
            return this.$route.query.edit;
        },
    },
    methods: {
        createParty: async function () {
            const data = {
                title: this.title,
                tags: this.selectedTags,
                order_time: this.orderTime.format(),
                content: this.content,
                user: this.userInfo,
            };
            try {
                const result = await request("/parties/", "POST", data);

                if (result.status === 201) {
                    this.$store.commit("pushToParties", result.data);
                    this.$router.go(-1);
                } else {
                    console.log(result);
                }
            } catch (error) {
                console.log(error);
            }
        },
        editParty: async function () {
            const data = {
                title: this.title,
                tags: this.selectedTags,
                order_time: this.orderTime.format(),
                content: this.content,
            };
            try {
                const result = await request(`/parties/${this.party.id}/`, "PATCH", data);

                console.log(result.status);

                if (result.status === 200) {
                    this.$router.go(-1);
                } else {
                    console.log(result);
                }
            } catch (error) {
                console.log(error);
            }
        },
        allowEditParty: function () {
            if (this.isEdit) {
                this.title = this.party.title;
                this.content = this.party.content;
                this.selectedTags = this.party.tags;
                const nowDate = dayjs();
                if (this.isBefore) {
                    const diffMinuteAbs = Math.abs(nowDate.diff(this.party.order_time, "minute"));
                    this.editTimerSlider.val = diffMinuteAbs;
                    this.timerSlider.val = diffMinuteAbs;
                }
            }
        },
    },
    watch: {},
};
</script>
