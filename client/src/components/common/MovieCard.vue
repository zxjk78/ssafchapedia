<template>
  <div class="text-center">
    <router-link :to="{name:'home'}">
    <img :src="'https://image.tmdb.org/t/p/w300/'+movie.poster_path" alt="" class="mx-auto">
    </router-link>
    <div>
      <div class="text-2xl font-bold">{{movie.title}}</div>
      <div class="text-gray-500 text-xl font-bold">⭐{{movie.vote_average}}</div>
    </div>
    <!-- <div>
      <b-modal size="lg" :title="`${movie.title}`">
        <img :src="movie.poster_path" alt="movie poster" id="movie_image"/>
        <h5>배우 {{movie.actor}}</h5>
        <h5>{{movie.popularity}}</h5>
      </b-modal>
    </div> -->
  </div>
</template>

<script>
// import axios from 'axios'
import {mapState} from 'vuex'
export default {
  name: 'MovieCard',
  data(){
    return {}
  },
  computed:{
    ...mapState(['movieInfo'])
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