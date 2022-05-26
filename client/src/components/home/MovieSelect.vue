<template>
  <div class="max-w-sm bg-white w-52 rounded-lg dark:bg-gray-800 dark:border-gray-700 scale-75">
    <router-link :to="{name:'movie_detail', params:{movieId:movie.pk}}">

        <img :src="'https://image.tmdb.org/t/p/w300/'+movie.poster_path" alt="" class="mx-auto" />
      <!-- </a> -->
    </router-link>
    <div>
      <div class="text-2xl font-bold">{{movie.title}}</div>
      <div class="text-gray-500 text-xl font-bold">⭐{{movie.vote_average}}</div>
    </div>

  </div>
</template>

<script>
// import axios from 'axios'
import {mapState} from 'vuex'
export default {
  name: 'MovieSelect',
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
  async created(){

    const movie_act = this.movie['actors']
    console.log(movie_act)
  }

}
</script>

<style>

</style>