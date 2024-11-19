<template>
  <div>
    <h3>Movie List</h3>
    <MovieListItem 
      v-for="movie in store.movies"
      :key="movie.id"
      :movie="movie"
    />
  </div>
</template>

<script setup>
import MovieListItem from '@/components/movie/MovieListItem.vue'
import { useMovieStore } from '@/stores/movie'

const store = useMovieStore
</script>
