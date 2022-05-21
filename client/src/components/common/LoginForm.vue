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
                <form class="space-y-6" action="#">
                    <div>
                        <input type="text" name="text" id="text" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" placeholder="아이디" required>
                    </div>
                    <div>
                        <input type="password" name="password" id="password" placeholder="비밀번호" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" required>
                    </div>
                    <div class="flex justify-between">

                        <a href="#" class="text-sm text-blue-700 hover:underline dark:text-blue-500">비밀번호를 잊으셨나요?</a>
                    </div>
                    <button type="submit" class="w-full text-white bg-yellow-300 hover:bg-yellow-400 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">로그인</button>
                    <div class="text-sm font-medium text-gray-500 dark:text-gray-300">
                        가입하지 않으셨나요? <a href="#" class="text-blue-700 hover:underline dark:text-blue-500">가입하기</a>
                    </div>

                    <hr>
                                  

                    <div class="flex justify-around social-icons">
                      
                      <div id="naver_id_login"></div>

                      <div id="my-signin2-google"></div>
                      <a href="#"><img src="@/assets/login/ico-kakao.png" alt=""></a>
                      

                    </div>

                </form>
            </div>
        </div>
    </div>
</div> 
</div>
</div>

</template>

<script>
export default {
name: 'LoginForm',
data(){ 
  // 수정 필요한 부분, 나중에 링크 달아줘야 한다.
  return {
    
    
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

  // google signin btn에서 사용되는 함수들 
  onSuccess(googleUser) {
      // eslint-disable-next-line
      console.log(googleUser);
      this.googleUser = googleUser.getBasicProfile();
    },
    onFailure(error) {
      // eslint-disable-next-line
      console.log(error);
    },

  createNaverLogin(){
    const NAVER_LOGIN_CLIENT_ID = 'QzQ846KTZpYwA62JSExY'
    const NAVER_LOGIN_CALLBACK_URL = 'http://localhost:8000/accounts/naver/login/callback/'

    var naver_id_login = new naver_id_login(NAVER_LOGIN_CLIENT_ID, NAVER_LOGIN_CALLBACK_URL);
    naver_id_login.setButton("white", 3,40); //네이버 로그인 버튼 설정
    naver_id_login.setPopup(); //Popup형태의 인증 진행
    naver_id_login.init_naver_id_login();
  }

},
computed: {
  toggleModal(){
    return this.$store.state.loginModal
  }
},
updated() { // 값이 바뀔 때: 즉 state의 값이 바뀔 때를 hookup하기 때문에 created, mounted 가 아닌  update를 사용
// 공식 문서에 따르면 스타일링에서 바꿀 수 있는 값은 한정되어 있음,
    window.gapi.signin2.render('my-signin2-google', {
      scope: 'profile email',
      width:  50,
      height: 50,
      // longtitle: true,
      // theme: 'dark',
      onsuccess: this.onSuccess,
      onfailure: this.onFailure,
    });



    const NAVER_LOGIN_CLIENT_ID = 'QzQ846KTZpYwA62JSExY'
    const NAVER_LOGIN_CALLBACK_URL = 'http://localhost:8000/accounts/naver/login/callback/'
    const naver_id_login = new window.naver_id_login(NAVER_LOGIN_CLIENT_ID, NAVER_LOGIN_CALLBACK_URL);
    const state = naver_id_login.getUniqState();
    naver_id_login.setButton("green", 1,40); // 버튼 설정
    naver_id_login.setState(state);
    // naver_id_login.setPopup(); // popup 설정을 위한 코드
    naver_id_login.init_naver_id_login();





  },
  head: {
    script: [
    { src: 'https://static.nid.naver.com/js/naveridlogin_js_sdk_2.0.0.js' },
    { src: 'http://code.jquery.com/jquery-1.11.3.min.js' },
  ]
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