<template>
  <div class="">

    <div class="w-3/4 mx-auto">
    
    <div class="flex justify-between mx-auto mb-10 border-b-2	">
      <div class="text-3xl font-bold">{{username}} 님이 리뷰를 남긴 작품들🎥</div>

    </div>
    <div v-if="reviews">
      <UserReviewDetail
      v-for="(review, index) in reviews"
      :key="index"
      :idx="index"
      :review="review"
      :user="username"
      /> 

    </div>
    </div>
      


  </div>
</template>

<script>
import UserReviewDetail from '@/components/profile/UserReviewDetail.vue'
import {fetchUserReviewList} from '@/api/index.js'

export default {
  name:'ProfileView',
  data(){return {
    username:this.$route.params.username,
    reviews: null,
    page: 1,
    maxPage: '',
  }},
  components:{
    UserReviewDetail,
  },
  computed:{

  },
  methods:{
    async onScroll(){
      // scrollTop: 스크롤바의 위에서부터의 수직 위치, clientHeight: 화면에 표시되는 해당 요소의 높이, scrollHeight 요소의 전체 높이
     const {scrollTop, clientHeight, scrollHeight } = document.documentElement;
      // console.log(scrollTop)
      if (scrollTop + clientHeight >= scrollHeight - 10) {
        if (this.page > this.maxPage) {
          return
          }
        const res = await fetchUserReviewList(this.username, this.page++)
        // console.log(res.data.results)
        this.reviews = this.reviews.concat( res.data.results)
        
      }

    }
  },
  async created(){
    try {
      const res = await fetchUserReviewList(this.username, this.page++)
      this.reviews = res.data.results
      this.maxPage = Math.ceil(res.data.count / this.reviews.length)
      
    } catch (error) {
      // console.error(error.response.data)

      if (error.response.status == 404){
        this.$router.push({name: 'not_found', params:{errorMsg: '해당 회원은 존재하지 않는 회원입니다.'}})
      }

    }
  },
  mounted(){
    //mounted에 
    window.addEventListener('scroll', this.onScroll)
  }
}
</script>

<style scoped>
.material-symbols-outlined {
  font-variation-settings:
  'FILL' 1,
  'wght' 400,
  'GRAD' 0,
  'opsz' 48
}
/* .my-picture{
  

}
my-picture > img{
  

} */
</style>