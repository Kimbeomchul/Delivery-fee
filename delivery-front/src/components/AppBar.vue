<template>
    <v-app-bar
        v-if="$route.name !== 'list' && $route.name !== 'home'"
        elevation="0"
        color="white"
        dense
        class="shrink"
    >
        <v-icon large @click="$router.go(-1)">mdi-chevron-left</v-icon>
        <v-spacer></v-spacer>
        <v-toolbar-title>배공파용</v-toolbar-title>

        <v-spacer></v-spacer>
        <v-menu bottom left>
            <template v-slot:activator="{ on, attrs }">
                <v-btn icon v-bind="attrs" v-on="on">
                    <v-icon>mdi-dots-vertical</v-icon>
                </v-btn>
            </template>

            <v-list>
                <v-list-item v-for="(item, i) in items" :key="i">
                    <v-list-item-title
                        v-text="item.title"
                        @click.stop="handleItemAction(item.title)"
                    >
                    </v-list-item-title>
                </v-list-item>
            </v-list>
            <v-dialog v-model="deleteDialog" max-width="300">
                <v-card>
                    <v-card-title class="text-body2">
                        {{ this.$route.params.partyId }}
                        "근처 파티구해요"에 dddd참가하시겠습니까?
                    </v-card-title>
                    <v-card-text class="text-caption">
                        참가를 진행할 경우 나가기 전까지 유지됩니다.
                    </v-card-text>
                    <v-divider></v-divider>

                    <v-card-actions>
                        <v-btn class="text-h5" color="green darken-1" text @click="dialog = false">
                            아니요
                        </v-btn>
                        <v-spacer></v-spacer>
                        <v-btn
                            class="text-h5 font-weight-bold"
                            color="green darken-1"
                            text
                            @click="dialog = false"
                        >
                            참가하기
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
            <v-dialog v-model="dialog" max-width="300">
                <v-card>
                    <v-card-title class="text-body2">
                        "근처 파티구해요"에 참가하시겠습니까?
                    </v-card-title>
                    <v-card-text class="text-caption">
                        참가를 진행할 경우 나가기 전까지 유지됩니다.
                    </v-card-text>
                    <v-divider></v-divider>

                    <v-card-actions>
                        <v-btn class="text-h5" color="green darken-1" text @click="dialog = false">
                            아니요
                        </v-btn>
                        <v-spacer></v-spacer>
                        <v-btn
                            class="text-h5 font-weight-bold"
                            color="green darken-1"
                            text
                            @click="dialog = false"
                        >
                            참가하기
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </v-menu>
    </v-app-bar>
</template>

<script>
export default {
    name: "appbar-component",
    data: () => ({
        loading: false,
        deleteDialog: false,
        dialog: false,
        items: [{ title: "삭제" }, { title: "수정" }, { title: "나가기" }, { title: "참가하기" }],
    }),
    methods: {
        deleteParty() {
            console.log(this.detailComponent);
            this.deleteDialog = true;
        },
        handleItemAction(title) {
            switch (title) {
                case "수정":
                    break;
                case "삭제":
                    this.deleteParty();
                    break;
                case "나가기":
                    break;
                case "참여하기":
                    break;
            }
        },
    },
};
</script>
