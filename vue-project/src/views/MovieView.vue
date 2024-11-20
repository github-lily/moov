<template>
  <div>
    <h1>Main Movie Page</h1>
    <MovieList
      v-for="movie in store.movies"
      :key="movie.id"
      :movie="movie"
     /> 
    </div>
    
    <hr>
    <RouterView />
</template>

<script setup>
import { onMounted } from 'vue'
import MovieList from '@/components/movie/MovieList.vue';
import { useMovieStore } from '@/stores/movie'

const store = useMovieStore()

onMounted(() => {
  // mount 되기전에 store에 있는 전체 게시글 요청 함수를 호출
  console.log('before getmovies')
  
  store.getMovies()

  console.log('end of getmovies')

  console.log(store.movies)
})
</script>

<style>

</style>
