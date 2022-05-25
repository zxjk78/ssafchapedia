<template>
  <div>
      <div class="flex gap-2">
      <div class="bg-red-100">
        <router-link :to="{name: 'actor_detail', params:{actorId:actor.pk}}"><img :src="actor_renew.profile_path" class="w-32" alt=""></router-link>
      </div>
      <div class="w-1/3 flex flex-col justify-start gap-y-4">
        <div class="font-bold text-2xl">{{actor_renew.korean_name}}</div>
        <div class="font-bold text-slate-500">작품 {{actor_renew.movies.length}}개</div>
        </div>
    </div>   
  </div>
</template>

<script>
export default {
name:'PeopleSearch',
props:{
    actor: {
    type:Object,
    required: true,
  }
},
computed:{
  actor_renew(){
    const {korean_name, profile_path, movies } = this.actor

    const actor2 = {korean_name, profile_path, movies}
    actor2.profile_path = `https://image.tmdb.org/t/p/w500/${actor2.profile_path}`

    return actor2
  }
}
}
</script>

<style scoped>

</style>