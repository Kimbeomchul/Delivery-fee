<template>
    <v-app-bar
        v-if="$route.name === 'detail' || $route.name === 'map' || $route.name === 'write'"
        elevation="0"
        color="white"
        dense
        class="shrink"
    >
        <v-icon large @click="$router.go(-1)">mdi-chevron-left</v-icon>
        <v-spacer></v-spacer>
        <v-toolbar-title>배공파용</v-toolbar-title>

        <v-spacer></v-spacer>
        <v-menu bottom left v-if="$route.name === 'detail'">
            <template #activator="{ on, attrs }">
                <v-btn icon v-bind="attrs" v-on="on">
                    <v-icon>mdi-dots-vertical</v-icon>
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
                    <v-card-title class="text-body2"> 파티를 삭제하시겠습니까? </v-card-title>
                    <v-divider></v-divider>

                    <v-card-actions>
                        <v-btn class="text-h5" color="#52D4DC" text @click="deleteDialog = false"> 아니요 </v-btn>
                        <v-spacer></v-spacer>
                        <v-btn
                            class="text-h5 font-weight-bold"
                            color="#52D4DC"
                            text
                            @click="deleteParty($route.params.partyId)"
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
                        <v-btn class="text-h5" color="green darken-1" text @click="editDialog = false"> 아니요 </v-btn>
                        <v-spacer></v-spacer>
                        <v-btn class="text-h5 font-weight-bold" color="green darken-1" text @click="goWrite()">
                            수정하기
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
            <v-dialog v-model="enterDialog" max-width="300">
                <v-card>
                    <v-card-title class="text-body2"> "근처 파티구해요"에 참가하시겠습니까? </v-card-title>
                    <v-card-text class="text-caption"> 참가를 진행할 경우 나가기 전까지 유지됩니다. </v-card-text>
                    <v-divider></v-divider>

                    <v-card-actions>
                        <v-btn class="text-h5" color="#52D4DC" text @click="enterDialog = false"> 아니요 </v-btn>
                        <v-spacer></v-spacer>
                        <v-btn
                            class="text-h5 font-weight-bold"
                            color="#52D4DC"
                            text
                            @click="enterParty($route.params.partyId)"
                        >
                            참가하기
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
            <v-dialog v-model="exitDialog" max-width="300">
                <v-card>
                    <v-card-title class="text-body2"> "근처 파티구해요"에서 나가시겠습니까? </v-card-title>
                    <v-card-text class="text-caption"> 나갈경우 새로운 파티에 참가할 수 있습니다. </v-card-text>
                    <v-divider></v-divider>

                    <v-card-actions>
                        <v-btn class="text-h5" color="#52D4DC" text @click="exitDialog = false"> 아니요 </v-btn>
                        <v-spacer></v-spacer>
                        <v-btn
                            class="text-h5 font-weight-bold"
                            color="#52D4DC"
                            text
                            @click="exitParty($route.params.partyId)"
                        >
                            나가기
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </v-menu>
    </v-app-bar>
</template>

<script>
import request from "@/request";

export default {
    name: "appbar-component",
    data: () => ({
        loading: false,
        deleteDialog: false,
        editDialog: false,
        enterDialog: false,
        exitDialog: false,
        items: [{ title: "삭제" }, { title: "수정" }, { title: "나가기" }, { title: "참가하기" }],
    }),
    computed: {
        userInfo() {
            return this.$store.state.userInfo;
        },
    },
    methods: {
        deleteParty: async function (partyId) {
            try {
                const result = await request(`/parties/${partyId}/`, "DELETE");
                if (result.status === 204) {
                    this.deleteDialog = false;
                    this.$router.go(-1);
                } else {
                    this.deleteDialog = false;
                }
            } catch (error) {
                console.log(error);
            }
        },
        enterParty: async function (partyId) {
            const data = {
                party: partyId,
                user: this.userInfo.user_id,
            };
            try {
                const result = await request("/participants/", "POST", data);
                if (result.status === 201) {
                    const { id, party } = result.data;
                    this.$store.dispatch("pushParticipationStatus", { id: id, party: party });
                    this.enterDialog = false;
                } else {
                    console.log(result);
                    this.enterDialog = false;
                }
            } catch (error) {
                console.log(error);
            }
            this.enterDialog = false;
        },
        // exitParty: async function (partyId) {
        //     try {
        //         const result = await request("/participants/", "POST", data);
        //         if (result.status === 201) {
        //             this.$store.dispatch("pushParticipationStatus" );
        //             this.enterDialog = false;
        //         } else {
        //             console.log(result);
        //             this.enterDialog = false;
        //         }
        //     } catch (error) {
        //         console.log(error);
        //     }
        //     this.enterDialog = false;
        // },
        goWrite() {
            this.$router.push({ name: "write", query: { edit: true } });
            this.editDialog = false;
        },
        handleItemAction(title) {
            switch (title) {
                case "수정":
                    this.editDialog = true;
                    break;
                case "삭제":
                    this.deleteDialog = true;
                    break;
                case "나가기":
                    this.exitDialog = true;
                    break;
                case "참가하기":
                    this.enterDialog = true;
                    break;
            }
        },
    },
};
</script>
