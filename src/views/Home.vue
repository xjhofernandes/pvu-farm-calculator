<template>
	<nav class="navbar">
		<div class="container">
			<div id="navMenu" class="navbar-menu is-active has-text-centered">
				<div class="mt-3 has-text-white">
					<p class="is-size-5">
						{{ linguagem_atual.nav_bar
						}}<b class="tag is-dark is-medium"
							>0xedF4C967E8f02fB39B0b36b3df10fbc406c99Bb9</b
						>
					</p>
				</div>

				<div class="navbar-end">
					<div class="navbar-item">
						<div class="buttons">
							<a
								class="button is-dark"
								target="”_blank”"
								href="https://github.com/xjhofernandes/pvu-farm-calculator"
								>Github</a
							>
						</div>
					</div>
				</div>
			</div>
		</div>
	</nav>

	<section class="hero is-link is-fullheight-with-navbar bg-primary">

		<div class="hero-body p-1">
			<div class="container">
				<div class="is-flex is-justify-content-flex-end">
					<BrazilIcon class="icon is-large pr-1 is-clickable" :class="linguagem == 'portuguese' ? '' : 'icone-transparent'" @click="alterar_linguagem('portuguese')"/>
					<EuaIcon class="icon is-large pr-1 is-clickable" :class="linguagem == 'english' ? '' : 'icone-transparent'" @click="alterar_linguagem('english')"/>
					<SpainIcon class="icon is-large is-clickable" :class="linguagem == 'spanish' ? '' : 'icone-transparent'" @click="alterar_linguagem('spanish')"/>
				</div>
			</div>
		</div>
		
		<div class="my-4">
			<div class="container notification" style="background: #605080">
				<div class="is-size-7 is-flex is-justify-content-space-between">
					<div>
						{{ linguagem_atual.pvuhub_credits }}
						<a
							class="has-text-weight-bold"
							href="https://pvuhub.info/#/"
							target="”_blank”"
							style="text-decoration: none;"
							>PVUHUB.info</a
						>
					</div>

					<div class="has-text-white has-text-weight-bold">
						<div class="tag is-black">PVU : {{ valores_pvu.dolar }} USD</div>
						<div class="is-size-7 tag is-light has-text-black">
							Volume: {{ valores_pvu.volume }} USD
						</div>
					</div>
				</div>

				<div class="columns">
					<div class="column is-8">
						<div class="mb-5 is-size-2 has-text-centered has-text-weight-bold">
							{{ linguagem_atual.my_plantation_text }}
						</div>
						<div
							class="box is-fluid has-text-centered"
							style="background: #7F719A"
						>
							<div class="mb-3 is-flex is-justify-content-center">
								<button
									class="mr-2 button is-primary is-light"
									@click="adicionar_nova_mama()"
								>
									{{ linguagem_atual.add_mama_button_text }}
								</button>
								<button
									class="button is-success"
									@click="adicionar_nova_sapling()"
								>
									{{ linguagem_atual.add_saplings_button_text }}
								</button>

							</div>
								<button
									class="button is-danger is-small is-flex mb-1 has-text-weight-bold"
									@click="remover_todas_plantas()"
								>
									{{ linguagem_atual.clean_text}}
								</button>
							<div class="columns is-multiline">
								<div
									class="column is-4"
									v-for="(plantacao, index) in listagem_plantacoes"
									:key="index"
								>
									<div
										class="p-5 has-background-white notification is-fullheight"
									>
										<figure class="image is-1by1">
											<!-- <img :src="require(`../assets/img/plantas/${plantacao.imagem}.png`)"> -->
											<img
												:src="
													require(`../assets/img/plantas/${plantacao.imagem}.png`)
												"
											/>
										</figure>


											<div class="has-text-black mb-2" v-if="!plantacao.nft">
												<label class="label is-small">{{
													linguagem_atual.type_text
												}}</label>
												<div class="control">
													<label class="radio" v-if="plantacao.tipo == 'plant'">
														<!-- <input type="radio" name="answer" checked> -->
														<span class="tag is-success">Plant</span>
													</label>
													<label class="radio" v-if="plantacao.tipo == 'mother'">
														<span class="tag is-success is-light"
															>Mother Tree</span
														>
													</label>
												</div>
											</div>

										<div class="is-flex is-justify-content-space-between mb-2" v-if="plantacao.nft">
											<div class="has-text-black ">
												<label class="label is-small">{{
													linguagem_atual.type_text
												}}</label>
												<div class="control">
													<label class="radio" v-if="plantacao.tipo == 'plant'">
														<!-- <input type="radio" name="answer" checked> -->
														<span class="tag is-success">Plant</span>
													</label>
													<label class="radio" v-if="plantacao.tipo == 'mother'">
														<span class="tag is-success is-light"
															>Mother Tree</span
														>
													</label>
												</div>
											</div>
											
											<div class="has-text-black" v-if="plantacao.nft">
												<label class="label is-small">
													element
												</label>
												<div class="control">
													<label class="radio" v-if="plantacao.elemento == 'Fire'">
														<!-- <input type="radio" name="answer" checked> -->
														<span class="tag is-success" style="background-color: #7E2121;">Fire</span>
													</label>
													<label class="radio" v-if="plantacao.elemento == 'Ice'">
														<span class="tag is-success"
														style="background-color: #00647A;">Ice</span
														>
													</label>
													<label class="radio" v-if="plantacao.elemento == 'Electro'">
														<span class="tag is-success"
														style="background-color: #BA7A14;">Electro</span
														>
													</label>
													<label class="radio" v-if="plantacao.elemento == 'Water'">
														<span class="tag is-success"
														style="background-color: #1D3AA0;">Water</span
														>
													</label>
													<label class="radio" v-if="plantacao.elemento == 'Wind'">
														<span class="tag is-success"
														style="background-color: #236025;">Wind</span
														>
													</label>
													<label class="radio" v-if="plantacao.elemento == 'Parasite'">
														<span class="tag is-success"
														style="background-color: #790B8B;">Parasite</span
														>
													</label>
													<label class="radio" v-if="plantacao.elemento == 'Dark'">
														<span class="tag is-success"
														style="background-color: #5E4771;">Dark</span
														>
													</label>
													<label class="radio" v-if="plantacao.elemento == 'Light'">
														<span class="tag is-success"
														style="background-color: #649CDE;">Light</span
														>
													</label>
													<label class="radio" v-if="plantacao.elemento == 'Metal'">
														<span class="tag is-success"
														style="background-color: #844903;">Metal</span
														>
													</label>
													<label class="radio" v-if="plantacao.elemento == 'N/A'">
														<span class="tag is-success"
														style="background-color: #f03a5f"
														>N/A</span
														>
													</label>																																																																																									
												</div>
											</div>

										</div>
											<label class="checkbox is-size-6" v-if="!plantacao.nft">
												<b class="mr-1 is-size-7">NFT</b>
												<input
													type="checkbox"
													:checked="plantacao.nft"
													disabled
												/>
											</label>
											<label class="is-size-6" v-if="plantacao.nft">
												<b class="mr-1 is-size-7">RARITY</b>
												<div class="tag is-success " :style="{ backgroundColor: plantacao.cor}">
													{{plantacao.raridade}}
												</div>
											</label>
										<div class="field">
											<label class="is-size-7">
												<b>{{ linguagem_atual.id_nft_text }} </b></label
											>
											<div class="control">
												<!-- <input class="input is-small" type="number" placeholder="72" v-model="nova_plantacao.id_planta"> -->
												<span
													class="input is-info is-light is-small is-fullwidth"
													>{{ plantacao.id_planta }}</span
												>
											</div>
										</div>

										<div class="is-flex is-justify-content-space-between">
											<div class="field">
												<label class="label is-small">{{
													linguagem_atual.total_cust_text
												}}</label>
												<span
													class="input is-info is-light is-small is-fullwidth"
													>{{ plantacao.custo_total }}</span
												>
											</div>

											<div class="field">
												<label class="label is-small">{{
													linguagem_atual.production_text
												}}</label>
												<span
													class="input is-info is-light is-small is-fullwidth"
													>{{ plantacao.producao }}</span
												>
											</div>
										</div>

										<div class="field">
											<label class="label is-small">{{
												linguagem_atual.hours_production_text
											}}</label>
											<span
												class="input is-info is-light is-small is-fullwidth"
												>{{ plantacao.horas_producao }}</span
											>
										</div>

										<!-- <div class="field">
                      <label class="label is-small">Dia de plantação
                      <p class="has-text-black is-size-7"> <b> *Não é necessário preencher.</b> </p>
                      </label>
                        <span class="input is-info is-light is-small is-fullwidth">10/10/21</span>
                    </div>                     -->

										<div class="mt-5 is-flex is-justify-content-space-between">
											<button
												class="button is-link is-small"
												@click="duplicar_planta(index)"
											>
												{{ linguagem_atual.duplicated_button_text }}
											</button>
											<button
												class="button is-danger is-small"
												@click="remover_planta(index)"
											>
												{{ linguagem_atual.remove_button_text }}
											</button>
										</div>
									</div>
								</div>

								<div class="column is-4">
									<div class="p-5 has-background-white notification">
										<div class="has-text-black">
											<label class="label is-small">{{
												linguagem_atual.type_text
											}}</label>
											<div class="control">
												<label class="radio">
													<input
														type="radio"
														v-model="nova_plantacao.tipo"
														id="plant"
														value="plant"
														checked
													/>
													Plant
												</label>
												<label class="radio">
													<input
														type="radio"
														v-model="nova_plantacao.tipo"
														id="mother"
														value="mother"
													/>
													Mother Tree
												</label>
											</div>
										</div>

										<label class="checkbox is-size-6">
											<b class="mr-1 is-size-7">NFT</b>
											<input
												type="checkbox"
												v-model="nova_plantacao.nft"
												:checked="
													!isNaN(nova_plantacao.id_planta) &&
														nova_plantacao.id_planta != 0
												"
											/>
										</label>

										<div class="field">
											<label class="is-size-7">
												<b>{{ linguagem_atual.id_nft_text }} </b></label
											>
											<p class="has-text-black is-size-7">
												<b>{{ linguagem_atual.not_necessary_fillin_text }}</b>
											</p>
											<div class="control">
												<input
													class="input is-small"
													type="number"
													placeholder="2009039914"
													v-model="nova_plantacao.id_planta"
												/>
											</div>
										</div>

										<div class="is-flex">
											<div class="field">
												<label class="label is-small">{{
													linguagem_atual.total_cust_text
												}}</label>

												<div class="control">
													<input
														class="input is-small"
														type="number"
														placeholder="150"
														v-model="nova_plantacao.custo_total"
														:disabled="
															nova_plantacao.nft ||
																(!isNaN(nova_plantacao.id_planta) &&
																	nova_plantacao.id_planta != 0)
														"
													/>
												</div>
											</div>

											<div class="ml-2 field">
												<label class="label is-small">{{
													linguagem_atual.production_text
												}}</label>
												<div class="control">
													<input
														class="input is-small"
														type="number"
														placeholder="250"
														v-model="nova_plantacao.producao"
														:disabled="
															!isNaN(nova_plantacao.id_planta) &&
																nova_plantacao.id_planta != 0
														"
													/>
												</div>
											</div>
										</div>

										<div class="field">
											<label class="label is-small">{{
												linguagem_atual.hours_production_text
											}}</label>
											<div class="control">
												<input
													class="input is-small"
													type="number"
													placeholder="72"
													v-model="nova_plantacao.horas_producao"
													:disabled="
														!isNaN(nova_plantacao.id_planta) &&
															nova_plantacao.id_planta != 0
													"
												/>
											</div>
										</div>

										<!-- <div class="field">
                      <label class="label is-small">Dia de plantação
                      <p class="has-text-black is-size-7"> <b> *Não é necessário preencher.</b> </p>
                      </label>
                      <div class="control">
                        <input class="input is-small" type="date">
                      </div>
                    </div>        -->

										<div class="mt-5 has-text-centered">
											<button
												class="button is-primary is-small"
												@click="adicionar_nova_planta(nova_plantacao)"
											>
												Adicionar
											</button>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>

					<div class="column is-4">
						<div class="mb-5 is-size-2 has-text-centered has-text-weight-bold">
							{{ linguagem_atual.earnings_periods_text }}
						</div>
						<div
							class="container p-1 is-size-3 notification"
							style="background: #7F719A;"
						>
						
						<div class="has-text-white has-text-weight-bold">
						<div class="tag is-info">605 LE</div>
						<div class="tag is-black">
							1 PVU
						</div>
						</div>

							<div
								class="is-flex is-align-items-center is-justify-content-space-between"
							>
								<span class="tag is-primary is-large">{{
									linguagem_atual.monetary_text
								}}</span>
								<div class="mt-2 dropdown">
									<div class="dropdown-trigger">
										<button
											class="button"
											aria-haspopup="true"
											aria-controls="dropdown-menu"
										>
											<span>PVU</span>
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
														BRL (R$)
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

							<div
								class="is-flex is-align-items-center is-justify-content-space-between"
							>
								<span class="tag is-primary is-large">{{
									linguagem_atual.seven_days_text
								}}</span>
								<div class="card">
									<div class="card-content">
										<div class="content">
											<div
												class="is-size-5"
												style="border-bottom: solid 1px #ddd;"
											>
												{{ linguagem_atual.profit_text }} :
												{{ ganhos_periodo[0]["lucro"] }} <b>LE</b>
											</div>
											<div
												class="is-size-5"
												style="border-bottom: solid 1px #ddd;"
											>
												{{ linguagem_atual.spent_text }} :
												{{ ganhos_periodo[0]["custo"] }} <b>LE</b>
											</div>
											<div
												class="is-size-5"
												style="border-bottom: solid 1px #ddd;"
											>
												{{ linguagem_atual.produced_text }} :
												{{ ganhos_periodo[0]["produzido"] }} <b>LE</b>
											</div>
											<div class="is-size-5">
												{{ linguagem_atual.revenues_text }} :
												{{ ganhos_periodo[0]["faturamento"] }} <b>PVU</b>
											</div>
										</div>
									</div>
								</div>
							</div>

							<div
								class="mt-3 is-flex is-align-items-center is-justify-content-space-between"
							>
								<span class="tag is-primary is-large">{{
									linguagem_atual.fourteen_days_text
								}}</span>
								<div class="card">
									<div class="card-content">
										<div class="content">
											<div
												class="is-size-5"
												style="border-bottom: solid 1px #ddd;"
											>
												{{ linguagem_atual.profit_text }} :
												{{ ganhos_periodo[1]["lucro"] }} <b>LE</b>
											</div>
											<div
												class="is-size-5"
												style="border-bottom: solid 1px #ddd;"
											>
												{{ linguagem_atual.spent_text }} :
												{{ ganhos_periodo[1]["custo"] }} <b>LE</b>
											</div>
											<div
												class="is-size-5"
												style="border-bottom: solid 1px #ddd;"
											>
												{{ linguagem_atual.produced_text }} :
												{{ ganhos_periodo[1]["produzido"] }} <b>LE</b>
											</div>
											<div class="is-size-5">
												{{ linguagem_atual.revenues_text }} :
												{{ ganhos_periodo[1]["faturamento"] }} <b>PVU</b>
											</div>
										</div>
									</div>
								</div>
							</div>

							<div
								class="mt-3 is-flex is-align-items-center is-justify-content-space-between"
							>
								<span class="tag is-primary is-large">{{
									linguagem_atual.thirty_days_text
								}}</span>
								<div class="card">
									<div class="card-content">
										<div class="content">
											<div
												class="is-size-5"
												style="border-bottom: solid 1px #ddd;"
											>
												{{ linguagem_atual.profit_text }} :
												{{ ganhos_periodo[2]["lucro"] }} <b>LE</b>
											</div>
											<div
												class="is-size-5"
												style="border-bottom: solid 1px #ddd;"
											>
												{{ linguagem_atual.spent_text }} :
												{{ ganhos_periodo[2]["custo"] }} <b>LE</b>
											</div>
											<div
												class="is-size-5"
												style="border-bottom: solid 1px #ddd;"
											>
												{{ linguagem_atual.produced_text }} :
												{{ ganhos_periodo[2]["produzido"] }} <b>LE</b>
											</div>
											<div class="is-size-5">
												{{ linguagem_atual.revenues_text }} :
												{{ ganhos_periodo[2]["faturamento"] }} <b>PVU</b>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
						<button
							class="mt-3 button is-large is-fullwidth is-primary"
							@click="atualizar_valores()"
							:class="is_loading ? 'is-loading' : ''"
						>
							{{ linguagem_atual.update_values_button_text }}
						</button>
					</div>
				</div>
			</div>
		</div>
	</section>
