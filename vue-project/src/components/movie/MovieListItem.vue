<template>
  <div class="movie-card">
    <img class="poster" :src="poster" alt="영화포스터" >
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

const props = defineProps({
  movie:Object
})
const poster = `https://image.tmdb.org/t/p/w500/${props.movie.poster_path}`

</script>

<style>
.movie-card {
  width: 100%;
  transform-origin: center;
  padding: 10px;
}

.poster {
  width: 90%;
  height: auto;
  display: block;
  border-radius: 20px;
  transition: transform 0.3s ease;
}

.poster:hover {
  transform: scale(1.05); 
}

</style>
