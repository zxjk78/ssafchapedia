<template>
  <div>
    <ReviewMovieCard
    :movieId="movieId"/>


    <div class="mx-auto p-2" style="width:700px;">
      <form class="bg-yellow-400" @submit.prevent="onSubmit">
        <table class="table-fixed mx-auto">
          <thead>
            <tr class="text-lg">
              <th>점수 평가</th>
              <th>💔그저 그래요..</th>
              <th>💛평범해요.</th>
              <th>💚굉장해요!</th>
            </tr>
          </thead>
          <tbody>
            <tr class="bg-yellow-300">
              <td class="text-lg font-bold">감독 연출</td>
              <td> <input type="radio" name="directing" value="1"></td>
              <td> <input type="radio" name="directing" value="2"></td>
              <td> <input type="radio" name="directing" value="3"></td>
              </tr>
              <tr>
                <td class="text-lg">OST</td>
                <td> <input type="radio" name="music" value="1"></td>
                <td> <input type="radio" name="music" value="2"></td>
                <td> <input type="radio" name="music" value="3"></td>
            </tr>
            <tr class="bg-yellow-300">
              <td class="text-lg font-bold">스토리</td>
              <td> <input type="radio" name="story" value="1"></td>
              <td> <input type="radio" name="story" value="2"></td>
              <td> <input type="radio" name="story" value="3"></td>
            </tr>
                <tr>
              <td class="text-lg font-bold">배우 연기</td>
              <td> <input type="radio" name="acting" value="1"></td>
              <td> <input type="radio" name="acting" value="2"></td>
              <td> <input type="radio" name="acting" value="3"></td>
            </tr>
            <tr class="bg-yellow-300">
              <td class="text-lg font-bold">영상미</td>
              <td> <input type="radio" name="art" value="1"></td>
              <td> <input type="radio" name="art" value="2"></td>
              <td> <input type="radio" name="art" value="3"></td>
            </tr>
          </tbody>
        </table>        

        <div class="py-2 flex justify-center">
          <button class="rounded-lg bg-yellow-200 my-5 p-3 px-10">점수 제출</button>
        </div>
      </form>
    </div>


  </div>
</template>

<script>
import {createReview} from '@/api/index.js'
import ReviewMovieCard from '@/components/review/ReviewMovieCard.vue'
export default {
name: 'ReviewScoreView',
data(){
  return {
    movieId: this.$route.params.movieId,

    reviewInfo: {
      directing: 0,
      OST: 0,
      acting: 0,
      story: 0,
      art: 0,
    },

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
      data.append('directing', chk[0])
      data.append('music', chk[1])
      data.append('acting', chk[2])
      data.append('story', chk[3])
      data.append('art', chk[4])
    try {
      const res = createReview(this.movieId, data)
      console.log(res) // 제대로 반환되서 promise 객체 반환함
      this.$router.push({name:'review_new_detail', params:{movieId:this.movieId}} )
    } catch (error) {
      console.error(error)
    }
    }


  },

  validationCheck(form){
    const inputValueList = [form.directing.value, form.music.value, form.acting.value, form.story.value, form.art.value]
    
    for (const i of inputValueList) {
      if (!i) {
        alert('점수를 모두 선정해 주세요')
        return false
      }
    }
    return inputValueList
},

},
// route를 타고 View가 렌더링 될 때 API와 통신해서 영화 정보를 가지고 옴



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