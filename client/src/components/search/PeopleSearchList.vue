<template>
  <div>   
      <h1 class="my-5 text-3xl font-bold">배우 또는 감독 <span>영화 개수</span></h1>

  <PeopleSearch/>
  </div>
</template>

<script>
import PeopleSearch from '@/components/search/PeopleSearch.vue'
export default {
name:'PeopleSearchList',
components: {
  PeopleSearch,
}
}
</script>

<style scoped>

</style>