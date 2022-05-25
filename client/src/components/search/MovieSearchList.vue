<template>
  <div>

    <div v-if="movieList.length">
    <h1 class="my-5 text-3xl font-bold">영화 <span>{{movieList.length}}</span></h1>

    
    <MovieSearch
    v-for="movie in movieList"
    :key="movie.pk"
    :movie="movie"
    class="hover:bg-yellow-200 hover:-translate-y-0.5 hover:scale-105 duration-300"

    />
    </div>


  </div>
  
</template>

<script>
import MovieSearch from '@/components/search/MovieSearch.vue'
import {fetchMovieSearchList} from '@/api/index.js'

export default {
  name: 'MovieSearchList',
  data(){
    return {
      movieList: ''
    }
  },
  components: {
    MovieSearch,
  },
props:{
  keyword:{
    type:String,
    required: true,
  }
},
  async created() {
    try {
    const keyword = this.keyword
    if (!keyword.trim()) return
    const movieSearchList = await fetchMovieSearchList(keyword)
    
    // console.log(this.movieList)
    this.movieList = movieSearchList.data
    this.$store.commit('SET_SEARCH_MOVIE_CNT', this.movieList.length)

  } catch (error) {
    console.error(error)
  }
  },
}
</script>

<style>

</style>