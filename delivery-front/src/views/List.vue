<template>
    <v-container class="spacing-playground pa-6">
        <v-text-field
            value="경기도 과천시 16"
            solo
            readonly
            append-outer-icon="mdi-map-marker"
        ></v-text-field>
        <br />
        참여중
        <v-divider></v-divider>
        <br />
        <v-card elevation="2" outlined>
            <v-row>
                <v-col cols="4" sm="6">
                    <v-img
                        width="100"
                        height="100"
                        src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
                    ></v-img
                ></v-col>
                <v-col cols="8" sm="6"> <v-card-title>Tonight's availabilit</v-card-title></v-col>
            </v-row>
        </v-card>
        <br />

        대기중
        <v-divider></v-divider>
        <br />
        <v-card elevation="2" outlined>
            <v-row>
                <v-col cols="4" sm="6">
                    <v-img
                        width="100"
                        height="100"
                        src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
                    ></v-img
                ></v-col>
                <v-col cols="8" sm="6"> <v-card-title>Tonight's availabilit</v-card-title></v-col>
            </v-row>
        </v-card>
        <br />
        <v-card elevation="2" outlined>
            <v-row>
                <v-col cols="4" sm="6">
                    <v-img
                        width="100"
                        height="100"
                        src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
                    ></v-img
                ></v-col>
                <v-col cols="8" sm="6"> <v-card-title>Tonight's availabilit</v-card-title></v-col>
            </v-row>
        </v-card>
        <br />
    </v-container>
</template>
