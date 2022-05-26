<template>
  <div>
    
    <MovieCardList/>
    <div class="popular-list row row-cols-1 row-cols-md-5 gy-3">
    
    <div v-if="isLoggedIn">

      <MovieRecommend/>
    </div>
    <div v-else>
      <div class="mt-10 flex-col justify-center items-center text-center font-bold text-2xl">
        <div>
        영화 추천 서비스 이용을 위해서는 로그인이 필요합니다. 
        </div>
        <div class="w-1/4 mt-10 mx-auto flex justify-between ">
          <button class="bg-blue-200 p-2 rounded" @click="toggleLoginModal">로그인</button>
          <button class="bg-green-400 p-2 rounded" @click="toggleSignupModal">회원가입</button>
        </div>
      </div>
    </div>
    </div>

  </div>
</template>

<script>
import MovieCardList from '@/components/home/MovieCardList.vue'
import MovieRecommend from '@/components/home/MovieRecommend.vue'

export default {
  name: 'HomeView',
  components: {
    MovieCardList,
    MovieRecommend,
  },
  data(){
    return{
      
    }
  },
  methods:{
    toggleLoginModal(){
    this.$store.commit('TOGGLE_LOGIN_MODAL')
  },
  toggleSignupModal(){
    this.$store.commit('TOGGLE_SIGNUP_MODAL')
  },
  },
  computed:{
    isLoggedIn(){
      return this.$store.getters.isLoggedIn
      // return true
    },
  },
  mounted(){
    // this.getMovies()
  },
  async created(){
    //1.API 서버로 게시글 목록 요청
    //2.성공_> 화면에 출력
    //3.실패->예외처리
    
    
  },
}
</script>

<style>

</style>