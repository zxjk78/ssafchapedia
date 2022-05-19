<template>
  <div >
    Home
    <h1 class="underline">테일윈드 작동하나요??</h1>
  </div>
</template>

<script>
import {fetchArticleList} from '@/api/index.js'
export default {
  name: 'HomeView',
  async created(){
    //1.API 서버로 게시글 목록 요청
    const res = await fetchArticleList()
    console.log(res)
    //2.성공_> 화면에 출력
    //3.실패->예외처리
  }
}
</script>

<style>

</style>