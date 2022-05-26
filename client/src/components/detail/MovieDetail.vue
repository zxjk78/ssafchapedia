<template v-if="arrType==1">
  <div>
  <!-- <template v-if="arrType==1"> -->

      <div class="popular-list row row-cols-1 row-cols-md-5 gy-3">
      <!-- <div class="text-2xl font-bold">{{movie['title']}}</div> -->
      <!-- <div class="text-gray-500 text-xl font-bold">⭐평점: {{movie['vote_average']}}</div> -->
      <!-- <div class="text-gray-500 text-xl font-bold">⭐장르: {{movie['genre_ids']}}</div> -->
      <div class="text-2xl font-bold bg-yellow-200">
         <router-link :to="{name:'review_new', params:{movieId:movie.pk}}">
           리뷰쓰기
          </router-link>
      </div>

      <div class="text-2xl font-bold">출연 배우진</div>
      <!-- <div class="text-gray-500 text-xl font-bold">⭐{{movie['overview']}}</div> -->
      <!-- <div class="text-gray-500 text-xl font-bold">⭐영화 개봉일: {{movie['release_date']}}</div> -->
      <div class="flex flex-wrap">
        <div class="text-gray-500 text-xl flex-grow" v-for="actor in actors" :key="actor.id">
          <router-link :to="{name:'actor_detail', params:{actorId:actor.id}}">
            <img :src="`https://image.tmdb.org/t/p/w500/${actor.profile_path}`" class="w-32" alt="">
          </router-link>
        {{actor.korean_name}}
      </div>
      </div>
      
      
      </div>
    </div>   

  <!-- </template> -->

</template>
  


<script>
// import {fetchMovie} from '@/api/index.js'
export default {
  name: 'MovieDetail',
  components: {
  },
  props: {
    movie: {
      type: Object,
      required: true
    },
    arrType: {
    type: Number,
    required: true,
  },

  },
  
  computed: {
    actors(){
      const tmp = this.movie.actors
      // console.log(tmp)
      return tmp
    },
    movie_actor(){
    const {korean_name,profile_path, movies } = this.movie['actors']
    // console.log(this.movie['actors'].length())
    const actor = {korean_name,profile_path,movies}
    actor.profile_path = `https://image.tmdb.org/t/p/w500/${actor.profile_path}`

    return actor
  },
  
  },
  async created() {
    // const movie_act = this.movie['actors']
    // movie_act.pk
    // console.log(movie_act.length)
    // const tmp = this.movie.actors
      // console.log(tmp)
  },
}
</script>

<style>

</style>
