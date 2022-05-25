import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

const SERVER = 'http://127.0.0.1:8000/'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    //TMDB 이미지 URL 여기에 profile_path나 poster_path 붙여넣어서 사용
    tmdbImgUrl:'https://image.tmdb.org/t/p/original/',
    // token 기반 인증에 사용
    authToken: localStorage.getItem('authToken') || '',
    username: '',
    // 키워드 검색에 사용되는 변수
    searchKeyword : '',
    searchMovieCnt: 0,
    searchActorCnt: 0,
    //영화 리스트 받아오기
    movies:[],
    movieList:[],
    movieTitles:[],
    reviews:[],
    rootDiv: null,
    // 로그인, 회원가입폼 modal에 사용되는 변수
    loginModal: false,
    signupModal: false,
    

  },
  // getters에서 state에 있는 변수들을 조회하고, component들의 computed에서는 getters의 함수만을 조회해서 사용하는 방식으로
  getters: {
    isLoggedIn(state){
      return state.authToken ? true : false
    },

    //영화 리스트
    movie:function(){
      return this.state.movies.map(a=>a.movieList)
    },

    movieTitles(state){
      return state.movieTitles
    },

    reviews(state){
      return state.reviews
    },
    //영화, 배우 검색 키워드
    search_keyword(state){
      return state.searchKeyword
    },
    //영화, 배우 검색후 결과 키워드
    search_result_exist(state){
      if (state.searchMovieCnt || state.searchActorCnt ){
        return true 
      } else {
        return false
      }
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
      localStorage.setItem('authToken', token)
    },
    SET_USERNAME(state, username){
      state.username = username
      localStorage.setItem('username', username)

    },
    SET_SEARCH_KEYWORD(state, keyword){
      state.searchKeyword = keyword
    },
    SET_SEARCH_MOVIE_CNT(state, cnt){
      state.searchMovieCnt = cnt
    },
    SET_SEARCH_ACTOR_CNT(state, cnt){
      state.searchActorCnt = cnt
    },
    LOGOUT(state){
      // 1. DB에서 해당 authToken 삭제
      // 2. localstorage에서 해당 authToken 삭제
      localStorage.setItem('authToken', '')
      localStorage.setItem('username', '')
      // 3. vuex state 에서 해당 authToken 삭제
      state.authToken = ''
    },
    
    //영화리스트
    GET_MOVIES(state, res) {
      state.movies = res
      //영화 추천 알고리즘에 적용할 필터
      // for (let index = 0; index < data.length; index++){
      //   if (data[index].popularity !=null){
      //     if (data[index].popularity.slice(-2, )=='만명' && data[index].popularity.slice(0,-2) > 10){
      //       state.recommend.push(data[index])
      //     }
      //     else if (data[index].reviews){
      //       state.recommend.push(data[index])
      //     }
      //   }
      // }
    },
    GET_MOVIE_TITLES(state, res) {
      const tmp = []
      for (var value of res){
        const tmp1 = {
          name:value.title,
          value:value.title
        }
        tmp.push(tmp1)
      }

      state.movieTitles = tmp
    },
    GET_REVIEWS(state,res){
      state.reviews = res
    }
  },
  actions: {

    getMovies({commit}) {
      axios.get({
        method: 'GET',
        url: `${SERVER}api/v1/movies/`,
      })
      .then(res => {
        commit('GET_MOVIES', res.data)
      })
      .catch(err => console.log(err))
    },
    getReviews({commit},token){
      axios({
        method: 'GET',
        url: `${SERVER}api/v1/reviews/`,
        headers: token,
      })
      .then(res => {
        commit('GET_REVIEWS', res.data)
      })
      .catch(err => console.log(err))
    }
  },
  modules: {
  }
})
