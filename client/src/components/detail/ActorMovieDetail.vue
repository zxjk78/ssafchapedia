<template>
  <div>
    <template v-if="arrType==1">
    <div class="w-5/6 ml-10 grid grid-cols-3">

    <ActMovMaster
    v-for="movie in movies"
    :key="movie.id"
    :movie="movie"
    />    
          </div>

    </template>
    
    <template v-if="arrType==2">
      <div class="flex-col">
        <ActMovNormal
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
        />    
      </div>
    </template>

  </div>
</template>

<script>
import ActMovNormal from '@/components/detail/ActMovNormal.vue'
import ActMovMaster from '@/components/detail/ActMovMaster.vue'
export default {
name: 'ActorMovieDetail',
props: {
  arrType: {
    type: Number,
    required: true,
  },
  movies: {
    type: Array,
    required: true,
  },


},
components: {
  ActMovNormal,
  ActMovMaster,
},


}
</script>

<style>

</style>