<template>
  <div>
    <!-- <RouterLink :to="{ name: 'SignUpView' }">SingUp</RouterLink> |
    <RouterLink :to="{ name: 'LogInView' }">LogIn</RouterLink> -->
    <!-- <HeaderNav /> -->
    <WelcomeView />
    <RouterView />

  </div>
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
import WelcomeView from './views/WelcomeView.vue';
// import HeaderNav from './components/common/HeaderNav.vue';

</script>

<style scoped>

</style>
