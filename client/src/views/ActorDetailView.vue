<template>
  <div class="relative flex-col justify-center my-24">
    <div class="flex-col w-1/2 mx-auto">
      <img :src="'https://image.tmdb.org/t/p/w200/'+ actorInfo.profile_path" class="w-96 mx-auto" alt="">
      <div>
        <div><h1 class="text-5xl font-bold my-6 text-center">{{actorInfo.korean_name}}</h1></div>
        <div><h1 class="text-3xl font-bold my-2 text-center text-gray-400">{{actorInfo.name}}</h1></div>
        <!-- <div>작품 개수: {{movieCnt}}개</div> -->
      </div>
    </div>
    <!-- 이거 렌더링이 더 빠르게 되서, props로 undefined가 넘어가는 현상: 검색해서 해결
    v-if로 값이 들어와야 렌더링하게 만들어서 자식 컴포넌트의 렌더링을 늦춤 -->
    <h1 class="text-6xl ml-8 my-36 font-bold">대표작🎞 </h1>
      <ActorMovieDetail
      v-if="actorInfo.masterpiece"
      :movies="actorInfo.masterpiece"
      :arrType="1"
      />
      <div class="">
        <ActorMovieDetail
        v-if="actorInfo.movies"
        :movies="actorInfo.movies"
        :arrType="2"
        class="absolute top-0 right-0"
        />
      </div>
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
    try {
      const actor = await fetchActorDetail(this.actorId)
      this.actorInfo = actor.data
      this.movieCnt= actor.data.movies.length
      
    } catch (error) {
      // console.error(error.response.data)

      if (error.response.status == 404){
        this.$router.push({name: 'not_found', params:{errorMsg: '찾으시는 배우는 존재하지 않습니다.'}})
      }
    }
  }
}
</script>

<style scoped>

</style>
