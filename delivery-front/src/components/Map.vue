<template>
    <div>
        <v-btn outlined color="#52D4DC" elevation="1" large block class="xl rounded-lg">
            <v-icon small>mdi-crosshairs-gps</v-icon>
            <v-spacer></v-spacer>
            <div class="black--text font-weight-black" style="font-size: 1.2em">주소 검색</div>
            <v-spacer></v-spacer>
        </v-btn>
        <br />
        <v-card elevation="0">
            <div id="map" class="map"></div>
        </v-card>

        <div class="black--text font-weight-black pt-5 pl-3" style="font-size: 1.3em">경기 과천시 관문로 106</div>
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
export default {
    name: "map-component",
    data: () => ({
        //
    }),
    mounted: function () {
        window.kakao && window.kakao.maps ? this.initMap() : this.addScript();
    },
    methods: {
        initMap() {
            var container = document.getElementById("map");
            var options = { center: new kakao.maps.LatLng(33.450701, 126.570667), level: 3 };
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
