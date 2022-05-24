<template>
  <div>
    <template v-if="arrType==1">
    <div class="grid grid-cols-3">

    <MovieCard
    v-for="movie in movies"
    :key="movie.id"
    :movie="movie"
    />    
          </div>

    </template>
    
    <template v-if="arrType==2">
      <div class="grid grid-cols-3">
        <MovieCard
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
        />    
      </div>
    </template>

  </div>
</template>

<script>
import MovieCard from '@/components/common/MovieCard'
export default {
name: 'MovieDetail',
props: {
  arrType: {
    type: Array,
    required: true,
  },
  movies: {
    type: Array,
    required: true,
  },


},
components: {
  MovieCard
},


}
</script>

<style>

</style>