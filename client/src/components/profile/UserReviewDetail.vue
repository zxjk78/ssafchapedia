<template>
  <div v-if="review">
    <div class="grid grid-cols-3">
      <div class="poster-box mx-auto text-xl w-80">
        <router-link  :to="{name:'movie_detail', params:{movieId:review.movie.pk}}" >
          <img :src="movieInfo.poster_path" alt="포스터" class="w-80">
        </router-link>
        <div class="">
          <p class="truncate ...">
            {{review.movie.title}}
          </p>
          <div class="flex justify-between">
            <div>{{movieInfo.release_date}}년</div>
          <div>
            <div v-if="isUpcoming">🎞 개봉 예정</div>
            <div v-else>⭐{{review.movie.vote_average}}</div>
          </div>
          </div>
        </div>
      </div>
      <div class="score-box flex flex-col justify-center items-center">
        <!-- <ScoreChart
        v-if="movieInfo.scores"
        :sscores="movieInfo.scores"
        :chartId="idx"
        class="w-96"
        /> -->
        <ScoreChart2
        v-if="movieInfo.scores"
        :sscores="movieInfo.scores"
        :chartId="idx"
        class="w-96"
        />

        <div class="mt-5 text-bold text-xl">
        {{username}}님의 다각도 평가점수
        </div>
        <div class="mt-3">
          <span class="p-2">{{movieInfo.scoreEmoji}}</span>{{movieInfo.scoreSum}} / 15
        </div>
      </div>
      <div class="review-box flex justify-center items-center">
        <div v-if="review.content">
          <div>{{review.title}}</div>
          <div>{{review.content}}</div>
        </div>
        <div v-else class="">
          작성한 상세 리뷰가 없습니다.
        </div>
      </div>

    </div>
  </div>
</template>

<script>
// import ScoreChart from '@/components/common/ScoreChart.vue'
import ScoreChart2 from '@/components/common/ScoreChart2.vue'
export default {
name: 'UserReviewDetail',
data(){
  return {
    username: this.$route.params.username,

  }
},
props:{
  review:{
    type: Object,
    required: true,
  },
  idx: {
    type:Number,
    required:true
  },

},
components: {
  // ScoreChart,
  ScoreChart2,
},
computed: {

  movieInfo(){
    const tmp = this.review.acting + this.review.art + this.review.directing + this.review.music + this.review.story
    return {
      poster_path: this.$store.state.tmdbImgUrl  +  this.review.movie.poster_path,
      release_date: this.review.movie.release_date.slice(0, 4),
      scores: {
              acting: this.review.acting,
              art: this.review.art,
              directing: this.review.directing,
              music: this.review.music,
              story: this.review.story,
            },
      scoreSum: tmp,
      scoreEmoji: tmp > 7 ? '👨‍👩‍👦' : (tmp > 4 ?  '💑' : '🤮'),
    }
  },
  isUpcoming(){
    const release = new Date(this.review.movie.release_date)
    // console.log(release > Date.now())
    
    if (release > Date.now()) {return true} 
    else {return false}
  }



},


}
</script>

<style scoped>

</style>