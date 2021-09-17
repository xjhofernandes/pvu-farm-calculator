<template>
  <div class="container p-5">
    <section>
      <div class="is-flex level">

        <div class="is-flex">
          <p class="is-size-4 has-text-white">Dashboard:</p>
          <p class="ml-4 is-size-4 has-text-grey-light">Character Tracking</p>
        </div>

        <div>
          <BruxoIcon class="icon" style="height: 6rem; width: 6rem" />
        </div>

        <div class="field is-horizontal">
          <div class="field-label">
            <label class="is-size-4 has-text-grey-light">Gold</label>
          </div>

          <div class="field-body">
            <div class="field">
              <div class="control has-icons-right is-inline">
                <input class="input" type="text" value="1.579.574" readonly />
                <MoedaIcon
                  class="icon is-small is-size-7 is-right mr-2"
                  style="opacity: 0.2"
                />
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="columns">
        <div class="column is-12 table-container">
          <table class="table is-fullwidth">
            <tr style="background-color: #85c1e9">
              <th
                class="has-text-white"
                v-for="colunas in Object.keys(heroAttributes[0])"
                :key="colunas"
              >
                {{ colunas }}
              </th>
            </tr>
            <tr v-for="colunas in heroAttributes" :key="colunas">
              <td v-for="coluna in colunas" :key="coluna">{{ coluna }}</td>
            </tr>
          </table>
        </div>
      </div>
    </section>

    <section>
      <div class="level mt-5">
        <div class="is-flex level-item">
          <p class="is-size-4 has-text-white">Class Skill:</p>
          <p class="is-size-4 has-text-grey-light pl-2">Avg Damage</p>
        </div>

          <div class="dropdown level-right" :class="drop_activate1 == true ? 'is-active' : ''" @click="drop_activate1 = !drop_activate1">
            <div class="dropdown-trigger">
              <button class="button" aria-haspopup="true" aria-controls="dropdown-menu3">
                <span>Skill List</span>
                <span class="icon is-small">
                  <ArrowIcon aria-hidden="true"/>
                </span>
              </button>
            </div>
            <div class="dropdown-menu" id="dropdown-menu3" role="menu">
              <div class="dropdown-content">
                <a href="#" class="dropdown-item">
                  Cold Bolt
                </a>
                <a href="#" class="dropdown-item">
                  Fire Ball
                </a>
                <a href="#" class="dropdown-item">
                  Fire Bolt
                </a>
                <a href="#" class="dropdown-item">
                  Fire Wall
                </a>
                <a href="#" class="dropdown-item">
                  Frost Driver
                </a>
                <a href="#" class="dropdown-item">
                  Lightning Bolt
                </a>
                <a href="#" class="dropdown-item">
                  Thunderstorm
                </a>
              </div>
            </div>
          </div>
      </div>   

      <div class="columns">
        <div class="column is-6">
          <DashboardChart
            :chart_height="550"
            :chart="trace2"
            :layout_extra_opts="layoutTrace2"
          />
        </div>
        <div class="column is-6">
          <DashboardChart
            :chart_height="550"
            :chart="trace1"
            :layout_extra_opts="layoutTrace1"
          />
        </div>        
      </div>

    </section>

    <section>
      <div class="level mt-5">
        <div class="is-flex level-item">
          <p class="is-size-4 has-text-white">Damage:</p>
          <p class="is-size-4 has-text-grey-light pl-2">by Class</p>
        </div>

          <div class="dropdown level-right" :class="drop_activate2 == true ? 'is-active' : ''" @click="drop_activate2 = !drop_activate2">
            <div class="dropdown-trigger">
              <button class="button" aria-haspopup="true" aria-controls="dropdown-menu3">
                <span>Classes List</span>
                <span class="icon is-small">
                  <ArrowIcon aria-hidden="true"/>
                </span>
              </button>
            </div>
            <div class="dropdown-menu" id="dropdown-menu3" role="menu">
              <div class="dropdown-content">
                <a href="#" class="dropdown-item">
                  Swordman
                </a>
                <a href="#" class="dropdown-item">
                  Thief
                </a>
                <a href="#" class="dropdown-item">
                  Archer
                </a>
                <a href="#" class="dropdown-item">
                  Mage
                </a>
                <a href="#" class="dropdown-item">
                  Merchant
                </a>
                <a href="#" class="dropdown-item">
                  Acolyte
                </a>
                <hr class="dropdown-divider">
                <a href="#" class="dropdown-item">
                  Knight
                </a>
                <a href="#" class="dropdown-item">
                  Crusade
                </a>
                <a href="#" class="dropdown-item">
                  Assassin
                </a>
                <a href="#" class="dropdown-item">
                  Rogue
                </a>
                <a href="#" class="dropdown-item">
                  Hunter
                </a>                                       
              </div>
            </div>
          </div>
      </div>   

      <div class="columns">
        <div class="column is-12">
          <DashboardChart
            :chart_height="550"
            :chart="trace3"
            :xaxis_dtick="10800000"
          />          
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import BruxoIcon from "@/assets/icons/bruxo.svg";
import MoedaIcon from "@/assets/icons/coin.svg";
import ArrowIcon from "@/assets/icons/arrow.svg";
import DashboardChart from "@/components/DashboardChart.vue";

