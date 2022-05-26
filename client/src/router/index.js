import Vue from 'vue'
import VueRouter from 'vue-router'

import HomeView from '@/views/HomeView'

import ProfileView from '@/views/ProfileView'
import SearchView from '@/views/SearchView'
import ReviewScoreView from '@/views/ReviewScoreView'
import ReviewUpdate from '@/views/ReviewUpdate'
import ActorDetailView from '@/views/ActorDetailView'
import MovieDetailView from '@/views/MovieDetailView'
import NotFoundView from '@/views/NotFoundView'
// import NaverLoginAccessView from '@/views/NaverLoginAccessView'
// import GoogleLoginAccessView from '@/views/GoogleLoginAccessView'

Vue.use(VueRouter)

const routes = [
  {
    path: '', //=> http://localhost:8080
    name: 'home',
    component: HomeView,

  },

  {
    path: '/:username/profile', //=> http://localhost:8080/:username/profile
    name: 'profile',
    component: ProfileView,
  },
  {
    path: '/search',  //=> http://localhost:8080/search
    name: 'search',
    component: SearchView,
  },
  
  //review
  {
    path: '/:movieId/review/new', //=> http://localhost:8080/:movieId/review/new
    name: 'review_new',
    component: ReviewScoreView,

  },
  {
    path: '/review/:reviewId/update', //=> http://localhost:8080/review/:reviewId/update
    name: 'review_update',
    component: ReviewUpdate,

  },



  //actor
  {
    path: '/actor/:actorId/detail', //=> http://localhost:8080/actor/:actorId/detail
    name: 'actor_detail',
    component: ActorDetailView,

  },
  //MovieDetail
  {
    path: '/:movieId/detail', //=> http://localhost:8080/:movieId/detail
    name: 'movie_detail',
    component: MovieDetailView,

  },

// 404 not found
{
  path: '/404', //=> 만들어놓은 404 vue
  name: 'not_found',
  
  component: NotFoundView,

},
{
  path: '*', //=> 어떤 경로와도 매칭이 되지 않은 경우 404 vue로 리다이트랙트해서 보여줌
  redirect: '/404',
  
},


]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
