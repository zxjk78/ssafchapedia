<template>
<form v-on:submit.prevent="onSubmit">

  <div class="max-w-sm bg-white w-52 rounded-lg dark:bg-gray-800 dark:border-gray-700 scale-75">
    <div class="flex flex-wrap">
        <router-link :to="{name:'actor_detail', params:{actorId:actor.pk}}">

        <img :src="'https://image.tmdb.org/t/p/w300/'+actor.profile_path" alt="" class="mx-auto flex flex-wrap" />
        <!-- </a> -->
        </router-link>
        <!-- <div> -->
          <div class="text-2xl font-bold">⭐{{actor.korean_name}}</div>
          <div>
            <!-- <router-link :to="{name:'profile', params:{username:username}}"> -->
              <!-- '/:username/profile' 클릭 시 마이페이지에 저장-->
              
              <!-- doThis:이벤트를 한번만 실행 -->
              <UserFavoriteActor/>
              <button class="favor text-xl font-bold" @click="doThis()">⭐선택</button>
            <!-- </router-link> -->
          </div>
          <!-- <div class="text-gray-500 text-xl font-bold">⭐{{actor.vote_average}}</div> -->
        <!-- </div> -->
    </div>
    

  </div>
</form>
</template>

<script>
// import axios from 'axios'
import {mapState} from 'vuex'
import UserFavoriteActor from '@/components/profile/MovieSelect'
export default {
  name: 'MovieSelect',
  data(){
    return {
        username: this.$route.params.username,

    }
  },
  components:{
    UserFavoriteActor
  },
  computed:{
    ...mapState(['actorInfo'])
  },
  props: {
    actor: {
      type:Object,
      required: true,
    },
    
  },
  methods:{
    // favor:function(){
    //   <UserFavoriteActor/>
    // }
  },
  async created(){
    console.log(this.username)
    // console.log(this.userid)
    // const movie_act = this.movie['actors']
    // console.log(this.movie)
    // console.log(movie_act)
  }

}
</script>

<style>

</style>