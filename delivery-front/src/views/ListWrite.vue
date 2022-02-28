<template>
    <v-container class="spacing-playground pa-6">
        <list-component></list-component>
        <v-btn fixed bottom right absoluteclass="mx-2" fab dark color="#52D4DC" router-link :to="{ name: 'write' }">
            <v-icon dark> mdi-plus </v-icon>
        </v-btn>
    </v-container>
</template>

<script>
import ListComponent from "@/components/List.vue";

export default {
    components: { ListComponent },
    data: () => ({
        //
    }),
};
</script>
