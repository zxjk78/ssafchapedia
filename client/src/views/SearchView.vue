<template>
  <div>
    <div class="ml-5">
      <!-- 강제로 re렌더링을 통해 create를 해서 계속 axios를 보내도록 하는 방법 : key를 활용한다. -->
      <MovieSearchList
      :keyword="searchKeyword"
      :key="searchKeyword"/>


      <PeopleSearchList
      :keyword="searchKeyword"
      :key="searchKeyword+1"/>




    </div>



  </div>
</template>

<script>
import MovieSearchList from '@/components/search/MovieSearchList.vue'
import PeopleSearchList from '@/components/search/PeopleSearchList.vue'


export default {
name: 'SearchView',
data() {
  return {
  }
},
components: {
  MovieSearchList,
  PeopleSearchList,
},
computed: {
  searchKeyword(){
    return this.$store.getters.search_keyword
  }
},


}
</script>

<style>

</style>