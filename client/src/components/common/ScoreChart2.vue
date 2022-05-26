<template>
    <div class="w-3/4">
        <canvas :id="chartTag" width="" height=""></canvas>
    </div>
</template>
<script>
import { Chart,registerables } from 'chart.js';
Chart.register(...registerables);
Chart.defaults.font.size = 15;

export default {
    methods: {
        fillData() {
            const ctx = document.getElementById(this.chartTag).getContext('2d');
            this.myChart = new Chart(ctx, {
                type: 'radar',
                data: {
                  labels: ['연출', 'OST', '스토리', '연기', '영상미'],
                  datasets: [
                    {       label: '',
                            data: [this.sscores.directing, this.sscores.music, this.sscores.story, this.sscores.acting, this.sscores.art],
                            fill:true,
                            // backgroundColor: 'rgba(255, 99, 132, 0.2)',
                            backgroundColor: 'rgba(255, 225, 148, 0.5)',
                              
                            
                            borderColor: '#FFB319',
                            pointBackgroundColor: '#FFE3A9',
                            pointBorderColor: '#FFD24C',
                            pointHoverBackgroundColor: '#516BEB',
                            pointHoverBorderColor: 'rgb(255, 99, 132)'
                            
                        }
                    ]
                },
                options: {
                    plugins:{
                      legend: {
                        display: false,
                    },
                    },

                    scale: {
        ticks: {
            max: 3,
            min: 0,
            stepSize: 3
        }
    },

                    scales: {

                          r: {
                              angleLines: {
                                  display: true
                              },
                              beginAtZero: true,
                              max: 3,
                              pointLabels:{
                                font:{
                                  size:20
                                }
                              },

                          },
                          grid:{
                            display: false,
                            drawTicks:false,
                          },
                          gridLines:{
                            display:false,
                          },
                          angleLines:{
                            display:false,
                          },
                          ticks:{
                            display:false, // x y축 삭제
                            stepSize:3,
                            fontColor: '#ffffff',
                            mirror:true,
                            z:1
                          }
                      },

                    elements: {
                        line: {
                            borderWidth: 3,

                        },
                        point:{
                          radius: 10,
                          hoverRadius:15,

                        },

                    }
                }
            });
        }
    },
    mounted() {
        this.fillData(this.sscores);
    },
    data() {
        return {
            myChart: null
        };
    },
    props:{
      sscores: {
      type:Object,
      required: true,
    },
    chartId: {
      type:Number,
      required: true,
    }
    },
    computed:{
    chartTag(){
      return 'chartDiv'+this.chartId
    }
  },
};
</script>
<style scoped>

</style>