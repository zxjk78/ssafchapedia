<template>
  <div class="flex-col">
        <router-link :to="{name:'movie_detail', params:{movieId:movie.pk}}">

    <img :src="poster_path" alt="" class="w-40">
        </router-link>


  </div>
</template>

<script>
export default {
  name: 'ActMovNormal',
  data(){
    return {}
  },
  props: {
    movie: {
      type:Object,
      required: true,
    }
  },
computed: {
  release_year(){
    const tmp = this.movie.release_date.slice(0,4)
    return tmp
  },
  poster_path(){
    const tmp = this.$store.state.tmdbImgUrl + this.movie.poster_path
    return tmp
  }
}
}
</script>

<style>

</style>