<template>
  <div>

    <div class="flex items-center min-h-screen bg-gray-50">
      <div
        class="flex-1 h-full max-w-4xl mx-auto bg-white rounded-lg shadow-xl"
      >
        <div class="flex flex-col md:flex-row">
          <div class="h-32 md:h-auto md:w-1/2">
            <img
              class="object-cover w-4/5"
              :src="poster_path"
              alt="img"
            />
          </div>
          <div class="flex justify-center p-6 md:w-1/2">
            <div class="w-full relative">
              <h3 class="mb-4 text-xl font-bold text-cyan-700">영화 평가</h3>
              <h3 class="mb-2 text-sm text-gray-400 font-bold">영화를 평가해 주세요.</h3>
              <div class="flex flex-wrap mx-auto">
                <a
                  class="form-tab inline-flex items-center
                    justify-center
                    w-1/2
                    h-full
                    py-3
                    font-medium
                    leading-none
                    tracking-wider
                    text-cyan-700
                    bg-gray-100
                    border-b-2 border-indigo-500
                    rounded-t
                    sm:px-6 sm:w-auto sm:justify-start
                  "
                @click="showTab(0)">
                  STEP 1
                </a>
                <a
                  class="form-tab
                    inline-flex
                    items-center
                    justify-center
                    w-1/2
                    py-3
                    font-medium
                    leading-none
                    tracking-wider
                    border-b-2 border-gray-200
                    sm:px-6 sm:w-auto sm:justify-start
                    hover:text-gray-900
                  "
                @click="showTab(1)">
                  STEP 2
                </a>
                <a
                  class="form-tab
                    inline-flex
                    items-center
                    justify-center
                    w-1/2
                    py-3
                    font-medium
                    leading-none
                    tracking-wider
                    border-b-2 border-gray-200
                    sm:px-6 sm:w-auto sm:justify-start
                    hover:text-gray-900
                  "
                @click="showTab(2)">
                  STEP 3
                </a>
              </div>
            <form @submit="onSubmit">

              <div id="reviewStep1" class="step h-full">              
              <div class="mt-4 mb-4">
                <div class="block text-sm"> 
                <div class="grid grid-cols-4">
                  <div>영화 연출</div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label inline-block text-gray-800" for="inlineRadio1">1</label>
                    <input class="form-check-input form-check-input rounded-full h-4 w-4 border border-gray-300 bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain ml-2 cursor-pointer" type="radio" name="directing" value="1">
                  </div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label inline-block text-gray-800" for="inlineRadio2">2</label>
                    <input class="form-check-input form-check-input rounded-full h-4 w-4 border border-gray-300 bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain ml-2 cursor-pointer" type="radio" name="directing" value="2">
                  </div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label inline-block text-gray-800" for="inlineRadio3">3</label>
                    <input class="form-check-input form-check-input rounded-full h-4 w-4 border border-gray-300 bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain ml-2 cursor-pointer" type="radio" name="directing" value="3">
                  </div>
                </div>
                </div>
              </div>
              <div class="my-4">
                <div class="block text-sm"> 
                <div class="grid grid-cols-4">
                  <div>OST</div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label inline-block text-gray-800" for="inlineRadio1">1</label>
                    <input class="form-check-input form-check-input rounded-full h-4 w-4 border border-gray-300 bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain ml-2 cursor-pointer" type="radio" name="music"  value="1">
                  </div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label inline-block text-gray-800" for="inlineRadio2">2</label>
                    <input class="form-check-input form-check-input rounded-full h-4 w-4 border border-gray-300 bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain ml-2 cursor-pointer" type="radio" name="music"  value="2">
                  </div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label inline-block text-gray-800" for="inlineRadio3">3</label>
                    <input class="form-check-input form-check-input rounded-full h-4 w-4 border border-gray-300 bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain ml-2 cursor-pointer" type="radio" name="music"  value="3">
                  </div>
                </div>
                </div>
              </div>
              <div class="my-4">
                <div class="block text-sm"> 
                <div class="grid grid-cols-4">
                  <div>스토리</div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label inline-block text-gray-800" for="inlineRadio1">1</label>
                    <input class="form-check-input form-check-input rounded-full h-4 w-4 border border-gray-300 bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain ml-2 cursor-pointer" type="radio" name="story" value="1">
                  </div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label inline-block text-gray-800" for="inlineRadio2">2</label>
                    <input class="form-check-input form-check-input rounded-full h-4 w-4 border border-gray-300 bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain ml-2 cursor-pointer" type="radio" name="story" value="2">
                  </div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label inline-block text-gray-800" for="inlineRadio3">3</label>
                    <input class="form-check-input form-check-input rounded-full h-4 w-4 border border-gray-300 bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain ml-2 cursor-pointer" type="radio" name="story"  value="3">
                  </div>
                </div>
                </div>
              </div>
              </div>
              <div id="reviewStep2" class="step h-full">              
              <div class="mt-4 mb-4">
                <div class="block text-sm"> 
                <div class="grid grid-cols-4">
                  <div>배우 연기</div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label inline-block text-gray-800" for="inlineRadio1">1</label>
                    <input class="form-check-input form-check-input rounded-full h-4 w-4 border border-gray-300 bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain ml-2 cursor-pointer" type="radio" name="acting"  value="1">
                  </div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label inline-block text-gray-800" for="inlineRadio2">2</label>
                    <input class="form-check-input form-check-input rounded-full h-4 w-4 border border-gray-300 bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain ml-2 cursor-pointer" type="radio" name="acting"  value="2">
                  </div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label inline-block text-gray-800" for="inlineRadio3">3</label>
                    <input class="form-check-input form-check-input rounded-full h-4 w-4 border border-gray-300 bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain ml-2 cursor-pointer" type="radio" name="acting" value="3">
                  </div>
                </div>
                </div>
              </div>
              <div class="my-4">
                <div class="block text-sm"> 
                <div class="grid grid-cols-4">
                  <div>영상미</div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label inline-block text-gray-800" for="inlineRadio1">1</label>
                    <input class="form-check-input form-check-input rounded-full h-4 w-4 border border-gray-300 bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain ml-2 cursor-pointer" type="radio" name="art"  value="1">
                  </div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label inline-block text-gray-800" for="inlineRadio2">2</label>
                    <input class="form-check-input form-check-input rounded-full h-4 w-4 border border-gray-300 bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain ml-2 cursor-pointer" type="radio" name="art"  value="2">
                  </div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label inline-block text-gray-800" for="inlineRadio3">3</label>
                    <input class="form-check-input form-check-input rounded-full h-4 w-4 border border-gray-300 bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain ml-2 cursor-pointer" type="radio" name="art" value="3">
                  </div>
                </div>
                </div>
              </div>
              </div>
              <div id="reviewStep3" class="step">              
              <div class="mt-4 mb-4">
                <div class="block text-sm"> 
                <div class="">
                  <div class="form-check form-check-inline">
                    <label class="form-check-label inline-block text-gray-800" for="reviewTitle"></label>
                    <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="reviewTitle" type="text" name="title"  placeholder="제목">
                  </div>
                  
                  <div class="form-check form-check-inline">
                    <label class="form-check-label inline-block text-gray-800" for="reviewContent"></label>
                    <textarea class="" name="content" id="reviewContent" cols="55" rows="10" maxlength="400" style="resize:none; border:solid 1px gray"  ></textarea>
                  </div>
                </div>
                </div>
              </div>

              </div>

            </form>


              <div class="flex justify-end">
                <button id="nextBtn"
                  class="
                    px-6
                    py-2
                    mt-4
                    text-sm
                    font-medium
                    leading-5
                    text-center text-white
                    transition-colors
                    duration-150
                    bg-cyan-700
                    border border-transparent
                    rounded-lg
                    hover:bg-cyan-800
                    focus:outline-none
                    absolute bottom-5
                  "
                 @click="showTab(currentTab+1)">
                  다음
                </button>
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>



  </div>
