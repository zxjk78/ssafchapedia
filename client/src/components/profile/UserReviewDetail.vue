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
        
        <ScoreChart2
        v-if="movieInfo.scores"
        :sscores="movieInfo.scores"
        :chartId="idx"
        class="w-96"
        />

        <div class="mt-5 text-bold text-xl">
        {{profile}}님의 다각도 평가점수
        </div>
        <div class="mt-3">
          <span class="p-2">{{movieInfo.scoreEmoji}}</span>{{movieInfo.scoreSum}} / 15
        </div>
      </div>
      <div class="review-box relative flex justify-center items-center">
        <div v-if="review.content" class="w-96">
          <div class="bg-green-400 text-xl p-2 rounded-t-xl font-bold">{{review.title}}</div>
          <div class="h-48 text-lg bg-yellow-200 p-2 rounded-b-xl text-gray-500">{{review.content}}</div>
        </div>
        <div v-else class="">
          작성한 상세 리뷰가 없습니다.
        </div>
        
        <div v-if="profile==username">
          <div class="absolute right-0 top-20">
            <button :id="'d'+ review.pk" class="p-2 rounded bg-red-300" @click="deleteReview">삭제</button>
            <button :id="'u'+review.pk" class="p-2 rounded bg-blue-300" @click="updateReview">수정</button>
          </div>
        </div>
        </div>
      </div>

    </div>
</template>

<script>
// import ScoreChart from '@/components/common/ScoreChart.vue'
import ScoreChart2 from '@/components/common/ScoreChart2.vue'
import {deleteReview} from '@/api/index.js'

export default {
name: 'UserReviewDetail',
data(){
  return {
    profile: this.$route.params.username,
    username: localStorage.getItem('username')
  }
},
methods:{
  async deleteReview(e){    
    let id = e.target.id
    id = id.slice(1, )

    try {
      await deleteReview(id)
      this.$router.go();
    } catch (error) {
      console.error(error)
    }

  },
  updateReview(e){    
    let id = e.target.id
    id = id.slice(1, )
    
    console.log(id)
    this.$router.push({name:'review_update', params:{reviewId:id}})

  },


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

mounted(){
  console.log(this.username)
  console.log(this.profile)
}
}
</script>

<style scoped>

</style>