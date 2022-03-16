<template>
    <v-container class="spacing-playground pa-4">
        <profile-component></profile-component>
    </v-container>
</template>

<script>
import ProfileComponent from "@/components/Profile.vue";

export default {
    components: { ProfileComponent },
    data: () => ({
        //
    }),
};
</script>
