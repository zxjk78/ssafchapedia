<template>
  <div>

    <!-- <div class="w-1/2 flex justify-around bg-yellow-300"> -->
    <!-- <div class="w-1/2 flex justify-around">
      

    </div> -->
  
    <h1 class="text-3xl font-bold m-5">당신에게 추천하는 영화배우</h1>
    <div class="flex justify-around " id="actor_select">
    <div class="inline-block flex flex-row">
      <MovieSelect
      v-for="actor in ActorInfo"
      :actor="actor"
      :key="actor.pk"
      />
      <button v-on:click="refresh">이 중에 없으신가요?</button>
    </div>

    </div>
    <div class="w-1/2 here relative inline-block">
      <div class="">
      <!-- <ScoreChart/> -->
      </div>
      
    </div>
  </div>
</template>

<script>
// import MovieCard from '@/components/home/MovieCardHome.vue'
import MovieSelect from '@/components/home/MovieSelect.vue'
// import ScoreChart from '@/components/common/ScoreChart.vue'
import {fetchMovieRandom} from '@/api/index.js'

export default {
  name:'MovieRecommend',
  data(){
    return {
      Actor:this.$route.params.movieId,
      ActorInfo: '',
    }
  },
  methods:{
    refresh(){
      // this.$actor_select.load(window.location.href+"actor_select")
      //새로고침
      this.$router.go()
    }
  },
  components: {
    // MovieCard,
    // ScoreChart,
    MovieSelect
  },
  async created(){
    const actorList = await fetchMovieRandom(this.Actor)
    this.ActorInfo = actorList.data
    console.log(this.ActorInfo)
  }
}
</script>

<style>

</style>