import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    authToken:JSON.parse(localStorage.getItem('authToken')) || '',
    //userInfo: null,
  },
  getters: {
    isLoggedIn(state){
      return state.authToken ? true:false
    }
  },
  mutations: {
    setAuthToken(state,authToken){
      state.authToken = authToken
      localStorage.setItem('authToken',JSON.stringify(authToken))

      // const userInfo={
      //   username:'kang',
      //   password:'ruddms',
      // }
      // localStorage.setItem(
      //   'userInfo',
      //   JSON.stringify(userInfo)
      // )
      // JSON.parse(localStorage.getItem('userInfo'))
    },
    
  },
  actions: {
  },
  modules: {
  }
})
