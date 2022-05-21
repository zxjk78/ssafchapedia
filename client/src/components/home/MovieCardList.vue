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

    <VueSlickCarousel v-bind="settings" class="mx-6">
      <MovieCard
      v-for="movie in 15"
      :key="movie.id"
      />


    </VueSlickCarousel>

    </div>
  </div>
</template>

<script>
  import VueSlickCarousel from 'vue-slick-carousel'
  import MovieCard from '@/components/common/MovieCard'
  import 'vue-slick-carousel/dist/vue-slick-carousel.css'

  import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'

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
      }
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