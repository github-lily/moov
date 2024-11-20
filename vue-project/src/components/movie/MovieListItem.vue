<template>
  <div>
    <h3>Movie List</h3>
      <p>제목 : {{ movie.title }}</p>
      <img :src="poster" alt="영화포스터" style="height:300px">
      <p>개요 : {{ movie.overview }}</p>
      <p>장르 : {{ movie.genre }}</p>
      <p>개봉일 : {{ movie.release_date }}</p>
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

</style>
