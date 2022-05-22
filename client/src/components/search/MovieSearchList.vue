<template>
  <div>
    <h1 class="my-5 text-3xl font-bold">영화 <span>{{movieList.length}}</span></h1>

    <MovieSearch
    v-for="movie in movieList"
    :key="movie.id"
    :movie="movie"
    />

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
    const movieSearchList = await fetchMovieSearchList(keyword)
    
    this.movieList = movieSearchList.data

  } catch (error) {
    console.error(error)
  }
  },
}
</script>

<style>

</style>