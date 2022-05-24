<template>
  <div>
    <TheNavbar/>
    


    <router-view/>
  </div>
</template>

<script>
import {mapActions} from 'vuex'
import TheNavbar from '@/components/common/TheNavbar.vue'
export default {
  name: 'App',
  components: {
    TheNavbar,
  },
  methods: {
    getToken() {
      const token = localStorage.getItem('jwt')
      return token
    },
    setToken() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
  },
  computed:{
    ...mapActions([
      'checkMovies'
    ]),
  },
}
</script>

<style>
/* @import './assets/styles/moviecard.css'; */

/* *:not(html, body) {
  border: solid 1px black
} */

</style>
