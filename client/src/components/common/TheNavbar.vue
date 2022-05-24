<template>
  <div>
      <!-- <div id="naver_id_login"></div> -->

    <nav>


      <div class="flex justify-between items-center my-2">
        <a href="/">
        <h2 class="ml-8 text-3xl text-yellow-400 font-bold">SSAFY</h2>
        </a>
        <div class="flex items-center relative">
        <svg class="w-5 h-5 absolute left-20 ml-5 text-slate-400 " fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd"></path></svg>
        <input type="text" class="text-center w-96 h-10 bg-slate-100 rounded-lg	ml-20	" placeholder="감독명, 작품, 배우를 검색해보세요." @input="onSearchDebounce">

        </div>

        
      <div v-if="isLoggedIn" class="w-56 flex justify-around items-center">
        <span class="material-symbols-outlined text-3xl">
        account_circle
        </span>
        
        <!-- <router-link :to="{name:'profile'}" class="bg-yello-400">마이페이지</router-link> -->
        <button class="bg-yello-400" @click="getMyInfo">마이페이지</button>
        <button class="border-2 border-yellow-400	" @click="logout">로그아웃</button>
      </div>
      <div v-else class="w-56 flex justify-around">
        <button class="" @click="toggleLoginModal">로그인</button>
        <button class="" @click="toggleSignupModal" >회원가입</button>
      </div>
      
      </div>

    </nav>




  <LoginForm/>
  <SignupForm/>



  </div>
</template>

<script>
import LoginForm from '@/components/common/LoginForm.vue'
import SignupForm from '@/components/common/SignupForm.vue'
import {getMyInfo} from '@/api/index.js'
import _ from 'lodash'

export default {
name: 'theNavbar',
data(){ 
  return {
    showLogin: this.$store.state.loginModal, 
    showSignup: this.$store.state.loginModal, 
    
} 
},
methods: {
  toggleLoginModal(){
    this.$store.commit('TOGGLE_LOGIN_MODAL')
  },
  toggleSignupModal(){
    this.$store.commit('TOGGLE_SIGNUP_MODAL')
  },

  // onSearchDebounce: _.debounce(function(event){      
  onSearchDebounce: _.debounce(function(event){      
      //v-model 한글 연동문제 있어서 event.target.value로 변경
      // this.$store.dispatch('keywordSearch', event.target.value)

      const keyword = event.target.value
      if (!keyword) return // 비었을 때는 작동 X
      this.$store.commit('SET_SEARCH_KEYWORD', keyword)

      if (document.location.pathname != '/search') {
        this.$router.push({name: 'search'}).catch(err=>{
          if (err.name === 'NavigationDuplicated'){
            return
          }
        })
      }
      }, 300),

  logout(){
    this.$store.commit('LOGOUT')
  },
  async getMyInfo(){
    const res = await getMyInfo()
    this.$store.commit('SET_USERNAME', res.data.username)
    this.$router.push({name:'profile', params:{username: this.$store.state.username}})
  },




},
computed: {
  isLoggedIn(){
      return this.$store.getters.isLoggedIn
      // return true
    },
  getUserName(){
    return this.$store.getters.getUserName
  },
},
components: {
  LoginForm,
  SignupForm,
},


}
</script>

<style>
.material-symbols-outlined {
  font-variation-settings:
  'FILL' 1,
  'wght' 400,
  'GRAD' 0,
  'opsz' 48
}
</style>