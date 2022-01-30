<template>
    <v-container class="spacing-playground pa-6 text-center">
        <v-card :loading="loading" class="mx-auto my-12" max-width="374" elevation="2" outlined>
            <template slot="progress">
                <v-progress-linear
                    color="deep-purple"
                    height="10"
                    indeterminate
                ></v-progress-linear>
            </template>

            <v-row dense>
                <v-col cols="8" xs="6"> <v-card-title>Tonight's availabilit</v-card-title></v-col>
                <v-col cols="4" xs="6">
                    <v-img
                        width="100"
                        height="100"
                        src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
                    ></v-img
                ></v-col>
                <v-col xs="2">
                    <v-card-title>주문 예정시간</v-card-title>
                </v-col>
                <v-col xs="4" offset-xs="4">
                    <v-card-title>10시 40분</v-card-title>
                </v-col>
            </v-row>

            <v-card-title>내용</v-card-title>
            <v-textarea
                value="배달비를 아껴봅시다 여러분 배달비를 아껴봅시다 여러분 배달비를 아껴봅시다 여러분 배달비를 아껴봅시다 여러분 배달비를 아껴봅시다 여러분 배달비를 아껴봅시다 여러분"
                auto-grow
                filled
                readonly
                rows="3"
            ></v-textarea>

            <v-card-title>댓글</v-card-title>
            <v-divider class="mx-4"></v-divider>

            <v-card-text>
                <v-row align="center" class="mx-0">
                    <v-rating
                        :value="4.5"
                        color="amber"
                        dense
                        half-increments
                        readonly
                        size="14"
                    ></v-rating>

                    <div class="grey--text ms-4">
                        4.5 (413)
                    </div>
                </v-row>

                <div class="my-4 text-subtitle-1">
                    $ • Italian, Cafe
                </div>

                <div>
                    Small plates, salads & sandwiches - an intimate setting with 12 indoor seats
                    plus patio seating.
                </div>
            </v-card-text>
        </v-card>
    </v-container>
</template>

<script>
export default {
    data: () => ({
        loading: false,
        selection: 1,
    }),

    methods: {
        reserve() {
            this.loading = true;

            setTimeout(() => (this.loading = false), 2000);
        },
    },
};
</script>
