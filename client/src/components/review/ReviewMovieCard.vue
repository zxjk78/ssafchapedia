<template>
  <div>
    <div class="max-w-sm bg-white w-52 rounded-lg dark:bg-gray-800 dark:border-gray-700">
    <a href="https://www.naver.com">
        <img class="rounded-t-lg" :src="'https://image.tmdb.org/t/p/w300/'+ movieInfo.poster_path" alt="" />
        <!-- <img :src="imgSrc" alt="포스터 없음"> -->
    </a>
    <div class="mt-1">
        <a href="https://www.naver.com">
            <h5 class="text-lg font-bold tracking-tight text-gray-900 dark:text-white">
              {{movieInfo.title}}
            </h5>
        </a>

    </div>
</div>

  </div>
</template> 

<script>
// import { object } from '@amcharts/amcharts5'
import { fetchMovie } from '@/api/index.js'
export default {
name: 'ReviewMovieCard',
data(){ 
  return {
    movieInfo: '',
} 
},
methods: {
  
},
props:{
  movieId:{
    type:String,
    required:true,
  }
},
computed: {
  imgSrc:function(){
    return "https://image.tmdb.org/t/p/original" + this.movie.poster_path
  }
},

async created(){
  const movie = await fetchMovie(this.movieId)
  this.movieInfo = movie.data

  }
}
</script>

<style>

</style>