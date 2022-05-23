<template>
  <div>   
      <h1 class="my-5 text-3xl font-bold">배우 <span>{{actorList.length}}</span></h1>

  <PeopleSearch
  v-for="actor in actorList"
  :key="actor.id"
  :actor="actor"
  />
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
    
    console.log(actorSearchList.data)
    this.actorList = actorSearchList.data
  } catch (error) {
    console.error(error)
  }
  },
}
</script>

<style scoped>

</style>