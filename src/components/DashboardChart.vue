<template>
	<div :ref="chart.uuid"></div>
</template>

<script>
	import Plotly from "plotly.js-dist";
	import _ from "lodash";

	export default {
		props: {
			layout_extra_opts: {
				type: Object,
				default: (() => {}),
			},
			chart: {
				type: Object
			},
			yaxis_title: {
				type: String,
				default: ""
			},
			xaxis_title: {
				type: String,
				default: ""
			},
			xaxis_side: {
				type: String,
				default: "bottom"
			},
			xaxis_showgrid: {
				type: Boolean,
				default: false
			},
			xaxis_tickformat: {
				type: String,
				default: "%d-%m-%Y %H:%m"
			},
			xaxis_dtick: {
				type: Number,
				default: 172800000 // tempo em milissegundos (atualmente 48H)
			},
			xaxis_spikemode: {
				type: String,
				default: "toaxis+across+marker"
			},
			chart_height: {
				type: Number,
				default: 300
			},
			legend_x: {
				type: Number,
				default: 1.01
			},
			legend_y: {
				type: Number,
				default: 1.01
			},
			legend_xanchor: {
				type: String,
				default: "right"
			},
			legend_yanchor: {
				type: String,
				default: "bottom"
			},
			legend_fontsize: {
				type: Number,
				default: 11
			},
			display_modebar: {
				type: Boolean,
				default: false
			}
		},

		data() {
			return {
				layout: {
					height: this.chart_height,
					separators: ".",
					xaxis: {
						ticklabelposition: "outsite bottom",
						title: this.xaxis_title,
						automargin: true,
						side: this.xaxis_side,
						showgrid: this.xaxis_showgrid,
						tickformat: this.xaxis_tickformat,
						spikemode: this.xaxis_spikemode,
						spikesnap: "cursor",
						spikethickness: 1,
						spikedash: "solid",
						dtick: this.xaxis_dtick
					},
					yaxis: {
						title: {
							standoff: 20,
							text: this.yaxis_title
						},
						yref: "paper",
						xref: "paper",
						side: "left",
						automargin: true,
						hoverformat: ".2f"
					},
					margin: {
						pad: 10,
						r: 0,
						l: 20,
						t: 0,
						b: 30
					},
					legend: {
						x: this.legend_x,
						y: this.legend_y,
						xanchor: this.legend_xanchor,
						yanchor: this.legend_yanchor,
						orientation: "h",
						font: {
							size: this.legend_fontsize
						}
					}
				},
				rangerOptions: {
					buttons: [
						{
							count: 7,
							label: "7 dias",
							step: "day",
							stepmode: "backward"
						},
						{
							count: 14,
							label: "14 dias",
							step: "day",
							stepmode: "backward"
						},
						{
							label: "Periodo Atual",
							step: "all"
						}
					]
				}
			};
		},
		computed: {

			updated_layout() {
				let layout_cp = this.layout
				return _.merge(layout_cp, this.layout_extra_opts);
			}

		},
		mounted() {
			Plotly.newPlot(
				this.$refs[this.chart.uuid],
				this.chart.traces,
				this.updated_layout,
				{
					responsive: true,
					scrollZoom: false,
					displaylogo: false,

					// plotly icon list = console.log(Plotly.Icons)
					modeBarButtonsToAdd: [
						[
							{
								name: "Download",
								icon: Plotly.Icons.camera,
								click: function(gd) {
									Plotly.downloadImage(gd, {
										filename: "grafico",
										format: "png",
										width: gd._fullLayout.width,
										height: gd._fullLayout.height
									});
								}
							}
						]
					],
					displayModeBar: this.display_modebar,

					// plotly mode bar buttons list:
					// https://github.com/plotly/plotly.js/blob/master/src/components/modebar/buttons.js
					modeBarButtonsToRemove: [
						"pan2d",
						"resetScale2d",
						"toImage",
						"toggleSpikelines",
						"hoverCompareCartesian",
						"hoverClosestGl2d",
						"hoverClosestCartesian",
						"zoomIn2d",
						"zoomOut2d",
						"autoScale2d",
						"lasso2d"
					]
				}
			);
		},
		methods: {
			formatarLayout: function() {
				this.layout.height = 600;

				// this.layout.xaxis.rangeselector = this.rangerOptions;
			}
		},
		watch: {
			chart: {
				handler: function() {
					Plotly.react(
						this.$refs[this.chart.uuid],
						this.chart.traces,
						this.layout
					);
				},
				deep: true
			}
		}
	};
</script>