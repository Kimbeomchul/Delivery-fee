<template>
    <v-container class="spacing-playground pa-6">
        
        <div class="pl-5">
        <v-row>
            <v-col class="text-left"> 
                <div class="font-weight-black pt-4" style="font-size:1.2em">
                    근처파티구해요
                </div>

                <div class="grey--text font-weight-bold pr-4" style="font-size:0.8em; text-align:right">
                    #치킨 #피자 #짜장면
                </div>

                
                <div class="grey--text font-weight-bold pr-4 pt-3" style="font-size:0.8em; text-align:right">
                    제주도 제주시 해안동
                </div>

                <div class="grey--text font-weight-medium pr-4" style="font-size:0.8em; text-align:right">
                    108m
                </div>

            </v-col>
            <v-col class="pt-4 pl-8">
                <v-img
                    class="rounded-card"
                    width="100"
                    height="100"
                    src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
                ></v-img>
            <div class="pl-4 pt-1 font-weight-black">
                10시 35분
            </div>
            </v-col>

        </v-row>
        </div>
    
        <div class="pl-4  pt-1 font-weight-black">
            내용
        </div>
       <v-text-field  class="pl-3 text-center" placeholder="치킨을 시키려구 합니다. 맛나느치킨" value="치킨을 시키려구 합니다. 맛나느치킨"></v-text-field>
        
    
        <v-btn block x-large rounded color="#52D4DC" dark class="font-weight-bold" style="font-size:1.02em">
            참여하기
        </v-btn>
    </v-container>
</template>