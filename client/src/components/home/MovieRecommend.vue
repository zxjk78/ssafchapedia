<template>
  <div>

    <!-- <div class="w-1/2 flex justify-around bg-yellow-300"> -->
    <!-- <div class="w-1/2 flex justify-around">
      

    </div> -->
    <h1 class="text-3xl font-bold m-5">당신에게 추천하는 영화</h1>
    <div class="flex justify-around ">
    <div class="inline-block">
      <MovieCard/>

    </div>
    <div class="w-1/2 here relative inline-block">
      <div class="">
      <ScoreChart/>
      </div>
      
    </div>

    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/common/MovieCard.vue'
import ScoreChart from '@/components/common/ScoreChart.vue'
export default {
  name:'MovieRecommend',
  data(){
    return {}
  },
  components: {
    MovieCard,
    ScoreChart,
  }

}
</script>

<style>

</style>