<template>
  <div>
    <h1 class="my-5 text-3xl font-bold">영화 <span>영화 개수</span></h1>

    <MovieSearch
    v-for="movie in movies"
    :key="movie.id"
    :movie="movie"
    />

  </div>
</template>

<script>
import MovieSearch from '@/components/search/MovieSearch.vue'
export default {
  name: 'MovieSearchList',
  components: {
    MovieSearch,
  },
  props: {
    movies: {
      type: Array,
      required: true,
    }
  }
}
</script>

<style>

</style>