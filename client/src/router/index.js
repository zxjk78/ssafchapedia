import Vue from 'vue'
import VueRouter from 'vue-router'

import HomeView from '@/views/HomeView'
import SignupView from '@/views/SignupView'
import LoginView from '@/views/LoginView'
import ProfileView from '@/views/ProfileView'
import SearchView from '@/views/SearchView'
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
    path: '/signup', //=> http://localhost:8080/signup
    name: 'signup',
    component: SignupView,
  },
  {
    path: '/login', //=> http://localhost:8080/login
    name: 'login',
    component: LoginView,
  },
  {
    // path: '/:username', //=> http://localhost:8080/:username
    path: '/profile', //=> http://localhost:8080/profile : 임시로 쓰는 url
    name: 'profile',
    component: ProfileView,
  },
  {
    path: '/search',  //=> http://localhost:8080/search
    name: 'search',
    component: SearchView,
  },
  // {
  //   path: '/accounts/naver/login/callback/',  //=> http://localhost:8080/accounts/naver/login/callback/
  //   name: 'login-naver',
  //   component: NaverLoginAccessView,
  // },
  // {
  //   path: '/accounts/google/login/callback/',  //=> http://localhost:8080/accounts/google/login/callback/
  //   name: 'login-google',
  //   component: GoogleLoginAccessView,
  // },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
