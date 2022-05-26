<template>
  <div class="">

  
    <h1 class="text-3xl font-bold m-5"> <span class="text-cyan-600">{{username}}</span> 님이 좋아하실 만한 <span class="text-cyan-600">{{favorite}}</span>  장르 추천영화들</h1>
    <div class="flex justify-around">
      <div v-if="notExist" class="mt-10 flex-col justify-center items-center text-center font-bold text-2xl">
        <div>
        아직 리뷰를 남긴 영화가 없어 회원님께 영화를 추천해 드릴 수 없습니다. 🤔 
        </div>
        <div class="mt-10">
        영화 페이지에서 리뷰를 남겨주세요 🙏
        </div>
      </div>
    <div v-else class="inline-block flex flex-row">
      <MovieCard
      v-for="movie in movies"
      :key="movie.pk"
      :movie="movie"
      />
    </div>

    </div>
    <div class="w-1/2 here relative inline-block">
      <div class="">
      </div>
      
    </div>
  </div>
</template>

<script>

import {fetchMovieRecommend} from '@/api/index.js'
import MovieCard from '@/components/common/MovieCard.vue'
export default {
  name:'MovieRecommend',
  data(){
    return {
      movies: '',
      favorite: '',
      username: localStorage.getItem('username'),
      notExist: false
    }
  },
  methods:{

  },
  
  components: {
    MovieCard,
  },
  async created(){
    const res = await fetchMovieRecommend()
    if (res.data.notExist){
        this.notExist = true
      } else{        
        this.movies = res.data.data
        this.favorite = res.data.genre
      }
  }
}
</script>

<style>

</style>