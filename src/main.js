import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

import axios from "axios";
import VueAxios from "vue-axios";

import { library } from "@fortawesome/fontawesome-svg-core";
import { faCoins, faHeadset, faHome } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

library.add([faCoins, faHeadset, faHome]);

require("@/assets/main.scss");

createApp(App)
	.use(router)
	.use(VueAxios, axios)
	.component("fa-icon", FontAwesomeIcon)
	.mount("#app");
