<template>
  <div>
    
    <nav>
      
      <div class="flex justify-between items-center my-2">
        <h2 class="ml-8 text-3xl text-yellow-400 font-bold	">SSAFY</h2>
        <div class="flex items-center relative">
        <svg class="w-5 h-5 absolute left-20 ml-5 text-slate-400 " fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd"></path></svg>
        <input type="text" class="text-center w-96 h-10 bg-slate-100  rounded-lg	ml-20	" placeholder="감독명, 작품, 배우를 검색해보세요.">

        </div>
      <div class="w-56 flex justify-around">
        <button @click="toggleLoginModal">로그인</button>
        <button @click="toggleSignupModal" class="p-2 border-2 rounded-lg">회원가입</button>
      </div>
      

      </div>

    </nav>




  <LoginForm/>
  <SignupForm/>

  </div>
</template>

<script>
import LoginForm from '@/components/LoginForm.vue'
import SignupForm from '@/components/SignupForm.vue'

export default {
name: 'theNavbar',
data(){ 
  return {

} 
},
methods: {
  toggleLoginModal(){
    this.$store.commit('TOGGLE_LOGIN_MODAL')
  },
  toggleSignupModal(){
    this.$store.commit('TOGGLE_SIGNUP_MODAL')
  },
},
computed: {},
components: {
  LoginForm,
  SignupForm,
},
}
</script>

<style>

</style>