export default {
  components: {
    BruxoIcon,
    MoedaIcon,
    DashboardChart,
    ArrowIcon
  },
  data() {
    return {
      drop_activate1: false,
      drop_activate2: false,
      heroAttributes: [
        {
          Name: "Anferus",
          Class: "Mage",
          Level: 42,
          Job: 34,
          Power: 17,
          "Magic Power": 70,
          Defense: 25,
        },
      ],
      layoutTrace1: {
        title: 'Fire Bolt Damage Per Level',
        margin: {
          t: 50,
        },       
      },
      layoutTrace2: {
        yaxis:{
          title: 'Mage vs Wizard Damage',
          titlefont: {
            size: 16,
            color: 'rgb(107, 107, 107)'
          },
          tickfont: {
            size: 14,
            color: 'rgb(107, 107, 107)'
          }
        },
        bargap: 0.15,
        bargroupgap: 0.1,
        barmode: 'group',
        margin: {
          l: 50,
        },        
      },      
      trace1: {
        uuid: "grafico-teste",
        traces: [
          {
            type: "bar",
            name: "grade",
            x: [1, 2, 3, 4],
            y: [5, 10, 2, 8],
            marker: {
              color: "#85c1e9",
            },
          },
        ],
      },
      trace2: {
        uuid: "grafico-teste",
        traces: [
          {
            type: "bar",
            name: 'Mage',
            x: ['Fire Bolt lv. 5', 'Napalm Beat lv. 10', 'Thunderstorm lv. 10'],
            y: [67, 42, 70],
            marker: {
              color: "#1a5276",
            },
          },
          {
            type: "bar",
            name: 'Wizard',
            x: ['Fire Bolt lv. 5', 'Napalm Beat lv. 10', 'Thunderstorm lv. 10'],
            y: [81, 53, 94],
            marker: {
              color: "#85c1e9",
            },
          },          
        ],
      }, 
      trace3: {
        uuid: "bla",
        traces: [{
          type: 'bar',
          x: [20, 14, 23, 32, 45, 66, 78, 95, 51, 19, 14, 22, 14, 16, 19, 15, 14, 10, 12, 12, 16],
          y: ['Novice', 'Swordman', 'Thief', "Archer", "Mage", "Merchant", "Acolyte", "Knight", "Crusader", 'Assassin', 'Rogue', 'Hunter', 'Bard', 'Dancer', 'Wizard', 'Sage', 'Blacksmith', 'Alchemist', 'Priest', 'Monk', 'Lord Knight'],
          orientation: 'h'}
        ]
      }       
    };
  },
};
</script>

<style scoped>
/* .default-background-color{
  color: #has-text-white;
} */
</style>