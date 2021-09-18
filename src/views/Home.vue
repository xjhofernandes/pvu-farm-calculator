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
    <div class="container notification" style="background: #605080">
      <div class="columns">

        <div class="column is-8">
           <div class="is-size-2 has-text-centered has-text-weight-bold mb-5">
              Minha plantação
            </div>          
            <div class="container is-fluid has-text-centered"  style="background: #7F719A"> 
              <div class="columns is-multiline">
                <div class="column is-one-third has-background-white mr-2 mt-2 mb-2">
                  <div class="field has-text-black">
                    <label class="label">Tipo</label>
                    <div class="control">
                      <label class="radio">
                        <input type="radio" name="answer">
                        Planta
                      </label>
                      <label class="radio">
                        <input type="radio" name="answer">
                        Mama
                      </label>
                    </div>
                  </div>

                <div class="is-flex">
                  <div class="field">
                    <label class="label">Custo total</label>
                    <div class="control">
                      <input class="input" type="number" placeholder="150">
                    </div>
                  </div>                    

                  <div class="field ml-2">
                    <label class="label">Produção</label>
                    <div class="control">
                      <input class="input" type="number" placeholder="250">
                    </div>
                  </div>
                </div>

                  <div class="field">
                    <label class="label">Horas de produção</label>
                    <div class="control">
                      <input class="input" type="number" placeholder="72">
                    </div>
                  </div>

                  <div class="field">
                    <label class="label ">Dia de plantação
                    <p class="has-text-black is-size-7"> <b> *Não é necessário preencher.</b> </p>
                    </label>
                    <div class="control">
                      <input class="input" type="date">
                    </div>
                  </div>                    

                  <div class="mt-5 has-text-centered">
                    <button class="button is-success">Adicionar</button>
                  </div>
                </div>
                                <div class="column is-one-third has-background-white mr-2 mt-2 mb-2">
                  <div class="field has-text-black">
                    <label class="label">Tipo</label>
                    <div class="control">
                      <label class="radio">
                        <input type="radio" name="answer">
                        Planta
                      </label>
                      <label class="radio">
                        <input type="radio" name="answer">
                        Mama
                      </label>
                    </div>
                  </div>

                <div class="is-flex">
                  <div class="field">
                    <label class="label">Custo total</label>
                    <div class="control">
                      <input class="input" type="number" placeholder="150">
                    </div>
                  </div>                    

                  <div class="field ml-2">
                    <label class="label">Produção</label>
                    <div class="control">
                      <input class="input" type="number" placeholder="250">
                    </div>
                  </div>
                </div>

                  <div class="field">
                    <label class="label">Horas de produção</label>
                    <div class="control">
                      <input class="input" type="number" placeholder="72">
                    </div>
                  </div>

                  <div class="field">
                    <label class="label ">Dia de plantação
                    <p class="has-text-black is-size-7"> <b> *Não é necessário preencher.</b> </p>
                    </label>
                    <div class="control">
                      <input class="input" type="date">
                    </div>
                  </div>                    

                  <div class="mt-5 has-text-centered">
                    <button class="button is-success">Adicionar</button>
                  </div>
                </div>
                                <div class="column is-one-third has-background-white mr-2 mt-2 mb-2">
                  <div class="field has-text-black">
                    <label class="label">Tipo</label>
                    <div class="control">
                      <label class="radio">
                        <input type="radio" name="answer">
                        Planta
                      </label>
                      <label class="radio">
                        <input type="radio" name="answer">
                        Mama
                      </label>
                    </div>
                  </div>

                <div class="is-flex">
                  <div class="field">
                    <label class="label">Custo total</label>
                    <div class="control">
                      <input class="input" type="number" placeholder="150">
                    </div>
                  </div>                    

                  <div class="field ml-2">
                    <label class="label">Produção</label>
                    <div class="control">
                      <input class="input" type="number" placeholder="250">
                    </div>
                  </div>
                </div>

                  <div class="field">
                    <label class="label">Horas de produção</label>
                    <div class="control">
                      <input class="input" type="number" placeholder="72">
                    </div>
                  </div>

                  <div class="field">
                    <label class="label ">Dia de plantação
                    <p class="has-text-black is-size-7"> <b> *Não é necessário preencher.</b> </p>
                    </label>
                    <div class="control">
                      <input class="input" type="date">
                    </div>
                  </div>                    

                  <div class="mt-5 has-text-centered">
                    <button class="button is-success">Adicionar</button>
                  </div>
                </div>
              </div>
            </div>              
        </div>

        <div class="column is-4">
            <div class="is-size-2 has-text-centered has-text-weight-bold mb-3">
              Ganhos por período
            </div>
          <div class="container is-size-3 p-1" style="background: #7F719A;">
            <div class="is-flex is-align-items-center is-justify-content-space-between">
              <span class="tag is-primary is-large">Moeda</span>
                <div class="dropdown mt-2">
                  <div class="dropdown-trigger">
                      <button class="button" aria-haspopup="true" aria-controls="dropdown-menu">
                        <span>BRL (R$)</span>
                          <div class="dropdown-menu" id="dropdown-menu" role="menu">
                      <div class="dropdown-content">
                        <a href="#" class="dropdown-item">
                          Dollar ($)
                        </a>
                        <a class="dropdown-item">
                          Euro (€)
                        </a>
                        <a href="#" class="dropdown-item">
                          BNB
                        </a>
                        <a href="#" class="dropdown-item">
                          PVU
                        </a>              
                      </div>
                    </div>
                    <span class="icon is-small">
                      <i class="fas fa-angle-down" aria-hidden="true">^</i>
                    </span>
                  </button>
                </div>
              </div>         
            </div>             

            <div class="is-flex is-align-items-center is-justify-content-space-between">
              <span class="tag is-primary is-large">7 Dias</span>
              <div class="card">
                <div class="card-content">
                  <div class="content">
                      <div class="is-size-5" style="border-bottom: solid 1px #ddd;">
                        Lucros : 1600 <b>LE</b>
                      </div>
                      <div class="is-size-5" style="border-bottom: solid 1px #ddd;">
                        Gastos : 1600 <b>LE</b>
                      </div>
                      <div class="is-size-5" style="border-bottom: solid 1px #ddd;">
                        Produzido : 1600 <b>LE</b>
                      </div>
                      <div class="is-size-5">
                        Faturamento : 1900 <b>BRL (R$)</b>
                      </div>    
                  </div>
                </div>
              </div>
            </div>

            <div class="is-flex is-align-items-center mt-3 is-justify-content-space-between">
            <span class="tag is-primary is-large">14 Dias</span>
              <div class="card">
                <div class="card-content">
                  <div class="content">
                      <div class="is-size-5" style="border-bottom: solid 1px #ddd;">
                        Lucros : 1600 <b>LE</b>
                      </div>
                      <div class="is-size-5" style="border-bottom: solid 1px #ddd;">
                        Gastos : 1600 <b>LE</b>
                      </div>
                      <div class="is-size-5" style="border-bottom: solid 1px #ddd;">
                        Produzido : 1600 <b>LE</b>
                      </div>
                      <div class="is-size-5">
                        Faturamento : 1900 <b>BRL (R$)</b>
                      </div>                      
                  </div>
                </div>
              </div>
            </div>

            <div class="is-flex is-align-items-center mt-3 is-justify-content-space-between">
            <span class="tag is-primary is-large">30 Dias</span>
              <div class="card">
                <div class="card-content">
                  <div class="content">
                      <div class="is-size-5" style="border-bottom: solid 1px #ddd;">
                        Lucros : 1600 <b>LE</b>
                      </div>
                      <div class="is-size-5" style="border-bottom: solid 1px #ddd;">
                        Gastos : 1600 <b>LE</b>
                      </div>
                      <div class="is-size-5" style="border-bottom: solid 1px #ddd;">
                        Produzido : 1600 <b>LE</b>
                      </div>
                      <div class="is-size-5">
                        Faturamento : 1900 <b>BRL (R$)</b>
                      </div>                     
                  </div>
                </div>
              </div>
            </div>
          </div>
        <button class="button is-large is-fullwidth mt-3 is-primary">Atualizar Valores</button>
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