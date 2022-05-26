<template>
  <div>

    <div class="flex bg-yellow-100">
      <img :src="'https://image.tmdb.org/t/p/w200/'+ MovieInfo.poster_path" class="w-50" alt="">
      <div>
        <div>
          <h1 class="text-3xl font-bold">{{MovieInfo.title}} ({{Dateyear[0]}})</h1>
          <h2 class="text-2xl text-gray-500 font-bold">{{MovieInfo.release_date}}</h2>
          <h2 class="text-2xl font-bold">⭐{{MovieInfo.vote_average}}점</h2>
          <h2 class="text-2xl font-bold">⭐개요</h2>
          <h3 class="text-xl text-gray-500 font-bold">{{MovieInfo.overview}}</h3>

          <div class="w-1/4 mx-auto font-bold">
          <!-- <ScoreChart2
          :sscores="ReviewInfo.scores"
          :chartId="ReviewInfo.id"
          /> -->
          <ScoreChart2
          />
          </div>
          
        </div>
        <!-- <div>작품 개수: {{movieCnt}}개</div> -->
      </div>
    </div>

    <!-- <h1 class="text-2xl font-bold">
      대표
    </h1> -->
   
    <!-- <h1 class="text-2xl font-bold">전체</h1>        -->
    
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
// import ScoreChart2 from '@/components/common/ScoreChart2'

// import MovieCardList from '@/components/home/MovieCardList'
export default {
  name: 'MovieDetailView',
  data(){
    return {
      MovieId:this.$route.params.movieId,

      MovieInfo: '',
      movieCnt: '',
      ReviewInfo:'',
      
    }
  },
  components: {
    MovieDetail,
    // ScoreChart2,
  },
  async created(){
    console.log(this.MovieId)
    const movie = await fetchMovie(this.MovieId)
    console.log(movie)
    console.log('영화상세페이지뷰')
    this.MovieInfo = movie.data
    this.movieCnt= movie.data.title.length

    const DateYear = this.MovieInfo.release_date.split('-')
    this.Dateyear = DateYear

    const review = await fetchReviewGet(this.MovieId)
    this.reviewInfo = review.data
    console.log(this.reviewInfo)
  },
  computed:{
    movieInfo(){
    const tmp = this.reviewInfo.acting + this.reviewInfo.art + this.reviewInfo.directing + this.reviewInfo.music + this.reviewInfo.story
    return {
      poster_path: this.$store.state.tmdbImgUrl  +  this.reviewInfo.movie.poster_path,
      release_date: this.reviewInfo.movie.release_date.slice(0, 4),
      scores: {
              acting: this.reviewInfo.acting,
              art: this.reviewInfo.art,
              directing: this.reviewInfo.directing,
              music: this.reviewInfo.music,
              story: this.reviewInfo.story,
            },
      scoreSum: tmp,
      scoreEmoji: tmp > 7 ? '👨‍👩‍👦' : (tmp > 4 ?  '💑' : '🤮'),
    }
  },
  }
}
</script>

<style scoped>

</style>