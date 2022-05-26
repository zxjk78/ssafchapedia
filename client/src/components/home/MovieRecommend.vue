<template>
  <div>

    <!-- <div class="w-1/2 flex justify-around bg-yellow-300"> -->
    <!-- <div class="w-1/2 flex justify-around">
      

    </div> -->
    <h1 class="text-3xl font-bold m-5">당신에게 추천하는 영화</h1>
    <div class="flex justify-around ">
    <div class="inline-block">
      <MovieSelect
      v-for="movie in MovieInfo"
      :movie="movie"
      :key="movie.pk"
      />

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
// import MovieCard from '@/components/home/MovieCardHome.vue'
import MovieSelect from '@/components/home/MovieSelect.vue'
import ScoreChart from '@/components/common/ScoreChart.vue'
import {fetchMovieRandom} from '@/api/index.js'

export default {
  name:'MovieRecommend',
  data(){
    return {
      Movie:this.$route.params.movieId,
      MovieInfo: '',
    }
  },
  components: {
    // MovieCard,
    ScoreChart,
    MovieSelect
  },
  async created(){
    const movieList = await fetchMovieRandom(this.Movie)
    console.log(movieList)
    this.MovieInfo = movieList.data.results
  }
}
</script>

<style>

</style>