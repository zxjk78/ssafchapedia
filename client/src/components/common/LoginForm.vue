<template>    
  <div>

<div v-if="toggleModal" id="back" class="w-screen h-screen fixed z-40 inset-0 bg-black flex justify-center items-center" @click="toggleLoginModal2">

<!-- Main modal -->
<div id="login-form" class="z-50  w-96">
    <div class="relative p-4 w-full max-w-md h-full md:h-auto">
        <!-- Modal content -->
        <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">

            <div class="py-6 px-6 lg:px-8">
                <h3 class="mb-4 text-2xl font-bold text-center font-medium text-yellow-400">SSAFY</h3>
                <h3 class="mb-4 text-xl text-center font-medium text-gray-900 dark:text-white">로그인</h3>
                <form class="space-y-6" @submit.prevent="onSubmit">
                    <div>
                        <input type="text" name="text"  v-model="loginInfo.username" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" placeholder="아이디" required>
                    </div>
                    <div>
                        <input type="password" name="password" v-model="loginInfo.password" placeholder="비밀번호" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" required>
                    </div>
                    <div class="flex justify-between">

                        <a href="#" class="text-sm text-blue-700 hover:underline dark:text-blue-500">비밀번호를 잊으셨나요?</a>
                    </div>
                    <button type="submit" class="w-full text-white bg-yellow-300 hover:bg-yellow-400 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">로그인</button>
                    <div class="text-sm font-medium text-gray-500 dark:text-gray-300">
                        가입하지 않으셨나요? <a href="#" class="text-blue-700 hover:underline dark:text-blue-500">가입하기</a>
                    </div>

                    <SocialLogin/>

                </form>
            </div>
        </div>
    </div>
</div> 
</div>
</div>

</template>

<script>
import SocialLogin from '@/components/common/SocialLogin.vue'
import {login} from '@/api/index.js'
export default {
name: 'LoginForm',
data(){ 
  return {
    loginInfo: {
      username: '',
      password: '',
    },
    
    } 
},
  
props: {
  
  },
methods: {
  toggleLoginModal2(e){
    const back = document.querySelector('#back')
    if (e.target == back)
    this.$store.commit('TOGGLE_LOGIN_MODAL')
  },
  async onSubmit(){
    // 1. 로그인 정보를 담은 객체를 api.js의 해당하는 함수에 전달 후 
    try {
      const res = await login(this.loginInfo)
      console.log(res)
      // 2. 성공하면 응답에 담긴 token을 localstorage, vuex store state에 저장, 로그인폼 끄기

      this.$store.commit('SET_AUTH_TOKEN', res.data.key)
      //vue 새로고침 함수는 this.$router.go()
      this.$router.go()
    } catch (error) {
      // 3. 실패하면 에러
      console.error(error)
    }

  }

},
computed: {
  toggleModal(){
    return this.$store.state.loginModal
  }
},
components: {
  SocialLogin
},



}
</script>

<style>
#back {
  background: rgba(0, 0, 0, 0.56)
}
.social-icons img {
  width: 50px;
  height: 50px;
}

#my-signin2-google > div{
  border-radius: 50%;
}
</style>