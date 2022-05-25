
<template>
  <div>

    <div :id="chartTag" style="width: 100%; height: 400px;"></div>

  </div>
</template>

<script>

//이런식으로 import해서 사용 가능
import * as am5 from "@amcharts/amcharts5";
import * as am5xy from "@amcharts/amcharts5/xy";
import * as am5radar from "@amcharts/amcharts5/radar";
import am5themes_Animated from "@amcharts/amcharts5/themes/Animated";

export default {
name: 'ScoreChart',
methods: {
  drawChart(sscores, chartId){
    
    
am5.ready(function() {

// Create root element
// https://www.amcharts.com/docs/v5/getting-started/#Root_element
let root = am5.Root.new(`chartDiv${chartId}`);
// console.log(root)
// Set themes
// https://www.amcharts.com/docs/v5/concepts/themes/
root.setThemes([
  am5themes_Animated.new(root)
]);

  

// Create chart
// https://www.amcharts.com/docs/v5/charts/radar-chart/
let chart = root.container.children.push(am5radar.RadarChart.new(root, {
  panX: false,
  panY: false,
  //  wheel 효과 삭제
  // wheelX: "panX",
  // wheelY: "zoomX"
}));

// Add cursor 마우스 오버시 나타나는 효과, lineX false로 line나오는 것 삭제함 behavor:zoom 삭제시 마우스 클릭해도 안움직임
// https://www.amcharts.com/docs/v5/charts/radar-chart/#Cursor
const cursor = chart.set("cursor", am5radar.RadarCursor.new(root, {
  // behavior: "zoomX"
}));

cursor.lineX.set("visible", false);
cursor.lineY.set("visible", false);


// Create axes and their renderers
// https://www.amcharts.com/docs/v5/charts/radar-chart/#Adding_axes
var xRenderer = am5radar.AxisRendererCircular.new(root, {});
// var xRenderer = am5radar.AxisRendererCircular.new(root, {});
xRenderer.labels.template.setAll({
  radius: 10,
  
});

let xAxis = chart.xAxes.push(am5xy.CategoryAxis.new(root, {
  maxDeviation: 0,
  categoryField: "score",
  renderer: xRenderer,
  // tooltip: am5.Tooltip.new(root, {})
}));

let yAxis = chart.yAxes.push(am5xy.ValueAxis.new(root, {
  renderer: am5radar.AxisRendererRadial.new(root, {})
}));
//ticks : 말그대로 눈금 말하는거
let yRenderer = yAxis.get("renderer");
// yRenderer.ticks.template.setAll({
  //   stroke: am5.color(0xFF0000),
//   visible: false
// });

//yRenderer.labels : 레이더의 y눈금 숫자
yRenderer.labels.template.setAll({
  // fill: am5.color(0xFF0000),
  // fontSize: "1.5em",
  visible:false
});



// Create series
// https://www.amcharts.com/docs/v5/charts/radar-chart/#Adding_series
let series = chart.series.push(am5radar.RadarLineSeries.new(root, {
  name: "Series",
  xAxis: xAxis,
  yAxis: yAxis,
  valueYField: "litres",
  categoryXField: "score",
  tooltip:am5.Tooltip.new(root, {
    labelText:"{valueY}",

  })
}));
// dot들 색깔 지정
// series.set("fill", am5.color(0xff0000)); 
// chart.get("colors").set("colors", [
//   am5.color(0x095256),
//   am5.color(0x087f8c),
//   am5.color(0x5aaa95),
//   am5.color(0x86a873),
//   am5.color(0xbb9f06)
// ]);


series.strokes.template.setAll({
  strokeWidth: 1
});

series.bullets.push(function () {
  return am5.Bullet.new(root, {
    sprite: am5.Circle.new(root, {
      radius: 7,
      fill: series.get("fill"),
    })
  });
});


// Set data
// https://www.amcharts.com/docs/v5/charts/radar-chart/#Setting_data
let data = [{
  "score": "감독연출",
  "litres": sscores.directing
}, {
  "score": "스토리",
  "litres": sscores.story
}, {
  "score": "영상미",
  "litres": sscores.art
}, {
  "score": "배우연기",
  "litres": sscores.acting
}, {
  "score": "OST",
  "litres": sscores.music
},];
series.data.setAll(data);
xAxis.data.setAll(data);


// Animate chart and series in
// https://www.amcharts.com/docs/v5/concepts/animations/#Initial_animation
series.appear(1000);
chart.appear(1000, 100);

}); // end am5.ready()




  }
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
async mounted(){
  // console.log('mounted')
  // console.log(this.chartId)
  this.drawChart(this.sscores, this.chartId)
},
}
</script>

<!-- Styles -->
<style scoped>

</style>

