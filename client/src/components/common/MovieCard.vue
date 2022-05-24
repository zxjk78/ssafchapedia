<template>
  <div class="text-center">
    <router-link :to="{name:'home'}">
    <img :src="'https://image.tmdb.org/t/p/w300/'+movie.poster_path" alt="" class="mx-auto">
    </router-link>
    <div>
      <div class="text-2xl font-bold">{{movie.title}}</div>
      <div class="text-gray-500 text-xl font-bold">⭐{{movie.vote_average}}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieCard',
  data(){
    return {}
  },
  props: {
    movie: {
      type:Object,
      required: true,
    }
  },

}
</script>

<style>

</style>