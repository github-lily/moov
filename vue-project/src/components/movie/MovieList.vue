<template>
  <div class="movie-grid">
      <MovieListItem 
      v-for="movie in props.movies"
        :key="movie.id"
        :movie="movie"
      />
  </div>
</template>

<script setup>
import MovieListItem from '@/components/movie/MovieListItem.vue'
import { useMovieStore } from '@/stores/movie';
import { defineProps } from 'vue';

const store = useMovieStore()


const props = defineProps({
  movies: {
    type: Array,
    required: true,
  }
})


</script>


<style>
.movie-grid {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: start;
  flex-wrap: wrap;
  gap: 20px;
  padding: 20px;
}
.movie-grid .movie-card {
  width: calc((100% - 40px) / 3);;
  min-width: 300px;
}

@media screen and (max-width: 999px) {
  .movie-grid .movie-card {
    width: calc((100% - 20px) / 2);
  }
}

@media screen and (max-width: 649px) {
  .movie-grid .movie-card {
    width: 100%;
  }
}
</style>