import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    authToken: JSON.parse(localStorage.getItem('authToken')) || '',
    
    // 키워드 검색에 사용되는 변수
    movieSearchList: [],
    peopleSearchList: [],

    // 로그인, 회원가입폼 modal에 사용되는 변수
    loginModal: false,
    signupModal: false,


  },
  getters: {
    isLoggedIn(state){
      return state.authToken ? true : false
    },
  },
  mutations: {
    TOGGLE_LOGIN_MODAL(state){      
      state.loginModal = !state.loginModal
    },
    TOGGLE_SIGNUP_MODAL(state){      
      state.signupModal = !state.signupModal
    },
    SET_AUTH_TOKEN(state, token){
      state.authToken = token
      //localStorage는 String밖에 저장하지 못하므로, 만약 객체 등을 저장하려면 JSON으로 문자열로 변환해서 저장 필요
      localStorage.setItem('authToken', JSON.stringify(token))
    },
    SET_MOVIE_SEARCH_LIST(state, list){
      state.movieSearchList = list
    },
    SET_PEOPLE_SEARCH_LIST(state, list){
      state.movieSearchList = list
    },
  },
  actions: {
    async keywordSearch(context, keyword){
      if (!keyword){
        context.commit('SET_MOVIE_SEARCH_LIST', [])
        context.commit('SET_PEOPLE_SEARCH_LIST', [])
        return
      } 
      
      const TMDB_API_KEY = 'd5207cc845d8fba31db1ee25f04e5084'  
      
      const api_url = `https://api.themoviedb.org/3/search/movie?api_key=${TMDB_API_KEY}&language=ko-KR&page=1&include_adult=false&query=${keyword}`
      const res = await axios.get(api_url)
      
      context.commit('SET_MOVIE_SEARCH_LIST', res.data.results)
      // store 쪽에서 router를 통해 이동하려면, router 를 import 해야 한다.
      // NavigationDuplicated Error가 났는데, 같은 페이지로 router.push를 시도할 경우 나는 에러, 같은 path가 아닐 때만 이동하도록
      if (document.location.pathname != '/search') {
        router.push({name: 'search'}).catch(err=>{
          if (err.name === 'NavigationDuplicated'){
            return
          }
        })
      } 

    }
  },
  modules: {
  }
})
