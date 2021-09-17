<template>
  <section class="hero is-primary is-fullheight">
    <HeroNavbar :routes="HeroNavbarRoutes" />

    <!-- Hero head: will stick at the top -->
    <div class="hero-head"></div>

    <!-- Hero content: will be in the middle -->
    <div class="hero-body">
      <div class="container has-text-centered">
        <h2 class="subtitle"><fa-icon icon="headset" /></h2>
        <h1 class="title">Contact</h1>
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
      HeroNavbarRoutes: [
        { "menu-name": "Home", "route-url": "/" },
        { "menu-name": "Contact", "route-url": "/contact" },
        { "menu-name": "Bitcoin", "route-url": "/bitcoin" },
      ],
    };
  },
};
</script>