</template>

<script>
import {reviewExist} from '@/api/index.js'
import {createReview} from '@/api/index.js'
import {fetchMovie} from '@/api/index.js'
export default {
name: 'ReviewScoreView',
data(){
  return {
    movieId: this.$route.params.movieId,
    currentTab: 0,
    MovieInfo: '',
    poster_path: '',
  }
},

components: {
},

methods: {
  // form data 제출 함수
  async onSubmit(form){
    const chk = this.validationCheck(form)
    
    if (chk) {
      const data = new FormData()      
      data.append('directing', chk[0])
      data.append('music', chk[1])
      data.append('acting', chk[2])
      data.append('story', chk[3])
      data.append('art', chk[4])
      data.append('title', chk[5])
      data.append('content', chk[6])
    try {
      createReview(this.movieId, data)
      
      this.$router.push({name:'movie_detail', params:{movieId:this.movieId}} )
    } catch (error) {
      console.error(error)
    }
    }


  },
  //tab 전환시마다 다른 form 부분을 display해주는 함수
  showTab(n){    
    const inputArr = document.querySelectorAll(".step")
    const reviewForm = document.querySelector('form')
    if (n >= inputArr.length) {
      this.onSubmit(reviewForm)
      return
    }
    
    const tabArr = document.querySelectorAll(".form-tab")
    tabArr[this.currentTab].classList.remove('bg-gray-100', 'text-cyan-700', 'border-cyan-700', 'rounded-t', 'font-bold')
    tabArr[this.currentTab].classList.add('border-gray-200')
    tabArr[n].classList.add('bg-gray-100', 'text-cyan-700', 'border-cyan-700',  'rounded-t', 'font-bold')


    const nextBtn = document.querySelector("#nextBtn")
    
    inputArr[this.currentTab].style.display="none"
    inputArr[n].style.display="block"
    this.currentTab = n

    if (n == inputArr.length - 1){
      nextBtn.innerHTML = "제출";
    } else{
      nextBtn.innerHTML = "다음";
    }
    
},

  //제출 시 점수에 한해서 다 입력했는지 검사
  validationCheck(form){
    const inputValueList = [form.directing.value, form.music.value, form.story.value, form.acting.value, form.art.value]
    for (const i of inputValueList) {
      if (!i) {
        alert('영화 점수는 모두 선택해 주세요')
        return false
      }
    }
    // 추가로 유효성 검사 필요없는거 집어넣고 전송
    const result = inputValueList.concat([form.title.value, form.content.value])
    
    return result
},

},
// route를 타고 View가 렌더링 될 때 API와 통신해서 영화 정보를 가지고 옴
async created(){

  try {

      // 1. 회원이 사전에 영화에 대한 리뷰를 작성하였으면, 리뷰 페이지로 그냥 redirect 시킨다.

      const isReviewExist = await reviewExist(this.movieId)
      console.log(isReviewExist)
      if (isReviewExist.data.result){
        alert('이미 리뷰를 작성하셨습니다.')
        return this.$router.push({name: 'profile', params:{username:localStorage.getItem('username')}})
      }
      // 2. 없으면 리뷰를 작성하도록 화면을 보여준다.
      const movie = await fetchMovie(this.movieId)
      this.MovieInfo = movie.data
      this.movieTitleLength= movie.data.title.length
      this.poster_path = this.$store.state.tmdbImgUrl + this.MovieInfo.poster_path
      
    } catch (error) {
      // console.error(error.response.data)

      if (error.response.status == 404){
        this.$router.push({name: 'not_found', params:{errorMsg: '찾으시는 영화는 존재하지 않습니다.'}})
      }
    }


  


},


// 마운팅 될 때 초기에 showTab으로 1번탭 활성화시킴
mounted(){
  const inputArr = document.querySelectorAll(".step")
  inputArr.forEach((ele)=>{
    ele.style.display='none'
  })
  this.showTab(0)

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