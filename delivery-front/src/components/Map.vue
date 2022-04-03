<template>
    <div>
        <v-btn
            outlined
            color="#52D4DC"
            elevation="1"
            large
            block
            class="xl rounded-lg"
            @click="handleAddressDialog('open')"
        >
            <v-icon small>mdi-crosshairs-gps</v-icon>
            <v-spacer></v-spacer>
            <div class="black--text font-weight-black" style="font-size: 1.2em">주소 검색</div>
            <v-spacer></v-spacer>
        </v-btn>
        <v-dialog v-model="searchAddressDialog" fullscreen hide-overlay transition="dialog-bottom-transition">
            <v-card>
                <v-toolbar elevation="0" dense>
                    <v-btn icon style="color: #52d4dc" @click="searchAddressDialog = false">
                        <v-icon color="black">mdi-close</v-icon>
                    </v-btn>
                    <v-spacer></v-spacer>
                    <v-toolbar-title class="font-weight-black" style="color: #52d4dc">주소 검색</v-toolbar-title>
                    <v-spacer class="mr-11"></v-spacer>
                </v-toolbar>
                <v-container class="spacing-playground pa-4">
                    <v-form ref="form" v-model="valid" lazy-validation>
                        <v-text-field
                            v-model="address"
                            maxlength="50"
                            label="도로명, 건물명, 지번으로 검색"
                            outlined
                            solo
                            prepend-inner-icon="mdi-magnify"
                            color="#52D4DC"
                            @keydown.enter.prevent="getSearchAddress($event)"
                            :rules="addressRules"
                        ></v-text-field>
                    </v-form>
                    <v-sheet class="pa-2" v-if="mapData">
                        <div v-for="(place, index) in places" :key="index">
                            <v-divider></v-divider>
                            <div @click="handleAddressDialog('close', place)" v-ripple="{ class: 'blue--text' }">
                                <p class="ma-0 pt-1 pb-1">{{ place.address_name }}</p>
                                <p class="ma-0 pt-1 pb-1 grey--text" :style="{ fontSize: '14px' }">
                                    [도로명] {{ place.road_address_name }} ({{ place.place_name }})
                                </p>
                            </div>
                        </div>
                    </v-sheet>
                    <v-sheet class="pa-2" v-else
                        ><div class="ml-3">
                            <div class="mb-1"><strong :style="{ fontSize: '18px' }">주소 검색 Tip</strong></div>
                            <ul class="pl-3">
                                <li>
                                    도로명 + 건물번호
                                    <v-list-item-subtitle class="grey--text">예) 테헤란로 320</v-list-item-subtitle>
                                </li>
                                <li>
                                    지역명 + 번지
                                    <v-list-item-subtitle class="grey--text">예) 논현동 5-34</v-list-item-subtitle>
                                </li>
                                <li>
                                    건물명 + 아파트명
                                    <v-list-item-subtitle class="grey--text">예) 여의도자이아파트</v-list-item-subtitle>
                                </li>
                            </ul>
                        </div>
                    </v-sheet>
                </v-container>
            </v-card>
        </v-dialog>
        <br />
        <v-card elevation="0">
            <div id="map" class="map"></div>
        </v-card>
        <div class="black--text font-weight-black pt-5 pl-3" style="font-size: 1.3em">{{ myAddress }}</div>
        <br />
        <!-- 
        <v-row>
            <v-col cols="11">
                <v-text-field class="pl-3" placeholder="건물명을 입력해주세요 (선택)"></v-text-field>
            </v-col>
        </v-row>
        -->
        <v-btn block x-large rounded color="#52D4DC" dark class="font-weight-bold" style="font-size: 1.02em">
            이 위치로 주소 설정
        </v-btn>
    </div>
</template>

<script>
import request from "@/request";

export default {
    name: "map-component",
    data: () => ({
        valid: true,
        address: "",
        searchAddressDialog: false,
        addressRules: [(value) => !!value || "검색어를 입력하세요."],
        mapData: null,
        myAddress: "",
        latitude: "",
        longitude: "",
    }),
    mounted: function () {
        window.kakao && window.kakao.maps ? this.initMap() : this.addScript();
    },
    computed: {
        places: function () {
            return this.mapData.documents.filter((document) => document.road_address_name !== "");
        },
    },
    methods: {
        initMap() {
            var container = document.getElementById("map");
            var options = null;

            if (!this.latitude && !this.longitude) {
                options = { center: new kakao.maps.LatLng(33.450701, 126.570667), level: 3 };
            } else {
                options = { center: new kakao.maps.LatLng(this.latitude, this.longitude), level: 3 };
            }

            var map = new kakao.maps.Map(container, options);

            //마커추가하려면 객체를 아래와 같이 하나 만든다.
            var marker = new kakao.maps.Marker({
                position: map.getCenter(),
            });
            marker.setMap(map);
        },
        addScript() {
            const script = document.createElement("script");
            const appkey = this.$store.state.kakaoAppkey;
            /* global kakao */
            script.onload = () => kakao.maps.load(this.initMap);
            script.src = `http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${appkey}`;
            document.head.appendChild(script);
        },
        handleAddressDialog(status, place) {
            if (status == "open") {
                this.searchAddressDialog = true;
                this.address = "";
                this.mapData = null;
            } else {
                this.searchAddressDialog = false;
                this.myAddress = place.address_name;
                this.latitude = place.x;
                this.longitude = place.y;
            }
        },
        getSearchAddress: async function (event) {
            //keydown 이벤트 사용시 이벤트의 중복호출 방지
            if (event.isComposing || event.keyCode === 229) {
                return;
            }

            const validate = this.$refs.form.validate();
            if (!validate) return;

            const apikey = this.$store.state.kakaoAPIkey;
            const data = this.address;

            let options = {
                method: "GET",
                headers: {
                    Authorization: `KakaoAK ${apikey}`,
                },
            };

            await fetch(
                "http://dapi.kakao.com//v2/local/search/keyword.json?query=" + encodeURIComponent(data),
                options
            )
                .then((response) => {
                    if (response.ok) {
                        console.log(response);
                        return response.json();
                    } else {
                        console.log(response);
                    }
                })
                .then((Json) => {
                    this.mapData = Json;
                    console.log(this.mapData);
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    },
};
</script>

<style>
.map {
    width: 100%;
    min-height: 570px;
    max-height: 570px;
}
</style>
