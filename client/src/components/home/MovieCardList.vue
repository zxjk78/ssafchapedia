<template>
  <div class="">
    <div class="btn-container flex justify-between w-full absolute top-48 z-30">

      <button @click="slidePrev">
        <span class="material-symbols-outlined text-5xl text-slate-300">
        arrow_circle_left
        </span>

      </button>
      <button @click="slideNext">
        <span class="material-symbols-outlined text-5xl text-slate-300">
        arrow_circle_right
        </span>

      </button>

    </div>
    <div class="mx-6">

    <VueSlickCarousel v-if="MovieInfo" v-bind="settings" class="mx-6">
      <MovieCard
      v-for="(movie,idx) in movieCnt"
      :key="idx"
      :movie='movie'
      :idx='idx'
      />
      <MovieDetail
      v-if="MovieInfo.pk"
      :movies="MovieInfo.pk"
      :arrType="1"
      />

    </VueSlickCarousel>

    <!-- 테스트용 -->
    <!-- 안녕안녕: {{getMovie()}}  -->
    </div>
  </div>
</template>

<script>
  import VueSlickCarousel from 'vue-slick-carousel'
  import MovieCard from '@/components/common/MovieCard'
  import 'vue-slick-carousel/dist/vue-slick-carousel.css'

  import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
  import {fetchMovie} from '@/api/index.js'
  import {mapGetters} from 'vuex'
  export default {
    name: 'MyComponent',
    data(){
      return {
        settings: {
            dots: false,
            arrows: true,
            focusOnSelect: true,
            infinite: false,
            speed: 500,
            slidesToShow: 5,
            slidesToScroll: 5,
            
          },
        MovieId:this.$route.params.movieId,
        MovieInfo: '',
        movieCnt: ''
      }
    },
    components: { 
      VueSlickCarousel,
      MovieCard,
      },
    methods:{
        slideNext(){
          const nextBtn = document.querySelector('.slick-next')
          nextBtn.click()
        },
        slidePrev(){
          const prevBtn = document.querySelector('.slick-prev')
          prevBtn.click()
        },
        //영화
        setToken(){
          const token = localStorage.getItem('jwt')
          const config = {
          Authorization: `JWT ${token}`
        }
          return config
        },
        //
        // getMovie(){
        //   this.$axios.get('http://localhost:8080/api/v1/movies')
        //   .then(response=>{
        //     console.log('### response: ' + JSON.stringify(response))
        //   this.boardList = response.data
        //   })
        //   .catch(error => {
        //     console.log(error)
        //   })
        //   },
        },
    computed:{
      ...mapGetters({
        movies:'movies'
    })
    },
    // created(){
    //   this.$store.dispatch('getMovies',this.setToken())
    //   // this.$store.dispatch('getMovies')
    //   // this.getMovie()
    // },
    async created(){
    const movie = await fetchMovie(this.MovieId)
    this.MovieInfo = movie.data
    this.movieCnt= movie.data.title.length
  }
  }
</script>

<style scoped>
/* arrow가 스타일링 할 때 자잘한 오류가 많아서 display None으로 안보이게 하고 
내가 스타일링한 화살표 버튼을 클릭하면 arrow 에 click 이벤트를발생시킴 */
.slick-next::before .slick-prev::before .slick-next .slick-prev {
  display:none;
}
</style>