<template>
  <div>
    <ReviewMovieCard
    :movieId="movieId"/>


    <div class="mx-auto p-2" style="width:600px;">
      <h1 class="text-2xl text-center font-bold mb-3">점수가 반영되었습니다. <br> 덧붙여 영화의 소감을 남기실 수 있습니다.</h1>

      <form class="bg-yellow-400 rounded-md" @submit.prevent="onSubmit">
        <label for="title" class="mx-4 font-bold text-xl">제목</label>        
        <input type="text" id="title" name="title" class="w-96 m-5 bg-yellow-300 rounded-xl p-2" required>
        <br>
        <label for="content" class="m-5 font-bold text-xl">감상</label>
        <br>
        <textarea name="content"  id="content"  class="bg-yellow-300 rounded-xl p-2 my-2 ml-10" cols="60" rows="10" required></textarea>

        <div class="py-2 flex justify-around">
          <button class="rounded-lg bg-yellow-200 my-5 p-3 px-10 font-bold">감상 제출</button>
          <button class="rounded-lg bg-yellow-200 my-5 p-3 px-10 font-bold"><router-link to="home">그만 두기</router-link></button>
        </div>
      </form>
    </div>


  </div>
</template>

<script>
import {updateReview} from '@/api/index.js'
import ReviewMovieCard from '@/components/review/ReviewMovieCard.vue'
export default {
name: 'ReviewScoreView',
data(){
  return {
    movieId: this.$route.params.movieId,
  }
},
components: {
  ReviewMovieCard,
},
methods: {
  async onSubmit(e){
    const chk = this.validationCheck(e.target)
    
    if (chk) {
      const data = new FormData()      
      data.append('title', chk[0])
      data.append('content', chk[1])

    try {
      const res = updateReview(this.movieId, data)
      console.log(res) // 제대로 반환되서 promise 객체 반환함
      this.$router.push({name:'home'})
    } catch (error) {
      console.error(error)
    }
    }


  },

  validationCheck(form){
    const inputValueList = [form.title.value, form.content.value]
    
    for (const i of inputValueList) {
      if (!i) {
        alert('내용을 모두 작성해 주세요')
        return false
      }
    }
    return inputValueList
}

},
// route를 타고 View가 렌더링 될 때 API와 통신해서 영화 정보를 가지고 옴



}
</script>

<style scoped>
textarea {
 
  resize: none;
}


</style>