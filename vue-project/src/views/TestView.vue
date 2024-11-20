<template>
  <div> 
    <h1>Test Page</h1>
    <RouterLink :to="{name:'MovieView'}">Go Movies</RouterLink>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
import MovieView from './MovieView.vue';
</script>

<style scoped>
h1 {
  color: white;
}
</style>