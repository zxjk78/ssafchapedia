<template v-if="arrType==1">
  <div>
  <!-- <template v-if="arrType==1"> -->

      <div class="popular-list row row-cols-1 row-cols-md-5 gy-3">
      <div class="text-2xl font-bold">{{moviePK.title}}</div>
      <div class="text-gray-500 text-xl font-bold">⭐{{moviePK.vote_average}}</div>
    </div>
  <!-- </template> -->
    </div>
</template>
  


<script>
import {fetchMovie} from '@/api/index.js'
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
  data() {
    return {
      // dialog: false,
      // notifications: false,
      // sound: true,
      // widgets: false,
    }
  },
  computed: {
    
  },
  async created() {
    try {
    const movie = this.movie.pk
    const movieDetail = await fetchMovie(movie)
    this.moviePK = movieDetail.data
    console.log(this.moviePK)
  } catch (error) {
    console.error(error)
  }
  },
}
</script>

<style>

</style>
