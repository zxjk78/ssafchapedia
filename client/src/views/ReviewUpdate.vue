<template>
  <div>
    <div class="font-bold text-3xl text-red-600">영화 수정</div>
    <form @submit.prevent="onSubmit" class="border-2">
      <div class="flex">

      
      
      
      <div class="flex-col">
        
      제목
        <input type="text" name="title" class="border-2 bg-blue-300" v-model="review_title">
        <br>
        내용
      <textarea name="content" id="" class="bg-green-300" cols="30" rows="10" v-model="review_content">
      </textarea>
      </div>
      
      <div class="ml-20">
        <div>
          <h1>연출</h1>
        1 <input type="radio" name="directing" value="1" v-model="review_directing">
        2 <input type="radio" name="directing" value="2" v-model="review_directing">
        3 <input type="radio" name="directing" value="3" v-model="review_directing">

        </div>
        <div>
          <h1>음악</h1>
        1 <input type="radio" name="music" value="1" v-model="review_music">
        2 <input type="radio" name="music" value="2" v-model="review_music">
        3 <input type="radio" name="music" value="3" v-model="review_music">

        </div>
        <div>
          <h1>스토리</h1>
        1 <input type="radio" name="story" value="1" v-model="review_story">
        2 <input type="radio" name="story" value="2" v-model="review_story">
        3 <input type="radio" name="story" value="3" v-model="review_story">

        </div>
        <div>
          <h1>연기력</h1>
        1 <input type="radio" name="acting" value="1" v-model="review_acting">
        2 <input type="radio" name="acting" value="2" v-model="review_acting">
        3 <input type="radio" name="acting" value="3" v-model="review_acting">

        </div>
        <div>
          <h1>미술</h1>
        1 <input type="radio" name="art" value="1" v-model="review_art">
        2 <input type="radio" name="art" value="2" v-model="review_art">
        3 <input type="radio" name="art" value="3" v-model="review_art">

        </div>
      </div>
      
      
      </div>




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
    review_acting : '',
    review_story : '',
    review_art : '',
    review_directing : '',
    review_music : '',
  }
},

components: {
},

methods: {
  async onSubmit(){
    const fo = {
      title: this.review_title,
      content: this.review_content,
      directing:this.review_directing,
      music:this.review_music,
      story:this.review_story,
      art:this.review_art,
      acting:this.review_acting,
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