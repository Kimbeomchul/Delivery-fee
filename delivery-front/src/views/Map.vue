<template>

    <v-container fluid >
        
        <v-img max-height="570" max-width="390" src="../assets/maps.png" alt="map" />  
        
        <div class="black--text font-weight-black pt-5 pl-3" style="font-size:1.3em">
            경기 과천시 관문로 106
        </div>

        <v-row>
            <v-col cols="11">
                <v-text-field class="pl-3" placeholder="건물명을 입력해주세요 (선택)"></v-text-field>
            </v-col>
        </v-row>
        <v-btn block x-large rounded color="#52D4DC" dark class="font-weight-bold" style="font-size:1.02em">
            이 위치로 주소 설정
        </v-btn>

    </v-container>
</template>
