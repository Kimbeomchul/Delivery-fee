<template>
    <v-container class="spacing-playground pa-4">
        <write-component></write-component>
    </v-container>
</template>

<script>
import WriteComponent from "@/components/Write.vue";

export default {
    components: { WriteComponent },
    data: () => ({
        //
    }),
};
</script>
