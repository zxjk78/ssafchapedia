<template>
  <div>

    <div class="flex bg-yellow-100">
      <img :src="'https://image.tmdb.org/t/p/original/'+ MovieInfo.poster_path" class="w-80" alt="">
      <div>
        <div>
          <h1 class="text-3xl font-bold">{{MovieInfo.title}} ({{Dateyear[0]}})</h1>
          <h2 class="text-2xl text-gray-500 font-bold">{{MovieInfo.release_date}}</h2>
          <h2 class="text-2xl font-bold">⭐{{MovieInfo.vote_average}}점</h2>
          <h2 class="text-2xl font-bold">⭐개요</h2>
          <h3 class="text-xl text-gray-500 font-bold">{{MovieInfo.overview}}</h3>

          <div class="w-2/3 mx-auto font-bold">
          <div v-if="sscores">
          <ScoreChart2
          :sscores="sscores"
          :chartId="scoreSum"
          />
          </div>
          <!-- <ScoreChart2
          /> -->
          </div>
          
        </div>

        <!-- <div>작품 개수: {{movieCnt}}개</div> -->
      </div>
    </div>

    
    <h2 class="text-2xl font-bold">
      <MovieDetail
      v-if="MovieInfo"
      :movie="MovieInfo"
      :arrType="1"
      />

    </h2>
  </div>

</template>

<script>
import {fetchMovie} from '@/api/index.js'
import {fetchReviewGet} from '@/api/index.js'

import MovieDetail from '@/components/detail/MovieDetail.vue'
import ScoreChart2 from '@/components/common/ScoreChart2'

// import MovieCardList from '@/components/home/MovieCardList'
export default {
  name: 'MovieDetailView',
  data(){
    return {
      MovieId:this.$route.params.movieId,
      sscores: '',
      MovieInfo: '',
      movieCnt: '',
      ReviewInfo:'',
      acting: 0,
      art: 0,
      directing: 0,
      music: 0,
      story: 0,
      i:0,
      average:'',

    }
  },
  components: {
    MovieDetail,
    ScoreChart2,
  },
  async created(){
    const movie = await fetchMovie(this.MovieId)
    this.MovieInfo = movie.data
    this.movieCnt= movie.data.title.length

    const DateYear = this.MovieInfo.release_date.split('-')
    this.Dateyear = DateYear

    const review = await fetchReviewGet(this.MovieId)
    this.ReviewInfo = review.data

    for(this.i=0;this.i<this.ReviewInfo.length;this.i++){
      this.acting += this.ReviewInfo[this.i].acting
      this.art += this.ReviewInfo[this.i].art
      this.directing += this.ReviewInfo[this.i].directing
      this.music += this.ReviewInfo[this.i].music
      this.story += this.ReviewInfo[this.i].story 
    }
    this.acting = this.acting / this.ReviewInfo.length
    this.art = this.art / this.ReviewInfo.length
    this.directing = this.directing / this.ReviewInfo.length
    this.music = this.music / this.ReviewInfo.length
    this.story = this.story / this.ReviewInfo.length
  
    const scores= {
              acting: this.acting,
              art: this.art,
              directing: this.directing,
              music: this.music,
              story: this.story,
            }
    this.scoreSum= 5
    this.sscores = scores
    // console.log(this.ReviewInfo)
  },
  computed:{
    movieScore(){
    // const tmp = this.acting + this.art + this.directing + this.music + this.story
    return {
      
    }

  },
  }
}
</script>

<style scoped>

</style>