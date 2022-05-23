<template>
  <div class="flex">
    <img :src="'https://image.tmdb.org/t/p/w300/'+movie.poster_path" alt="" class="w-20">
    <div>
      <div class="font-bold">{{movie.title}}</div>
      <div class="text-gray-500 font-bold">{{release_year}}</div>
    </div>
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
  }
}
}
</script>

<style>

</style>