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
            <div class="box is-fluid has-text-centered"  style="background: #7F719A"> 
              <div class="columns is-multiline">

                <div class="column is-4" v-for="(plantacao, index) in listagem_plantacoes" :key="index">
                  <div class="has-background-white p-5 notification is-fullheight">
                    <div class="has-text-black " >
                      <label class="label is-small">Tipo</label>
                      <div class="control">
                        <label class="radio">
                          <input type="radio" name="answer" disabled :checked="plantacao.tipo == 'plant'">
                          Plant
                        </label>
                        <label class="radio" >
                          <input type="radio" name="answer" disabled :checked="plantacao.tipo == 'mother'">
                          Mother Tree
                        </label>
                      </div>
                    </div>
                  <label class="checkbox is-size-6">
                    <b class="mr-1 is-size-7">NFT</b>
                    <input type="checkbox" :checked="plantacao.nft" disabled>
                  </label>

                  <div class="is-flex">
                    <div class="field">
                      <label class="label is-small">Custo total</label>
                      <span class="input is-info is-light is-small is-fullwidth">{{ plantacao.custo_total }}</span>
                    </div>           

                    <div class="field ml-6">
                      <label class="label is-small">Produção</label>
                      <span class="input is-info is-light is-small is-fullwidth">{{ plantacao.producao}}</span>
                    </div>
                  </div>

                    <div class="field">
                      <label class="label is-small">Horas de produção</label>
                        <span class="input is-info is-light is-small is-fullwidth">{{ plantacao.horas_producao}}</span>
                    </div>

                    <div class="field">
                      <label class="label is-small">Dia de plantação
                      <p class="has-text-black is-size-7"> <b> *Não é necessário preencher.</b> </p>
                      </label>
                        <span class="input is-info is-light is-small is-fullwidth">10/10/21</span>
                    </div>                    

                    <div class="mt-5 is-flex is-justify-content-space-between">
                      <button class="button is-link is-small" @click="duplicar_planta(index)">Duplicar</button>
                      <button class="button is-danger is-small" @click="remover_planta(index)">Remover</button>
                    </div>
                  </div>
                </div>

                <div class="column is-4">
                  <div class="has-background-white p-5 notification">
                    <div class="has-text-black">
                      <label class="label is-small">Tipo</label>
                      <div class="control">
                        <label class="radio">
                          <input type="radio" v-model="nova_plantacao.tipo" id="plant" value="plant">
                          Plant
                        </label>
                        <label class="radio">
                          <input type="radio" v-model="nova_plantacao.tipo" id="mother" value="mother">
                          Mother Tree
                        </label>
                      </div>
                    </div>

                  <label class="checkbox is-size-6">
                    <b class="mr-1 is-size-7">NFT</b>
                    <input type="checkbox" v-model="nova_plantacao.nft">
                  </label>

                  <div class="is-flex">
                    <div class="field">
                      <label class="label is-small">Custo total</label>

                      <div class="control">
                        <input class="input is-small" type="number" placeholder="150" v-model="nova_plantacao.custo_total" :disabled="nova_plantacao.nft">
                      </div>
                    </div>    

                    <div class="field ml-2">
                      <label class="label is-small">Produção</label>
                      <div class="control">
                        <input class="input is-small" type="number" placeholder="250" v-model="nova_plantacao.producao">
                      </div>
                    </div>
                  </div>

                    <div class="field">
                      <label class="label is-small">Horas de produção</label>
                      <div class="control">
                        <input class="input is-small" type="number" placeholder="72" v-model="nova_plantacao.horas_producao">
                      </div>
                    </div>

                    <div class="field">
                      <label class="label is-small">Dia de plantação
                      <p class="has-text-black is-size-7"> <b> *Não é necessário preencher.</b> </p>
                      </label>
                      <div class="control">
                        <input class="input is-small" type="date">
                      </div>
                    </div>                    

                    <div class="mt-5 has-text-centered">
                      <button class="button is-primary is-small" @click="adicionar_nova_planta(nova_plantacao)">Adicionar</button>
                    </div>
                  </div>
                </div>

              </div>
            </div>              
        </div>

        <div class="column is-4">
            <div class="is-size-2 has-text-centered has-text-weight-bold mb-5">
              Ganhos por período
            </div>
          <div class="container is-size-3 p-1 notification" style="background: #7F719A;">
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
                        Lucros : {{ ganhos_periodo[0]["lucro"] }} <b>LE</b>
                      </div>
                      <div class="is-size-5" style="border-bottom: solid 1px #ddd;">
                        Gastos : {{ ganhos_periodo[0]["custo"] }} <b>LE</b>
                      </div>
                      <div class="is-size-5" style="border-bottom: solid 1px #ddd;">
                        Produzido : {{ ganhos_periodo[0]["produzido"] }} <b>LE</b>
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
                        Lucros : {{ ganhos_periodo[1]["lucro"] }} <b>LE</b>
                      </div>
                      <div class="is-size-5" style="border-bottom: solid 1px #ddd;">
                        Gastos : {{ ganhos_periodo[1]["custo"] }} <b>LE</b>
                      </div>
                      <div class="is-size-5" style="border-bottom: solid 1px #ddd;">
                        Produzido : {{ ganhos_periodo[1]["produzido"] }} <b>LE</b>
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
                        Lucros : {{ ganhos_periodo[2]["lucro"] }} <b>LE</b>
                      </div>
                      <div class="is-size-5" style="border-bottom: solid 1px #ddd;">
                        Gastos : {{ ganhos_periodo[2]["custo"] }} <b>LE</b>
                      </div>
                      <div class="is-size-5" style="border-bottom: solid 1px #ddd;">
                        Produzido : {{ ganhos_periodo[2]["produzido"] }} <b>LE</b>
                      </div>
                      <div class="is-size-5">
                        Faturamento : 1900 <b>BRL (R$)</b>
                      </div>                     
                  </div>
                </div>
              </div>
            </div>
          </div>
        <button class="button is-large is-fullwidth mt-3 is-primary" @click="atualizar_valores()">Atualizar Valores</button>
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
    return { 
      ganhos_periodo :
        [
          {'periodo': '7d', 'produzido': 0, 'custo': 0, 'lucro': 0},
          {'periodo': '14d', 'produzido': 0, 'custo': 0, 'lucro': 0},
          {'periodo': '30d', 'produzido': 0, 'custo': 0, 'lucro': 0}
        ],
      nova_plantacao :
        {
          "tipo": "", 
          "producao": Number, 
          "horas_producao": Number,
          "custo_total": Number,
          "nft": false
        },
      listagem_plantacoes : [],
    };
  },
  methods: {
    adicionar_nova_planta(nova_plantacao) {
      console.log(nova_plantacao);
      if (nova_plantacao.nft == true){
        nova_plantacao.custo_total = 0;
      }

      this.listagem_plantacoes.push(nova_plantacao);
      this.nova_plantacao = {
          "tipo": "", 
          "producao": Number, 
          "horas_producao": Number,
          "custo_total": Number,
          "nft": false
        }
    },
    duplicar_planta(index) {
      this.listagem_plantacoes.push(this.listagem_plantacoes[index]);
    },
    remover_planta(index) {
      this.listagem_plantacoes.splice(index, 1);
    },
    async obter_lucros(listagem_plantacoes) {
      console.log("listagem:")
      console.log(listagem_plantacoes)
      
      const requestOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        },
        body: JSON.stringify(listagem_plantacoes),
      };
      
      let data = await fetch(
        "http://localhost:8000/api/obter-periodo-lucros",
        requestOptions
      )
        .then((response) => response.json())
        .then((data) => {
          return data;
        })
        .catch((error) => {
          console.error(error);
        });
        console.log(data);
      return data;
    },
    async atualizar_valores(){
      this.ganhos_periodo = await this.obter_lucros(this.listagem_plantacoes);
    }
  }
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