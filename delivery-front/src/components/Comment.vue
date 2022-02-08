<template>
    <v-text-field hide-details dense v-model="message" outlined clearable label="댓글" type="text">
        <template v-slot:append>
            <v-fade-transition leave-absolute>
                <v-progress-circular
                    v-if="loading"
                    size="24"
                    color="info"
                    indeterminate
                ></v-progress-circular>
                <img
                    v-else
                    width="24"
                    height="24"
                    src="https://cdn.vuetifyjs.com/images/logos/v-alt.svg"
                    alt=""
                />
            </v-fade-transition>
        </template>
    </v-text-field>
</template>

<script>
export default {
    name: "comment-component",
};
</script>
