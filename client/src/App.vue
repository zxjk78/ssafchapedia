<template>
  <div>
    <nav>
      <template v-if="isLoggedIn">

      <router-link to="/">Home</router-link> |
      </template>
      <template v-else>

      <router-link to="/login">Login</router-link> |
      <router-link to="/signup">Signup</router-link> |
      </template>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  computed:{
    isLoggedIn(){
      return this.$store.getters.isLoggedIn
    },
  },
}
</script>

<style scoped>
</style>