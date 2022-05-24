<template>
  <div>
      <div class="m-2">
      <div>
        <div class="flex justify-around items-center">
        <!-- card 4개 정도 받고, 더보기 하려는 아이콘 -->
        <MovieCard/>
        <MovieCard/>
        <MovieCard/>
        <MovieCard/>
        <router-link to="/"><span class="material-symbols-outlined text-7xl mb-7">
         </span></router-link>

        </div>
      </div>


    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/common/MovieCard.vue'
export default {
  name: 'MyMovieList',
  components: {
    MovieCard,
  }
}
</script>

<style>

</style>