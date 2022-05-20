<template>
  <div>
      <div class="flex gap-2">
      <div class="bg-red-100">
        <div><img :src="movie_renew.poster_path" class="w-32" alt=""></div>
      </div>
      <div class="w-1/3 flex flex-col justify-start gap-y-4">
        <div class="font-bold text-2xl">{{movie_renew.title}}</div>
        <div class="flex gap-x-2">
          <div class="font-bold text-slate-500">{{movie.genre_ids}}, {{movie_renew.release_date}}년</div>
          <div class="">{{movie_renew.vote_average}}점</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
name:'MovieSearch',

props:{
  movie: {
    type:Object,
    required: true,
  }
},
computed: {
  movie_renew(){
    // 이부분 디스트럭쳐링 할당 하고 내가 고치고 싶은 부분만 고치기
    const {title, release_date, vote_average, poster_path} = this.movie

    const movie2 = {
      title, release_date, vote_average, poster_path
    }
    movie2.poster_path = `https://image.tmdb.org/t/p/w500/${movie2.poster_path}`
    movie2.release_date = movie2.release_date.slice(0,4)
    return movie2
  }
}
}
</script>

<style scoped>

</style>