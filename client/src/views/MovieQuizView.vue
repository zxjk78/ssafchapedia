<template>
  <div>
    <h1 class="text-3xl">무비퀴즈 🎞</h1>
    <div class="container w-1/2 mx-auto my-16">
    <div class="flex justify-between text-2xl font-bold">
    <div >Stage <span id="QuizNum" class="">{{stageNum}}</span> / 9</div>
    <div>
    획득 점수: <span id="myScore">0</span> 
    </div>
    </div>
    <div v-if="stageNum < 4">
      <QuizEasy/>
    </div>
    <div v-else-if="4 <= stageNum < 7">
      <QuizMid/>
    </div>
    <div v-else>
      <QuizHard/>

    </div>

    </div>



  </div>
</template>

<script>
import {fetchMovieQuizInfo} from '@/api/index.js'
import QuizEasy from '@/components/quiz/QuizEasy.vue'
export default {
name: 'MovieQuizView',
data(){
  return {
    stageNum: 1
  }
},
components:{
  QuizEasy
},

async created(){
    const res = await fetchMovieQuizInfo()
    console.log(res)

    

},
mounted(){},

}


</script>

<style scoped>

</style>