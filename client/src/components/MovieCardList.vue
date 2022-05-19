<template>
  <div class="">
    <div class="btn-container flex justify-between w-full absolute top-48 z-50">
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
  import MovieCard from '@/components/MovieCard'
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
            infinite: true,
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

</style>