<template>
  <div class="flex justify-center items-center h-screen text-center">
    <div>

    <div class="text-8xl font-bold">
      404
    </div>
    
    <div class="text-5xl font-bold mt-5">
      Not Found  
    </div> 
    <div class="text-lg text-gray-600 font-bold mt-6">
      <div v-if="errorMsg">
        {{errorMsg}}
      </div>
      <div v-else>
        {{errorMsgDefault}}
      </div>
    </div>
    </div>
  </div>
</template>

<script>
export default {
name: 'NotFoundView',
data() {
  return {
    errorMsgDefault: '요청하신 URL은 유효하지 않습니다.',
    errorMsg: this.$route.params.errorMsg
  }
}
}
</script>

<style>

</style>