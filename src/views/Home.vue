<template>
<nav class="navbar">
  <div class="container">
    <div id="navMenu" class="navbar-menu">
      <div class="navbar-start">
        <a class="navbar-item">
          Home
        </a>
        <a class="navbar-item">
          Documentation
        </a>
      </div>

      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <a class="button is-dark">Github</a>
            <a class="button is-link">Download</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</nav>

<section class="hero is-link is-fullheight-with-navbar">
  <div class="hero-body bg-primary">
    <div class="container notification" style="height: 100vh; background: #605080">
      <div class="columns" >
        <div class="column is-7 is-fullwidth">
          <div>
            <h1>TESTE</h1>
          </div>
        </div>
        <div class="column is-4 is-fullwidth">
          <div>
            <h1>TESTE</h1>
          </div>
        </div>        
      </div>
    </div>
  </div>
</section>
</template>

<script>

//import DashboardChart from "@/components/DashboardChart.vue";

export default {
  components: {
  },
  data() {
    return { };
  },
};
</script>

<style scoped>
/* .default-background-color{
  color: #has-text-white;
} */

.bg-primary {
	background-image: url(https://plantvsundead.com/assets/img/background.png);
	background-repeat: no-repeat;
	background-size: cover;
	background-position: center;
}
</style>