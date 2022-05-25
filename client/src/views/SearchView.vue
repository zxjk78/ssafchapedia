<template>
  <div>
    <div class="ml-10">
      <!-- 강제로 re렌더링을 통해 create를 해서 계속 axios를 보내도록 하는 방법 : key를 활용한다. -->
      <MovieSearchList
      :keyword="searchKeyword"
      :key="searchKeyword"/>


      <PeopleSearchList
      :keyword="searchKeyword"
      :key="searchKeyword+1"/>


      <div v-if="!searchResultExist" class="flex justify-center items-center h-96">
        <div class="text-2xl text-slate-400">
          🎞
        검색 결과가 없습니다. 다른 검색어를 입력해보세요.

        </div>
      </div>

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
  },
  searchResultExist(){
    return this.$store.getters.search_result_exist
  }
},


}
</script>

<style>

</style>