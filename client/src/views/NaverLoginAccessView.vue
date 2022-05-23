<template>
  <div></div>
</template>

<script>
export default {
mounted() {
    const NAVER_LOGIN_CLIENT_ID = 'QzQ846KTZpYwA62JSExY'
    const NAVER_LOGIN_CALLBACK_URL = 'http://localhost:8080/accounts/naver/login/callback/'
    const naver_id_login = new window.naver_id_login(NAVER_LOGIN_CLIENT_ID, NAVER_LOGIN_CALLBACK_URL);
    const accessToken = naver_id_login.getAccessToken()
    console.log("access token", naver_id_login.getAccessToken()); // 정상적 로그인이 된 경우 access token값 출력
    localStorage.setItem('naverAccessToken', accessToken); // 앞으로는 담아 보낼 수 있도록한다. 
  },
}
</script>

<style>

</style>