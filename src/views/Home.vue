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
        <div class="column is-7 " style="background: #7F719A">
          <div class="is-size-2 has-text-centered has-text-weight-bold">
            Plantas
          </div>
        </div>
        <div class="column is-5 ml-2" style="background: #7F719A">
          <div class="container">
            <div class="is-size-2 has-text-centered has-text-weight-bold mb-5">
              Ganhos por período
            </div>
            <div class="is-flex is-align-items-center">
              <div class="is-size-4 mr-2">
                07D
              </div>
              <div class="card">
                <div class="card-content">
                  <div class="content">
                    Lorem ipsum leo risus, porta ac consectetur ac, vestibulum at eros. Donec id elit non mi porta gravida at eget metus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras mattis consectetur purus sit amet fermentum.
                  </div>
                </div>
              </div>
            </div>

            <div class="is-flex is-align-items-center mt-3">
              <div class="is-size-4 mr-2">
                14D
              </div>
              <div class="card">
                <div class="card-content">
                  <div class="content">
                    Lorem ipsum leo risus, porta ac consectetur ac, vestibulum at eros. Donec id elit non mi porta gravida at eget metus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras mattis consectetur purus sit amet fermentum.
                  </div>
                </div>
              </div>
            </div>

            <div class="is-flex is-align-items-center mt-3">
              <div class="is-size-4 mr-2">
                30D
              </div>
              <div class="card">
                <div class="card-content">
                  <div class="content">
                    Lorem ipsum leo risus, porta ac consectetur ac, vestibulum at eros. Donec id elit non mi porta gravida at eget metus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras mattis consectetur purus sit amet fermentum.
                  </div>
                </div>
              </div>
            </div>   
                            
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