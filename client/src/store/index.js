import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    loginModal: false,
    signupModal: false
  },
  getters: {
  },
  mutations: {
    TOGGLE_LOGIN_MODAL(state){
      
      state.loginModal = !state.loginModal
    },
    TOGGLE_SIGNUP_MODAL(state){
      
      state.signupModal = !state.signupModal
    },
  },
  actions: {
  },
  modules: {
  }
})
