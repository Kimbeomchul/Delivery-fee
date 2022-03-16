<template>
    <v-container class="spacing-playground pa-4">
        <detail-component></detail-component>
    </v-container>
</template>

<script>
import DetailComponent from "@/components/Detail.vue";

export default {
    name: "Detail",
    components: { DetailComponent },
    data: () => ({
        //
    }),
};
</script>
