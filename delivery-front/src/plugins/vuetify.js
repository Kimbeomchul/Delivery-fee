import Vue from "vue";
import Vuetify, { VSnackbar, VBtn, VIcon } from "vuetify/lib";
import VuetifyToast from "vuetify-toast-snackbar-ng";

Vue.use(Vuetify, {
    components: {
        VSnackbar,
        VBtn,
        VIcon,
    },
});

Vue.use(VuetifyToast);

export default new Vuetify({});
