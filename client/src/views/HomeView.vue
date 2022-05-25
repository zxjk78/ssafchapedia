<template>
  <div>
    
    <MovieCardList/>
    <div class="popular-list row row-cols-1 row-cols-md-5 gy-3">
    <!-- <MovieDetail
        v-for="(movie, idx) in movies"
        :key="idx"
        :movie="movie"/> -->
    <MovieRecommend/>
    
    </div>

  </div>
</template>

<script>
import MovieCardList from '@/components/home/MovieCardList.vue'
import MovieRecommend from '@/components/home/MovieRecommend.vue'
// import axios from 'axios'

export default {
  name: 'HomeView',
  components: {
    // MovieCard,
    MovieCardList,
    MovieRecommend,
    // MovieDetail,
  },
  data(){
    return{
      
    }
  },
  methods:{
    
  },
  mounted(){
    // this.getMovies()
  },
  async created(){
    //1.API 서버로 게시글 목록 요청
    //2.성공_> 화면에 출력
    //3.실패->예외처리
    
    
  }
}
</script>

<style>

</style>