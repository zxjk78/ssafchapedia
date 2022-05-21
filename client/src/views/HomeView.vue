<template>
  <div>
    
    <MovieCardList/>
    <MovieRecommend/>

  </div>
</template>

<script>
import {fetchArticleList} from '@/api/index.js'
// import MovieCard from '@/components/MovieCard.vue'
import MovieCardList from '@/components/home/MovieCardList.vue'
import MovieRecommend from '@/components/home/MovieRecommend.vue'


export default {
  name: 'HomeView',
  components: {
    // MovieCard,
    MovieCardList,
    MovieRecommend,
  },
  async created(){
    //1.API 서버로 게시글 목록 요청
    const res = await fetchArticleList()
    console.log(res)
    //2.성공_> 화면에 출력
    //3.실패->예외처리
  }
}
</script>

<style>

</style>