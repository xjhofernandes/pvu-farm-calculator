<template>
  <section class="hero is-primary is-fullheight">
    <HeroNavbar :routes="HeroNavbarRoutes" />

    <!-- Hero head: will stick at the top -->
    <div class="hero-head"></div>

    <!-- Hero content: will be in the middle -->
    <div class="hero-body">
      <div class="container has-text-centered">
        <h2 class="subtitle"><fa-icon icon="coins"/></h2>
        <h1 @click="fetchBitcoin" class="title">Bitcoin</h1>
        <div v-for="(data, code) in bitcoin" :key="code">
          {{ code }} {{ decoder(data.symbol) }} {{ data.rate }}
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import HeroNavbar from "../components/HeroNavbar.vue";

export default {
  components: {
    HeroNavbar,
  },
  data() {
    return {
      bitcoin: "loading...",
      HeroNavbarRoutes: [
        { "menu-name": "Home", "route-url": "/" },
        { "menu-name": "Contact", "route-url": "/contact" },
        { "menu-name": "Bitcoin", "route-url": "/bitcoin" },
      ],
    };
  },
  methods: {
    fetchBitcoin: function () {
      this.axios
        .get("https://api.coindesk.com/v1/bpi/currentprice.json")
        .then((response) => {
          this.bitcoin = response.data.bpi;
          console.log(this.bitcoin)
        });
    },
    decoder(str) {
      const textArea = document.createElement("textarea");
      textArea.innerHTML = str;
      return textArea.value;
    },
  },
  mounted: function () {
    this.fetchBitcoin(); // Calls the method before page loads
  },
};
</script>