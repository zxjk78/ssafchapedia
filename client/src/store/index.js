import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    loginModalToggle: false
  },
  getters: {
  },
  mutations: {
    toggleLoginModal(state){
      
      state.loginModalToggle = !state.loginModalToggle
      console.log(state.loginModalToggle)
    }
  },
  actions: {
  },
  modules: {
  }
})
