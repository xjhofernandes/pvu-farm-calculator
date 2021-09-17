<template>
  <header class="navbar">
    <div class="container">
      <div class="navbar-brand">
        <a class="navbar-item">
          <img src="../assets/logo.png" alt="Logo" />
        </a>
      </div>
      <div id="navbarMenuHeroC" class="navbar-menu">
        <div class="navbar-end">
          <router-link v-for="route in routes" :key="route" :to="route['route-url']">
            <a class="navbar-item"> {{ route['menu-name'] }} </a>
          </router-link>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  props: {
    routes: Array,
  },
};
</script>