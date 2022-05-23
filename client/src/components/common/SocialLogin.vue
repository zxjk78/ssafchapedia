<template>
  <div>
      <hr>
      <div class="flex mt-3 justify-around social-icons">
        <a :href="google_path"><img src="@/assets/login/google-g-2015-logo-png-transparent.png" alt=""></a>
        <a :href="naver_path"><img src="@/assets/login/btnG_icon_circle.png" alt=""></a>
        <a :href="kakao_path"><img src="@/assets/login/ico-kakao.png" alt=""></a>
      </div>
  </div>
</template>

<script>
export default {
name: 'SocialLogin',
data() {
  return {
    SERVER_OAUTH_LOGIN_URL: 'http://localhost:8000/accounts',
    KAKAO_PATH: '/kakao/login',
    NAVER_PATH: '/naver/login',
    GOOGLE_PATH: '/google/login',

  }
},
computed: {
  kakao_path(){
    return this.SERVER_OAUTH_LOGIN_URL + this.KAKAO_PATH
  },
  google_path(){
    return this.SERVER_OAUTH_LOGIN_URL + this.GOOGLE_PATH
  },
  naver_path(){
    return this.SERVER_OAUTH_LOGIN_URL + this.NAVER_PATH
  },
}
}
</script>

<style>

</style>