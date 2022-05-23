<template>
  <div>
    영화
    {{movieId}}
    <MovieCard
    :movieid="movieId"/>


    <div>
      <form >
        <div class="flex">
          <label for="">감독 연출</label> 
        <div>
          <input type="radio" name="directing" value="1">
          <input type="radio" name="directing" value="2">
          <input type="radio" name="directing" value="3">
        </div>
        </div>

        <div class="">
          <button>제출</button>
          <button>자세한 리뷰 쓰기</button>
        </div>
      </form>
    </div>


  </div>
</template>

<script>
import {fetchMovie} from '@/api/index.js'
import MovieCard from '@/components/common/MovieCard.vue'
export default {
name: 'ReviewCreateView',
data(){
  return {
    movieId: this.$route.params.movieId
  }
},
components: {
  MovieCard,
},
// route를 타고 View가 렌더링 될 때 API와 통신해서 영화 정보를 가지고 옴
created(){
  // console.log(this.$route.params.movieId) // 잘 넘어오는거 확인
  const movieId = this.$route.params.movieId
    try {
      const res = fetchMovie(movieId)
      console.log(res)
      
    } catch (error) {
      console.error(error)
    }

}


}
</script>

<style>

</style>