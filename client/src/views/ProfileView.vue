<template>
  <div>
    <div class="my-picture">
      여기 이미지는 DB에서 내가 본 영화 중에서 아무거나 poster path 가져와서 붙이기
      <img src="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjAyMTRfMjE2%2FMDAxNjQ0ODExMDA1MTI1.EE08QdhHev5V9om2NoY6FNXuOvSw0eprGCHeshrLIugg.u8hy7r21VlaaEvP4UV7nBA3rVjrkxZzqoIyuRPBo4oIg.JPEG.mssixx%2FIMG_1336.JPG&type=sc960_832" 
      alt="프로필이미지"
      class="w-12 h-12">
    </div>
    <div class="text-3xl">
      유저 이름
    </div>
    <MyMovieList/>


  </div>
</template>

<script>
import MyMovieList from '@/components/profile/MyMovieList.vue'
export default {
  name:'ProfileView',
  data(){return {}},
  components:{
    MyMovieList,
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