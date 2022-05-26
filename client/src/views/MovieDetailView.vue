<template>
  <div>
    <div class="flex">
      <img :src="movieInfo.poster_path" class="w-80" alt="">
      <div>
        <div><h1 class="text-3xl font-bold">{{movieInfo.title}}</h1></div>
        <!-- <div>작품 개수: {{movieCnt}}개</div> -->
      </div>
    </div>

    <h1 class="text-2xl font-bold">
      대표
    </h1>
   
    <!-- <h1 class="text-2xl font-bold">전체</h1>        -->
    
    <h2 class="text-2xl font-bold">
      <MovieDetail
      v-if="movieInfo"
      :movie="movieInfo"
      :arrType="1"
      />

    </h2>
  </div>

</template>

<script>
import {fetchMovie} from '@/api/index.js'
import MovieDetail from '@/components/detail/MovieDetail.vue'
// import MovieCardList from '@/components/home/MovieCardList'
export default {
  name: 'MovieDetailView',
  data(){
    return {
      MovieId:this.$route.params.movieId,
      movieInfo: '',
      movieCnt: '',
      

    }
  },
  components: {
    MovieDetail,
    
  },
  async created(){
    const movie = await fetchMovie(this.MovieId)
    this.movieInfo = movie.data
    this.movieCnt= movie.data.title.length
    this.movieInfo.poster_path = this.$store.state.tmdbImgUrl + movie.data.poster_path
    console.log(movie.data)
  },
  
}
</script>

<style scoped>

</style>