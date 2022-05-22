<template>
  <div>
    <div class="max-w-sm bg-white w-52 rounded-lg dark:bg-gray-800 dark:border-gray-700">
    <a href="https://www.naver.com">
        <!-- <img class="rounded-t-lg" src="https://image.tmdb.org/t/p/w300/6DrHO1jr3qVrViUO6s6kFiAGM7.jpg" alt="" /> -->
        <img :src="imgSrc" alt="포스터 없음">
    </a>
    <div class="mt-1">
        <a href="https://www.naver.com">
            <h5 class="text-lg font-bold tracking-tight text-gray-900 dark:text-white">
              <!-- 범죄도시2 -->
              {{ movie }}
              {{ movie.title }}
            </h5>
        </a>

    </div>
</div>

  </div>
</template> 

<script>
// import { object } from '@amcharts/amcharts5'
// import tmdb from '@/@/fixtures/tmdb.json'
export default {
name: 'MovieCard',
data(){ 
  return {
      dialog: false,
      notifications: false,
      sound: true,
      widgets: false,
} 
},
methods: {
  
},
props:{
  movie:{
    type:Object,
    required:true,
  }
},
computed: {
  imgSrc:function(){
    return "https://image.tmdb.org/t/p/original" + this.movie.poster_path
  }
},
components: {},
}
</script>

<style>

</style>