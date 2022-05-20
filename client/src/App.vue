<template>
  <div>
    <TheNavbar/>
    
    <router-view/>
  </div>
</template>

<script>
import TheNavbar from '@/components/common/TheNavbar.vue'
export default {
  name: 'App',
  components: {
    TheNavbar,
  },
  computed:{
    
  },
}
</script>

<style scoped>
</style>
