<template>
  <div>
    <div class="ml-5">

      <MovieSearchList/>


      <PeopleSearchList/>

      <h1>감독 <span>감독 명수</span></h1>


    </div>



  </div>
</template>

<script>
import MovieSearchList from '@/components/search/MovieSearchList.vue'
import PeopleSearchList from '@/components/search/PeopleSearchList.vue'
export default {
name: 'SearchView',
components: {
  MovieSearchList,
  PeopleSearchList,
},
}
</script>

<style>

</style>