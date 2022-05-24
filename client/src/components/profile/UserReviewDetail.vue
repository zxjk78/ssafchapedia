<template>
  <div v-if="reviewInfo">
    <div class="grid grid-cols-3">
      <div class="poster-box mx-auto text-xl w-80">
        <img :src="poster_path" alt="포스터" class="w-80">
        <div class="">
          <p class="truncate ...">
            {{reviewInfo.movie.title}}
          </p>
          <div class="flex justify-between">
            <div>{{reviewInfo.movie.release_date}}</div>
          <div>⭐{{reviewInfo.movie.vote_average}}</div>
          </div>
        </div>
      </div>
      <div class="score-box flex flex-col justify-center items-center">
        <ScoreChart
        v-if="this.scores"
        :sscores="this.scores"
        class="w-96"
        />
        <div class="mt-5 text-bold text-xl">
        {{username}}님의 다각도 평가점수
        </div>
        <div class="mt-3">
          <span class="p-2">{{scoreEmoji}}</span>{{scoreSum}} / 15
        </div>
      </div>
      <div class="review-box flex justify-center items-center">
        <div v-if="reviewInfo.content">
          <div>{{reviewInfo.title}}</div>
          <div>{{reviewInfo.content}}</div>
        </div>
        <div v-else class="">
          작성한 상세 리뷰가 없습니다.
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import {fetchUserReviewList} from '@/api/index.js'
import ScoreChart from '@/components/common/ScoreChart.vue'
export default {
name: 'UserReviewDetail',
data(){
  return {
    username: this.$route.params.username,
    reviewInfo: null,
    poster_path: '',
    scores: null,
    scoreSum: 0,
    scoreEmoji: '',
  }
},
props:{

},
components: {
  ScoreChart,
},
async created(){
  const res = await fetchUserReviewList(this.username)
  this.reviewInfo = res.data
  this.poster_path = this.$store.state.tmdbImgUrl + this.reviewInfo.movie.poster_path
  this.scores = {
    acting: res.data.acting,
    art: res.data.art,
    directing: res.data.directing,
    music: res.data.music,
    story: res.data.story,
  }
  this.scoreSum = res.data.acting + res.data.art + res.data.directing + res.data.music + res.data.story
  this.scoreEmoji = this.scoreSum > 10 ? '👨‍👩‍👦' : (this.scoreSum > 5 ?  '💑' : '🤮')  
}
}
</script>

<style scoped>

</style>