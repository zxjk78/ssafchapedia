<template>
<!-- <a href="" class="outer"> -->
    <router-link :to="{name:'movie_detail', params:{movieId:movie.pk}}" class="outer">

  <div class="text-center mx-2 screen">
    <div class="poster">
      
    <img :src="poster_path" alt="" class="mx-auto">

    </div>
    
    <div class="bottom">
      <div :id="'movie-title'+movie.pk" class="font-bold">{{movie.title}}</div>
      <div class="text-yellow-400 font-bold mb-3">⭐{{movie.vote_average}}</div>
      
    <!-- <router-link :to="{name:'movie_detail', params:{movieId:movie.pk}}"> -->
    <!-- </router-link> -->
    </div>
  </div>

    </router-link>
</template>

<script>
export default {
  name: 'ActMovMaster',
  data(){
    return {}
  },
  props: {
    movie: {
      type:Object,
      required: true,
    }
  },
  methods:{
    setMovieTitleFontSize(){
      const movieTitle = this.$el.querySelector('#movie-title'+this.movie.pk)
      // console.log(movieTitle)
      const movieTitleLength = this.movie.title.length
      // console.log(movieTitleLength)
      if (movieTitleLength > 15){
        movieTitle.classList.add('text-3xl')  
      }
      else if (movieTitleLength > 11){
        movieTitle.classList.add('text-4xl')
      } 
      else if (movieTitleLength > 9){
        movieTitle.classList.add('text-5xl')
      } else{
        movieTitle.classList.add('text-6xl')
      }
    },


  },
  computed:{
  poster_path(){
    const tmp = this.$store.state.tmdbImgUrl + this.movie.poster_path
    return tmp
  },
  },
  mounted(){


      this.setMovieTitleFontSize()
  
  },
}
</script>

<style scoped>
.poster{
  max-height: 730px;
  overflow: hidden;
}

.poster img{
  
  max-height: initial;
}


.screen {position:relative;overflow:hidden;}

.screen .bottom {position:absolute;top:150%;left:0px; right:0px; margin-left:0px; margin-right:0px;z-index:2;color:#fff;font-size:50px;
transition:all .35s;
}
.screen::after {content:'';display:block;position:absolute;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.5);z-index:1;opacity:0;
transition:all .35s;
}
.bottom button{
  font-size:20px;
}
.outer:hover .bottom {top:65%;}
.outer:hover .screen::after {opacity:1;}
</style>