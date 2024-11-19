<template>
  <div>
    <h1>MOOV.</h1>
    <RouterLink :to="{ name: 'SignUpView' }">SingUp</RouterLink> |
    <RouterLink :to="{ name: 'LogInView' }">LogIn</RouterLink>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
</script>

<style scoped>

</style>