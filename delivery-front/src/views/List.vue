<template>
    <v-container class="spacing-playground pa-6">
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
            <div class="black--text font-weight-black" style="font-size:1.2em">
                경기도 과천시
            </div>
        </v-btn>

        <div class="black--text font-weight-black pt-10 pb-2" style="font-size:1.2em">
            참여중
        </div>
        <v-divider class="pb-5"></v-divider>

        <div class="pt-5 pb-3">
            <v-card
                router-link
                :to="{ name: 'detail' }"
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
                            10시 35분
                        </div>
                    </v-col>

                    <v-col class="text-left">
                        <div class="font-weight-black pt-4" style="font-size:1.2em">
                            근처 파티 구해요
                        </div>

                        <div
                            class="grey--text font-weight-bold pr-4"
                            style="font-size:0.8em; text-align:right"
                        >
                            #치킨 #피자 #짜장면
                        </div>

                        <div
                            class="grey--text font-weight-bold pr-4 pt-3"
                            style="font-size:0.8em; text-align:right"
                        >
                            제주도 제주시 해안동
                        </div>

                        <div
                            class="grey--text font-weight-medium pr-4"
                            style="font-size:0.8em; text-align:right"
                        >
                            108m
                        </div>
                    </v-col>
                </v-row>
            </v-card>
        </div>

        <div class="black--text font-weight-black pt-5 pb-2" style="font-size:1.2em">
            대기중
        </div>
        <v-divider class="pb-5"></v-divider>

        <div class="pt-5 pb-3">
            <v-card
                router-link
                :to="{ name: 'detail' }"
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
                            10시 35분
                        </div>
                    </v-col>

                    <v-col class="text-left">
                        <div class="font-weight-black pt-4" style="font-size:1.2em">
                            근처파티구해요
                        </div>

                        <div
                            class="grey--text font-weight-bold pr-4"
                            style="font-size:0.8em; text-align:right"
                        >
                            #치킨 #피자 #짜장면
                        </div>

                        <div
                            class="grey--text font-weight-bold pr-4 pt-3"
                            style="font-size:0.8em; text-align:right"
                        >
                            제주도 제주시 해안동
                        </div>

                        <div
                            class="grey--text font-weight-medium pr-4"
                            style="font-size:0.8em; text-align:right"
                        >
                            108m
                        </div>
                    </v-col>
                </v-row>
            </v-card>
        </div>

        <div class="pt-5 pb-3">
            <v-card
                router-link
                :to="{ name: 'detail' }"
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
                            10시 35분
                        </div>
                    </v-col>

                    <v-col class="text-left">
                        <div class="font-weight-black pt-4" style="font-size:1.2em">
                            근처파티구해요
                        </div>

                        <div
                            class="grey--text font-weight-bold pr-4"
                            style="font-size:0.8em; text-align:right"
                        >
                            #치킨 #피자 #짜장면
                        </div>

                        <div
                            class="grey--text font-weight-bold pr-4 pt-3"
                            style="font-size:0.8em; text-align:right"
                        >
                            제주도 제주시 해안동
                        </div>

                        <div
                            class="grey--text font-weight-medium pr-4"
                            style="font-size:0.8em; text-align:right"
                        >
                            108m
                        </div>
                    </v-col>
                </v-row>
            </v-card>
        </div>

        <div class="pt-5 pb-3">
            <v-card
                router-link
                :to="{ name: 'detail' }"
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
                            10시 35분
                        </div>
                    </v-col>

                    <v-col class="text-left">
                        <div class="font-weight-black pt-4" style="font-size:1.2em">
                            근처파티구해요
                        </div>

                        <div
                            class="grey--text font-weight-bold pr-4"
                            style="font-size:0.8em; text-align:right"
                        >
                            #치킨 #피자 #짜장면
                        </div>

                        <div
                            class="grey--text font-weight-bold pr-4 pt-3"
                            style="font-size:0.8em; text-align:right"
                        >
                            제주도 제주시 해안동
                        </div>

                        <div
                            class="grey--text font-weight-medium pr-4"
                            style="font-size:0.8em; text-align:right"
                        >
                            108m
                        </div>
                    </v-col>
                </v-row>
            </v-card>
        </div>

        <!-- 바텀 시트 -> 컴포넌트로 빼기. -->
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
                <v-text-field placeholder="제목을 입력해주세요."></v-text-field>
                <div class="font-weight-black" style="color:#52D4DC">
                    종류
                </div>
                <v-item-group multiple>
                    <v-item v-for="n in 8" :key="n" v-slot="{ active, toggle }">
                        <v-chip
                            small
                            class="ma-1"
                            active-class="blue--text"
                            :input-value="active"
                            @click="toggle"
                        >
                            # 음식 {{ n }}
                        </v-chip>
                    </v-item>
                </v-item-group>
                <br />
                <div class="font-weight-black" style="color:#52D4DC">
                    주문하고 싶은 시간대를 선택해주세요
                </div>
                <div class="text-right text-caption" v-text="ex3.val + '분후'">분후</div>
                <v-slider
                    v-model="ex3.val"
                    :thumb-color="ex3.color"
                    thumb-label="true"
                    step="10"
                    ticks
                    dense
                    hide-details
                ></v-slider>
                <div class="font-weight-black text-right text-body2">오후 10시 30분</div>

                <div class="font-weight-black" style="color:#52D4DC">
                    내용
                </div>
                <v-textarea
                    name="input-7-1"
                    rows="6"
                    filled
                    no-resize
                    placeholder="내용을 입력해주세요."
                    value=""
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
                    @click="sheet = !sheet"
                >
                    작성하기
                </v-btn>
            </v-sheet>
        </v-bottom-sheet>
    </v-container>
</template>

<script>
export default {
    data: () => ({
        sheet: false,
        ex1: { label: "color", val: 25, color: "orange darken-3" },
        ex2: { label: "track-color", val: 75, color: "green lighten-1" },
        ex3: { val: 0, color: "#52D4DC" },
    }),
};
</script>
