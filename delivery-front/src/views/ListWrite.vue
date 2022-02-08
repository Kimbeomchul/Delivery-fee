<template>
    <v-container class="spacing-playground pa-6">
        <list-component></list-component>
        <write-component></write-component>
    </v-container>
</template>

<script>
import ListComponent from "@/components/List.vue";
import WriteComponent from "@/components/Write.vue";

export default {
    components: { ListComponent, WriteComponent },
    data: () => ({
        //
    }),
};
</script>
