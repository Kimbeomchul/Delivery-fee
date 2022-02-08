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
    </div>
</template>

<script>
export default {
    name: "write-component",
    data: () => ({
        sheet: false,
        ex1: { label: "color", val: 25, color: "orange darken-3" },
        ex2: { label: "track-color", val: 75, color: "green lighten-1" },
        ex3: { val: 0, color: "#52D4DC" },
    }),
};
</script>
