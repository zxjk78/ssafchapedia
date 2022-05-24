<template>
  <div>
    <div class="flex">
      <img :src="'https://image.tmdb.org/t/p/w200/'+ MovieInfo.poster_path" class="w-20" alt="">
      <div>
        <div><h1 class="text-3xl font-bold">{{MovieInfo.title}}</h1></div>
        <!-- <div>작품 개수: {{movieCnt}}개</div> -->
      </div>
    </div>

    <h1 class="text-2xl font-bold">대표</h1>
      <MovieDetail
      v-if="MovieInfo.pk"
      :movies="MovieInfo.pk"
      :arrType="1"
      />
    <h1>
      {{movieId}}
    </h1>
    <h1 class="text-2xl font-bold">전체</h1>       
      <!-- <MovieDetail
      v-if="MovieInfo.overview"
      :movies="MovieInfo.overview"
      :arrType="2"
      /> -->
  </div>
</template>

<script>
import {fetchMovie} from '@/api/index.js'
import MovieDetail from '@/components/detail/MovieDetail.vue'
export default {
  name: 'MovieDetailView',
  data(){
    return {
      MovieId:this.$route.params.movieId,
      MovieInfo: '',
      movieCnt: ''
    }
  },
  components: {
    MovieDetail,
  },
  async created(){
    const movie = await fetchMovie(this.MovieId)
    this.MovieInfo = movie.data
    this.movieCnt= movie.data.title.length
  }
}
</script>

<style scoped>

</style>