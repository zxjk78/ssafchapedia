<template>
  <div>
    <div class="font-bold text-3xl text-red-600">영화 수정</div>
    <form @submit.prevent="onSubmit" class="border-2">
      제목
        <input type="text" name="title" class="border-2 bg-blue-300" v-model="review_title">
        <br>
        내용
      <textarea name="content" id="" class="bg-green-300" cols="30" rows="10" v-model="review_content">
      </textarea>

      <button class="bg-red-300">제출하기</button>
    </form>



  </div>
</template>

<script>
import {fetchReview} from '@/api/index.js'
import {updateReview} from '@/api/index.js'
export default {
name: 'ReviewUpdate',
data(){
  return {
    review_pk : '',
    review_title : '',
    review_content : '',
  }
},

components: {
},

methods: {
  async onSubmit(){
    const fo = {
      title: this.review_title,
      content: this.review_content
    }
    const res =  await updateReview(this.review_pk,fo)
    console.log(res)
    this.$router.push({name:'profile', params:{username:localStorage.getItem('username')}})
  }


  },
 



// route를 타고 View가 렌더링 될 때 API와 통신해서 영화 정보를 가지고 옴
async created(){

  try {

      const reviewId = this.$route.params.reviewId
      console.log('review아디',reviewId)
      const res = await fetchReview(reviewId)
      console.log(res.data)
      this.review_pk= res.data.pk
      this.review_title= res.data.title
      this.review_content= res.data.content
    } catch (error) {

      if (error.response.status == 404){
       console.log(1)
      }
    }


  


},



}
</script>

<style scoped>

  tr, td, th {    
    padding: 30px;
    text-align:center;
  }
  td > input[type=radio] {
    text-align: center;
  }
</style>