</template>

<script>
	import BrazilIcon from "@/assets/svg/countries/brazil.svg";
	import EuaIcon from "@/assets/svg/countries/eua.svg";
	import SpainIcon from "@/assets/svg/countries/spain.svg";
	
	import portuguese_translate from "@/assets/translations/portuguese.json";
	import english_translate from "@/assets/translations/english.json";
	import spanish_translate from "@/assets/translations/spanish.json";

	export default {
		components: {
			BrazilIcon,
			EuaIcon,
			SpainIcon
		},
		data() {
			return {
				linguagens: {
					portuguese: portuguese_translate,
					english: english_translate,
					spanish: spanish_translate,
				},
				linguagem_atual: portuguese_translate,
				linguagem: "portuguese",
				is_loading: false,
				ganhos_periodo: [
					{ periodo: "7d", produzido: 0, custo: 0, lucro: 0 },
					{ periodo: "14d", produzido: 0, custo: 0, lucro: 0 },
					{ periodo: "30d", produzido: 0, custo: 0, lucro: 0 },
				],
				nova_plantacao: {
					tipo: "plant",
					producao: Number,
					horas_producao: Number,
					custo_total: Number,
					nft: false,
					id_planta: Number,
				},
				listagem_plantacoes: [],
				valores_pvu: {
					dolar: 0,
					volume: 0,
				},
			};
		},
		methods: {
			remover_todas_plantas(){
				this.listagem_plantacoes = [];
				localStorage.setItem("listagem_plantacoes", JSON.stringify([]));
			},
			salvarPlantacoes(plantacoes) {
				localStorage.setItem("listagem_plantacoes", JSON.stringify(plantacoes));
			},
			lerPlantacoes() {
				const plantacoes = JSON.parse(
					localStorage.getItem("listagem_plantacoes")
				);
				if (plantacoes) {
					return plantacoes;
				} else return new Array();
			},
			alterar_linguagem(linguagem) {
				this.linguagem_atual = this.linguagens[linguagem];
				this.linguagem = linguagem;
			},
			adicionar_nova_mama() {
				let nova_plantacao = {
					tipo: "mother",
					producao: 850,
					horas_producao: 144,
					custo_total: 250,
					nft: false,
					id_planta: "N/A",
					imagem: "mama",
				};

				this.listagem_plantacoes.push(nova_plantacao);
				this.salvarPlantacoes(this.listagem_plantacoes);
			},
			adicionar_nova_sapling() {
				let nova_plantacao = {
					tipo: "plant",
					producao: 250,
					horas_producao: 72,
					custo_total: 150,
					nft: false,
					id_planta: "N/A",
					imagem: "sapling",
				};

				this.listagem_plantacoes.push(nova_plantacao);
				this.salvarPlantacoes(this.listagem_plantacoes);
			},
			adicionar_nova_planta(nova_plantacao) {
				if (!isNaN(nova_plantacao.id_planta) && nova_plantacao.id_planta != 0) {
					let teste = this.id_calculate(nova_plantacao.id_planta);
					console.log(teste);
					nova_plantacao.producao = teste["LE"];
					nova_plantacao.horas_producao = teste["hour"];
					nova_plantacao.nft = true;
					nova_plantacao.tipo = teste["type"].split(" ")[0].toLowerCase();
					nova_plantacao.imagem = `${teste["id"]}_${teste["img"]}`;
					nova_plantacao.elemento = teste["element"];
					nova_plantacao.raridade = teste["rarityType"];
					nova_plantacao.cor = teste["color"];
				} else {
					nova_plantacao.id_planta = "N/A";
					nova_plantacao.imagem = "sapling";
					nova_plantacao.elemento = "N/A";
					nova_plantacao.raridade = "N/A";
					nova_plantacao.cor = '#f03a5f';
				}

				if (nova_plantacao.nft == true) {
					nova_plantacao.custo_total = 0;
				}

				console.log(this.listagem_plantacoes);
				if (
					!isNaN(nova_plantacao.producao) &&
					!isNaN(nova_plantacao.horas_producao) &&
					!isNaN(nova_plantacao.custo_total)
				) {
					this.listagem_plantacoes.push(nova_plantacao);
					this.salvarPlantacoes(this.listagem_plantacoes);

					this.nova_plantacao = {
						tipo: "plant",
						producao: Number,
						horas_producao: Number,
						custo_total: Number,
						nft: false,
						id_planta: Number,
					};
				}
				console.log(this.listagem_plantacoes);
			},
			duplicar_planta(index) {
				this.listagem_plantacoes.push(this.listagem_plantacoes[index]);
				this.salvarPlantacoes(this.listagem_plantacoes);
			},
			remover_planta(index) {
				this.listagem_plantacoes.splice(index, 1);
				this.salvarPlantacoes(this.listagem_plantacoes);
			},
			async obter_lucros(listagem_plantacoes) {
				this.is_loading = true;
				console.log(listagem_plantacoes);

				const requestOptions = {
					method: "POST",
					headers: {
						"Content-Type": "application/json",
						"Access-Control-Allow-Origin": "*",
					},
					body: JSON.stringify(listagem_plantacoes),
				};

				let data = await fetch(
					"https://pvu-calculator-api.herokuapp.com/api/obter-periodo-lucros",
					requestOptions
				)
					.then((response) => response.json())
					.then((data) => {
						return data;
					})
					.catch((error) => {
						console.error(error);
					});
				this.is_loading = false;
				return data;
			},
			async atualizar_valores() {
				if (this.listagem_plantacoes.length > 0) {
					this.ganhos_periodo = await this.obter_lucros(
						this.listagem_plantacoes
					);
				}
			},
			async obter_valores_pvu() {
				const requestOptions = {
					method: "GET",
					headers: {
						"Content-Type": "application/json",
						"Access-Control-Allow-Origin": "*",
					},
				};

				let data = await fetch(
					"https://pvu-calculator-api.herokuapp.com/api/obter-valores-pvu",
					requestOptions
				)
					.then((response) => response.json())
					.then((data) => {
						return data;
					})
					.catch((error) => {
						console.error(error);
					});
				this.is_loading = false;
				return data;
			},
		},
		setup() {
			const PlantInfo = [
				{
					id: "0",
					element: "Fire",
					baseLE: [400, 440, 511, 701],
					hour: "48",
					step: "1",
					type: "Plant",
				},
				{
					id: "1",
					element: "Fire",
					baseLE: [400, 440, 511, 701],
					hour: "48",
					step: "1",
					type: "Plant",
				},
				{
					id: "2",
					element: "Ice",
					baseLE: [500, 550, 591, 751],
					hour: "60",
					step: "1",
					type: "Plant",
				},
				{
					id: "3",
					element: "Electro",
					baseLE: [500, 550, 591, 751],
					hour: "48",
					step: "1",
					type: "Plant",
				},
				{
					id: "4",
					element: "Water",
					baseLE: [950, 1040, 1111, 1301],
					hour: "108",
					step: "1",
					type: "Plant",
				},
				{
					id: "5",
					element: "Water",
					baseLE: [950, 1040, 1111, 1301],
					hour: "108",
					step: "1",
					type: "Plant",
				},
				{
					id: "6",
					element: "Ice",
					baseLE: [500, 550, 591, 751],
					hour: "60",
					step: "1",
					type: "Plant",
				},
				{
					id: "7",
					element: "Fire",
					baseLE: [400, 440, 511, 701],
					hour: "48",
					step: "1",
					type: "Plant",
				},
				{
					id: "8",
					element: "Electro",
					baseLE: [500, 550, 591, 751],
					hour: "48",
					step: "1",
					type: "Plant",
				},
				{
					id: "9",
					element: "Wind",
					baseLE: [750, 800, 861, 1051],
					hour: "72",
					step: "1",
					type: "Plant",
				},
				{
					id: "10",
					element: "Wind",
					baseLE: [750, 800, 861, 1051],
					hour: "72",
					step: "1",
					type: "Plant",
				},
				{
					id: "11",
					element: "Parasite",
					baseLE: [900, 950, 1011, 1151],
					hour: "120",
					step: "1",
					type: "Plant",
				},
				{
					id: "12",
					element: "Parasite",
					baseLE: [900, 950, 1011, 1151],
					hour: "120",
					step: "1",
					type: "Plant",
				},
				{
					id: "13",
					element: "Parasite",
					baseLE: [900, 950, 1011, 1151],
					hour: "120",
					step: "1",
					type: "Plant",
				},
				{
					id: "14",
					element: "Dark",
					baseLE: [1200, 1840, 2211, 2401],
					hour: "192",
					step: "10",
					type: "Plant",
				},
				{
					id: "15",
					element: "Electro",
					baseLE: [500, 550, 591, 751],
					hour: "48",
					step: "1",
					type: "Plant",
				},
				{
					id: "16",
					element: "Wind",
					baseLE: [900, 950, 1011, 1151],
					hour: "96",
					step: "1",
					type: "Plant",
				},
				{
					id: "17",
					element: "Fire",
					baseLE: [650, 700, 811, 1001],
					hour: "72",
					step: "1",
					type: "Plant",
				},
				{
					id: "18",
					element: "Light",
					baseLE: [1200, 1250, 1311, 1401],
					hour: "240",
					step: "1",
					type: "Plant",
				},
				{
					id: "19",
					element: "Light",
					baseLE: [1200, 1250, 1311, 1401],
					hour: "240",
					step: "1",
					type: "Plant",
				},
				{
					id: "20",
					element: "Light",
					baseLE: [1600, 1650, 1711, 1901],
					hour: "312",
					step: "1",
					type: "Plant",
				},
				{
					id: "21",
					element: "Light",
					baseLE: [1600, 1650, 1711, 1901],
					hour: "312",
					step: "1",
					type: "Plant",
				},
				{
					id: "22",
					element: "Parasite",
					baseLE: [1300, 1350, 1411, 1551],
					hour: "168",
					step: "1",
					type: "Plant",
				},
				{
					id: "23",
					element: "Parasite",
					baseLE: [1300, 1350, 1411, 1551],
					hour: "168",
					step: "1",
					type: "Plant",
				},
				{
					id: "24",
					element: "Parasite",
					baseLE: [1300, 1350, 1411, 1551],
					hour: "168",
					step: "1",
					type: "Plant",
				},
				{
					id: "25",
					element: "Metal",
					baseLE: [3500, 4240, 4711, 5101],
					hour: "336",
					step: "10",
					type: "Plant",
				},
				{
					id: "26",
					element: "Metal",
					baseLE: [3500, 4240, 4711, 5101],
					hour: "336",
					step: "10",
					type: "Plant",
				},
				{
					id: "27",
					element: "Metal",
					baseLE: [5500, 6340, 6711, 7001],
					hour: "480",
					step: "10",
					type: "Plant",
				},
				{
					id: "28",
					element: "Metal",
					baseLE: [5500, 6340, 6711, 7001],
					hour: "480",
					step: "10",
					type: "Plant",
				},
				{
					id: "29",
					element: "Ice",
					baseLE: [800, 850, 911, 1151],
					hour: "96",
					step: "1",
					type: "Plant",
				},
				{
					id: "30",
					element: "Fire",
					baseLE: [650, 700, 811, 1001],
					hour: "72",
					step: "1",
					type: "Plant",
				},
				{
					id: "31",
					element: "Dark",
					baseLE: [1200, 1840, 2211, 2401],
					hour: "192",
					step: "10",
					type: "Plant",
				},
				{
					id: "32",
					element: "Electro",
					baseLE: [650, 700, 811, 1001],
					hour: "60",
					step: "1",
					type: "Plant",
				},
				{
					id: "33",
					element: "Dark",
					baseLE: [1400, 2040, 2411, 2701],
					hour: "216",
					step: "10",
					type: "Plant",
				},
				{
					id: "34",
					element: "Electro",
					baseLE: [650, 700, 811, 1001],
					hour: "60",
					step: "1",
					type: "Plant",
				},
				{
					id: "35",
					element: "Dark",
					baseLE: [1400, 2040, 2411, 2701],
					hour: "216",
					step: "10",
					type: "Plant",
				},
				{
					id: "36",
					element: "Water",
					baseLE: [950, 1040, 1111, 1301],
					hour: "108",
					step: "1",
					type: "Plant",
				},
				{
					id: "37",
					element: "Wind",
					baseLE: [900, 950, 1011, 1151],
					hour: "96",
					step: "1",
					type: "Plant",
				},
				{
					id: "38",
					element: "Water",
					baseLE: [1050, 1140, 1211, 1401],
					hour: "120",
					step: "1",
					type: "Plant",
				},
				{
					id: "39",
					element: "Water",
					baseLE: [1050, 1140, 1211, 1401],
					hour: "120",
					step: "1",
					type: "Plant",
				},
				{
					id: "90",
					element: "Fire",
					baseLE: [750, 1040, 1211, 1401],
					hour: "48",
					step: "5",
					type: "Mother tree",
				},
				{
					id: "91",
					element: "Light",
					baseLE: [1400, 1690, 1851, 2021],
					hour: "240",
					step: "5",
					type: "Mother tree",
				},
				{
					id: "92",
					element: "Ice",
					baseLE: [1050, 1340, 1511, 1701],
					hour: "96",
					step: "5",
					type: "Mother tree",
				},
				{
					id: "93",
					element: "Dark",
					baseLE: [2600, 2890, 3061, 3201],
					hour: "216",
					step: "5",
					type: "Mother tree",
				},
			];

			const SAPLING = {
				LE: 250,
				hour: "72",
				img: "sapling",
				plantID: "sapling",
				type: "Sapling",
			};

			const MAMA = {
				LE: 850,
				hour: "144",
				img: "mama",
				plantID: "mama",
				type: "Mama",
			};
			const convertID = (plant) => {
				let arrayID = plant.toString().split("");
				// aaa-bb-c-dd-xx
				// let type = `${arrayID[0]}${arrayID[1]}${arrayID[2]}`;
				let id = parseInt(`${arrayID[3]}${arrayID[4]}`);
				let img = `${arrayID[5]}`;
				let rarity = `${arrayID[6]}${arrayID[7]}`;
				return { id, img, rarity };
			};

			const calculateRarity = (num) => {
				let rarityType = "",
					color = "",
					rarityNum = 0;
				let rarity = parseInt(num);
				if (rarity >= 0 && rarity <= 59) {
					rarityType = "Common";
					rarityNum = 0;
					color = "#198754";
				} else if (rarity >= 60 && rarity <= 88) {
					rarityType = "Uncommon";
					rarityNum = 1;
					color = "#0d6efd";
				} else if (rarity >= 89 && rarity <= 98) {
					rarityType = "Rare";
					rarityNum = 2;
					color = "#dc3545";
				} else if (rarity === 99) {
					rarityType = "Mythic";
					rarityNum = 3;
					color = "#6610f2";
				}
				return { rarityType, rarityNum, color };
			};

			const searchPlantId = (id) => {
				return PlantInfo.filter((plant) => {
					return plant.id == id;
				})[0];
			};

			const calculateLE = (baseLE, rarityNum, rarity, step) => {
				let lowestRarity;
				// eslint-disable-next-line default-case
				switch (rarityNum) {
					case 0:
						lowestRarity = 0;
						break;
					case 1:
						lowestRarity = 60;
						break;
					case 2:
						lowestRarity = 89;
						break;
					case 3:
						lowestRarity = 99;
						break;
				}
				return (
					baseLE[rarityNum] + lowestRarity + (rarity - lowestRarity) * step
				);
			};

			const convertToObj = (plantID) => {
				if (isNaN(plantID)) {
					return plantID === "sapling" ? SAPLING : MAMA;
				}
				let { id, img, rarity } = convertID(plantID);
				let plantOBJ = Object.assign(
					searchPlantId(id),
					{
						img,
						rarity,
						LE: "",
						plantID,
					},
					calculateRarity(rarity)
				);
				plantOBJ.LE = calculateLE(
					plantOBJ.baseLE,
					plantOBJ.rarityNum,
					plantOBJ.rarity,
					plantOBJ.step
				);
				let result = {
					...plantOBJ,
				};
				delete result.baseLE;
				delete result.step;
				return result;
			};

			const id_calculate = (id) => {
				if (Array.isArray(id)) {
					let team = id.map((plantID) => {
						return convertToObj(plantID);
					});
					return team;
				} else {
					return convertToObj(id);
				}
			};

			return {
				id_calculate,
			};
		},

		async beforeMount() {
			var values = await this.obter_valores_pvu();
			this.valores_pvu.dolar = values.usd;
			this.valores_pvu.volume = values.volume;
			this.listagem_plantacoes = this.lerPlantacoes(this.listagem_plantacoes);
		},
	};
</script>

<style scoped>
	.bg-primary {
		background-image: url(../assets/img/background.png);
		background-repeat: no-repeat;
		background-size: cover;
		background-position: center;
		background-attachment: fixed;
	}

	.icone-transparent {
		fill-opacity: 50%;
	}
</style>
