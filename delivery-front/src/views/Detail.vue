<template>
    <v-container class="spacing-playground pa-6">
        <div>
            <v-row>
                <v-col cols="8" class="text-left">
                    <div class="font-weight-black pt-4" style="font-size:1.2em">
                        롯데캐슬 치킨 먹을사람1
                    </div>

                    <div
                        class="grey--text font-weight-bold pr-4"
                        style="font-size:0.8em; text-align:right"
                    >
                        #치킨 #피자 #짜장면
                    </div>

                    <div
                        class="grey--text font-weight-bold pr-4"
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
                <v-col cols="4" class="pt-4 ">
                    <v-img
                        class="rounded-lg"
                        width="100"
                        height="100"
                        src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
                    ></v-img>
                    <div class="text-center pt-1 font-weight-black">
                        10시 35분
                    </div>
                </v-col>
            </v-row>
        </div>

        <div class="pt-1 font-weight-black">
            내용
        </div>
        <v-text-field
            class="text-center"
            placeholder="치킨을 시키려구 합니다. 맛나느치킨"
            value="치킨을 시키려구 합니다. 맛나느치킨"
        ></v-text-field>

        <div class="pb-5 pt-1 font-weight-black">
            댓글
        </div>
        <v-divider class="pb-5"></v-divider>

        <v-row class="">
            <v-col cols="4">
                <div class="font-weight-black text-body-2">
                    거친 삑삑도요
                </div>
            </v-col>
            <v-col cols="6">
                <div class="text-caption">
                    · 43분전
                </div>
            </v-col>
            <v-col cols="2">
                <v-menu bottom left>
                    <template v-slot:activator="{ on, attrs }">
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
        <div class=" pb-5 text-body-2">
            오늘 관악산 다녀왔는데 정상에서먹은 내이름은 정상수~
        </div>
        <v-row class="">
            <v-col cols="4">
                <div class="font-weight-black text-body-2">
                    거친 삑삑도요
                </div>
            </v-col>
            <v-col cols="6">
                <div class="text-caption">
                    · 43분전
                </div>
            </v-col>
            <v-col cols="2">
                <v-menu bottom left>
                    <template v-slot:activator="{ on, attrs }">
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
        <div class=" pb-5 text-body-2">
            오늘 관악산 다녀왔는데 정상에서먹은 내이름은 정상수~
        </div>
        <v-row class="">
            <v-col cols="4">
                <div class="font-weight-black text-body-2">
                    거친 삑삑도요
                </div>
            </v-col>
            <v-col cols="6">
                <div class="text-caption">
                    · 43분전
                </div>
            </v-col>
            <v-col cols="2">
                <v-menu bottom left>
                    <template v-slot:activator="{ on, attrs }">
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
        <div class=" pb-5 text-body-2">
            오늘 관악산 다녀왔는데 정상에서먹은 내이름은 정상수~
        </div>
        <v-row class="">
            <v-col cols="4">
                <div class="font-weight-black text-body-2">
                    거친 삑삑도요
                </div>
            </v-col>
            <v-col cols="6">
                <div class="text-caption">
                    · 43분전
                </div>
            </v-col>
            <v-col cols="2">
                <v-menu bottom left>
                    <template v-slot:activator="{ on, attrs }">
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
        <div class=" pb-5 text-body-2">
            오늘 관악산 다녀왔는데 정상에서먹은 내이름은 정상수~
        </div>
    </v-container>
</template>

<script>
export default {
    name: "Detail",
    data: () => ({
        items: [
            { title: "Click Me" },
            { title: "Click Me" },
            { title: "Click Me" },
            { title: "Click Me 2" },
        ],
        //
    }),
};
</script>
