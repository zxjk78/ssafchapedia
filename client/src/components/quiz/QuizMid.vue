<template>
  <div class="w-2/3">
    <div class="text-2xl text-right">획득 가능 점수: <span class="score">{{qScore}}점</span></div>
    <div class="quiz-area">
    <h1 class=""> <span class="text-3xl text-green-500">Q. 영화의 줄거리가 주어지는 동안, 영화 제목을 고르세요</span></h1>
    <span id="quizText" class="text-3xl">{{question}}</span> 
    </div>
    <div class="ans-area">
      <table>
        <tr>
          <td class="ans a1">{{answer1}}</td>
          <td class="ans a2">{{answer1}}</td>
        </tr>
        <tr>
          <td class="ans a3">{{answer1}}</td>
          <td class="ans a4">{{answer1}}</td>
        </tr>

      </table>

    </div>


  </div>
</template>

<script>
export default {
name: 'QuizMid',
data(){
  return {
    question: '',
    answer1:'',
    answer2:'',
    answer3:'',
    answer4:'',
    idx:0,
    question_original: '123132342342',
  }
},
methods:{
  typing(){
    if (this.idx < this.question_original.length){
      this.question= this.question.concat(this.question_original.charAt(this.idx))
      this.idx++

    } 
  }
  
},
props:{
  quizNum:{
    type: Number,
  }
},
computed:{
  qScore(){
    return this.question_original.length - this.idx
  } 
},
mounted(){
  setInterval(this.typing, 200)
  


}
}

</script>

<style>

</style>