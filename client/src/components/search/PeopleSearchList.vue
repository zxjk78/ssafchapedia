<template>
  <div>   

        <div v-if="actorList.length">

      <h1 class="my-5 text-3xl font-bold">배우 <span>{{actorList.length}}</span></h1>

          <PeopleSearch
          v-for="actor in actorList"
          :key="actor.pk"
          :actor="actor"
          class="hover:bg-yellow-200 hover:-translate-y-0.5 hover:scale-105 duration-300"

          />
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
    if (!keyword.trim()) return
    const actorSearchList = await fetchActorSearchList(keyword)
    
    this.actorList = actorSearchList.data
    this.$store.commit('SET_SEARCH_ACTOR_CNT', this.actorList.length)
    // console.log(this.actorList)
  } catch (error) {
    console.error(error)
  }
  },
}
</script>

<style scoped>

</style>