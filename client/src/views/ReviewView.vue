<template>
  <div>
    <!-- 영화 카드 이미지 보여줌 -->
    <ReviewMovieCard/>


  </div>
</template>

<script>
import ReviewMovieCard from '@/components/review/ReviewMovieCard.vue'
export default {
name: 'ReviewView',
components: {
  ReviewMovieCard,
},


}
</script>

<style>

</style>