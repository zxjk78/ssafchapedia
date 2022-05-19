<template>
  <div>
    <div class="max-w-sm bg-white w-52 rounded-lg dark:bg-gray-800 dark:border-gray-700">
    <a href="#">
        <img class="rounded-t-lg" src="https://image.tmdb.org/t/p/w300/6DrHO1jr3qVrViUO6s6kFiAGM7.jpg" alt="" />
    </a>
    <div class="mt-1">
        <a href="#">
            <h5 class="text-lg font-bold tracking-tight text-gray-900 dark:text-white">범죄도시2</h5>
        </a>
        <div class="flex justify-between w-1/2 pr-2" >
          <div>년도</div>
          <div>&#183;</div>
          <div>나라</div>
        </div>
        
        <div class="flex justify-between text-sm text-slate-500" >
          <div>예매율 <span></span>%</div>
          <div>&#183;</div>
          <div>누적 관객 <span></span>만명</div>
        </div>


    </div>
</div>

  </div>
</template> 

<script>

export default {
name: 'MovieCard',
data(){ return {

} 
},
methods: {

},
computed: {},
components: {},
}
</script>

<style>

</style>