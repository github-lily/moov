<template>
  <div class="movie-list">
    <div class="card">      
      <MovieListItem 
      v-for="movie in store.movies"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script setup>
import MovieListItem from '@/components/movie/MovieListItem.vue'
import { useMovieStore } from '@/stores/movie';

const store = useMovieStore()


</script>


<style>
.movie-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.card {
  border: beige, 1px, solid;
  width: 200px;
  padding: 15px;
  
}
</style>