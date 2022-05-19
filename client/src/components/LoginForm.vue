<template>    
  <div>

<div v-if="toggleModal" id="back" class="w-screen h-screen fixed inset-0 bg-black flex justify-center items-center" @click="toggleLoginModal">

<!-- Main modal -->
<div id="authentication-modal" tabindex="-1" class="z-50">
    <div class="relative p-4 w-full max-w-md h-full md:h-auto">
        <!-- Modal content -->
        <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
  
            <div class="py-6 px-6 lg:px-8">
                <h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">로그인</h3>
                <form class="space-y-6" action="#">
                    <div>
                        <input type="text" name="text" id="text" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" placeholder="아이디" required>
                    </div>
                    <div>
                        <input type="password" name="password" id="password" placeholder="비밀번호" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" required>
                    </div>
                    <div class="flex justify-between">

                        <a href="#" class="text-sm text-blue-700 hover:underline dark:text-blue-500">비밀번호를 잊으셨나요?</a>
                    </div>
                    <button type="submit" class="w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">로그인</button>
                    <div class="text-sm font-medium text-gray-500 dark:text-gray-300">
                        가입하지 않으셨나요? <a href="#" class="text-blue-700 hover:underline dark:text-blue-500">가입하기</a>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div> 
</div>
</div>

</template>

<script>
export default {
name: 'LoginForm',
data(){ 
  return {
  } 
},
props: {

},
methods: {
  toggleLoginModal(){
    this.$store.commit('toggleLoginModal')
  }
},
computed: {
  toggleModal(){
    return this.$store.state.loginModalToggle
  }
},
}
</script>

<style>
#back {
  background: rgba(0, 0, 0, 0.56)
}

</style>