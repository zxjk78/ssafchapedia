<template>    
  <div>

<div v-if="toggleModal" id="back" class="w-screen h-screen fixed z-40 inset-0 bg-black flex justify-center items-center" @click="toggleSignupModal2">

<!-- Main modal -->
<div id="signup-form" class="z-50 w-96">
    <div class="relative p-4 w-full max-w-md h-full md:h-auto">
        <!-- Modal content -->
        <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
  
            <div class="py-6 px-6 lg:px-8">
                <h3 class="mb-4 text-2xl font-bold text-center font-medium text-yellow-400">SSAFY</h3>
                <h3 class="mb-4 text-xl text-center font-medium text-gray-900 dark:text-white">회원가입</h3>
                <form class="space-y-6" @submit.prevent="onSubmit">
                    <div>
                        <input type="text" id="id" name="text" v-model="signupInfo.username" class="inp bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" placeholder="아이디" required>
                        <div id="idValiMsg" class="text-sm text-red-300 msgs"></div>
                    </div>  
                    <div>
                        <input type="email" id="email" name="email" v-model="signupInfo.email" placeholder="이메일" class="inp bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" required>
                        <div id="emailValiMsg" class="text-sm text-red-300 msgs"></div>

                    </div>
                    <div>
                        <input type="password" id="pw1" name="password" v-model="signupInfo.password1" placeholder="비밀번호" class="inp bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" required>
                        <div id="pw1ValiMsg" class="text-sm text-red-300 msgs"></div>

                    </div>
                    <div>
                        <input type="password" id="pw2" name="password2" v-model="signupInfo.password2" placeholder="비밀번호 재입력" class="inp bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" required>
                        <div id="pw2ValiMsg" class="text-sm text-red-300 msgs"></div>

                    </div>
                    <div class="flex justify-between">

                        <a href="#" class="text-sm text-blue-700 hover:underline dark:text-blue-500">비밀번호를 잊으셨나요?</a>
                    </div>
                    <button type="submit" class="w-full text-white bg-yellow-300 hover:bg-yellow-400 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">회원가입</button>
                    <div class="text-sm font-medium text-gray-500 dark:text-gray-300">
                        이미 가입하셨나요? <a href="" class="text-blue-700 hover:underline dark:text-blue-500">로그인</a>
                    </div>
                    <!-- <SocialLogin/> -->
                </form>
            </div>
        </div>
    </div>
</div> 
</div>
</div>

</template>

<script>
// import SocialLogin from '@/components/common/SocialLogin.vue'
// 회원가입을 위해 account/signup endpoint로 id, pw1, pw2, email을 axios로 보내는 signup 함수를 사용
import {signup} from '@/api/index.js'
export default {
name: 'SignupForm',
data(){ 
  return {
    signupInfo: {
        username : '',
        password1 : '',
        password2 : '',
        email : '',
    }
  } 
},
props: {

},
methods: {
  toggleSignupModal2(e){
    const back = document.querySelector('#back')
    if (e.target == back)
    this.$store.commit('TOGGLE_SIGNUP_MODAL')
  },
  // 에러메세지 왔을 때 처리하는 함수
  handleSignupError(errorData){
    const msgs =  document.querySelectorAll('.inp')

    msgs.forEach(element => {
      element.addEventListener('input', (e)=>{
        e.target.style.border = ""
        e.target.nextElementSibling.innerText=''
      })
    });

    const {username, password1, password2, email } = errorData
    
    if (username){
      document.querySelector('#id').style.border = "solid 2px red"
      document.querySelector('#idValiMsg').innerText = username[0].slice(1, -1)
      

    }
    if (password1){
      document.querySelector('#pw1').style.border = "solid 2px red"
      document.querySelector('#pw1ValiMsg').innerText = password1[0].slice(1, -1)

    }
    if (password2){
      document.querySelector('#pw2').style.border = "solid 2px red"
      document.querySelector('#pw2ValiMsg').innerText = password2[0].slice(1, -1)
      
    }
    if (email){
      document.querySelector('#email').style.border = "solid 2px red"
      document.querySelector('#emailValiMsg').innerText = email[0].slice(1, -1)
    }



  },



  async onSubmit(){
    // 1. api 서버로 요청 보내는데, 이를 api관련 함수들을 담은 api/index.js의 함수를 호출해서 처리함
    try {
      //2. 성공시 응답 출력하고 home 창으로 이동
      await signup(this.signupInfo)
      // 새로고침해주는 함수는 this.$router.go()
      this.$router.go()
    } catch (error) {
      //3. 실패시 에러 출력
      // console.error('에러응답정보', error.response.data)

      // error.response.data에 계정 관련해서 회원가입이 조건에 안맞는 안된 정보들이 담겨 있고 정보를 dj-rest-auth에서 자체 form에서 화면에 뿌리는 형식이었는데, 
      // 나도 비슷하게 내 signup 폼에다가 뿌림
      this.handleSignupError(error.response.data)
      }
  }
},
computed: {
  toggleModal(){
    return this.$store.state.signupModal
  }
},
components: {
  // SocialLogin
},
}
</script>

<style>
#back {
  background: rgba(0, 0, 0, 0.56)
}

</style>