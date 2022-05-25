<template>
  <div>   

        <div v-if="actorList.length">

      <h1 class="my-5 text-3xl font-bold">배우 <span>{{actorList.length}}</span></h1>

          <PeopleSearch
          v-for="actor in actorList"
          :key="actor.pk"
          :actor="actor"
          />
      </div>
          <div v-else class="my-5 text-3xl font-bold">
            검색 조건에 맞는 배우가 없습니다. 
    </div>

  </div>
</template>

<script>
import PeopleSearch from '@/components/search/PeopleSearch.vue'
import {fetchActorSearchList} from '@/api/index.js'

export default {
name:'PeopleSearchList',
data(){
  return {
    actorList: ''
  }
},
components: {
  PeopleSearch,
},
props:{
  keyword:{
    type:String,
    required: true,
  }
},
computed:{
    searchKeyword(){
    return this.$store.getters.search_keyword
  }
},
  async created() {
    try {
    const keyword = this.keyword
    const actorSearchList = await fetchActorSearchList(keyword)
    
    this.actorList = actorSearchList.data
    // console.log(this.actorList)
  } catch (error) {
    console.error(error)
  }
  },
}
</script>

<style scoped>

</style>