<template>
  <div class="w-2/3">
    <div class="text-2xl text-right">획득 가능 점수: <span class="score">{{qScore}}점</span></div>
    <div class="quiz-area">
    <h1 class=""> <span class="text-3xl text-green-500">Q. 영화 포스터의 일부가 주어집니다. 영화의 제목를 고르세요</span></h1>

    <div>
      <img :src="posterUrl" alt="" class="w-60">

    </div>

    </div>
    <div class="ans-area">
      <table>
        <tr>
          <td class="ans a1">{{answer1}}</td>
          <td class="ans a2">{{answer2}}</td>
        </tr>
        <tr>
          <td class="ans a3">{{answer3}}</td>
          <td class="ans a4">{{answer4}}</td>
        </tr>

      </table>

    </div>


  </div>
</template>

<script>
export default {
name: 'QuizEasy',
data(){
  return {
    posterUrl: '',
    answer1:'',
    answer2:'',
    answer3:'',
    answer4:'',
    idx:0,
    question_original: '123132342342',
  }
},
methods:{

  
},
props:{
  quizNum:{
    type: Number,
  }
},
computed:{
  
},
mounted(){  
  const qInfo = this.$store.state.quizInfo[this.quizNum]
  this.poster_url = this.$store.state.tmdbImgUrl + qInfo.poster_url
  this.answer1 = qInfo.answer1
  this.answer2 = qInfo.answer1
  this.answer3 = qInfo.answer1
  this.answer4 = qInfo.answer1

  document.querySelectorAll('.ans').forEach(element => {
    element.addEventListener('click', (e)=>{
      console.log(e.target)
    })
  });

},
}

</script>

<style>

</style>