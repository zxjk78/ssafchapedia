<template>
  <div>
    <div class="flex">
      <img :src="'https://image.tmdb.org/t/p/w200/'+ actorInfo.profile_path" class="w-20" alt="">
      <div>
        <div><h1 class="text-3xl font-bold">{{actorInfo.korean_name}}</h1></div>
        <div>작품 개수: {{movieCnt}}개</div>
      </div>
    </div>
    <!-- 이거 렌더링이 더 빠르게 되서, props로 undefined가 넘어가는 현상: 검색해서 해결
    v-if로 값이 들어와야 렌더링하게 만들어서 자식 컴포넌트의 렌더링을 늦춤 -->
    <h1 class="text-2xl font-bold">대표작</h1>
      <ActorMovieDetail
      v-if="actorInfo.masterpiece"
      :movies="actorInfo.masterpiece"
      :arrType="1"
      />
    <h1 class="text-2xl font-bold">전체</h1>       
      <ActorMovieDetail
      v-if="actorInfo.movies"
      :movies="actorInfo.movies"
      :arrType="2"
      />
  </div>
</template>

<script>
import {fetchActorDetail} from '@/api/index.js'
import ActorMovieDetail from '@/components/detail/ActorMovieDetail.vue'
export default {
  name: 'ActorDetailView',
  data(){
    return {
      actorId:this.$route.params.actorId,
      actorInfo: '',
      movieCnt: ''
    }
  },
  components: {
    ActorMovieDetail,
  },
  async created(){
    const actor = await fetchActorDetail(this.actorId)
    this.actorInfo = actor.data
    this.movieCnt= actor.data.movies.length
  }
}
</script>

<style scoped>

</style>
