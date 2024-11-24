<template>
  <div class="container">
    <HeaderNav />
    <h2 class="mt-4">"{{ $route.params.keyword }}" 검색 결과</h2>
    <div class="movie-grid">
      <div v-if="movieStore.movies.length" class="row">
        <!-- 영화 목록 표시 -->
        <div v-for="movie in movieStore.movies" :key="movie.id" class="col-md-3 mb-4">
          <div class="card">
            <img 
              :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" 
              class="card-img-top" 
              :alt="movie.title"
            >
            <div class="card-body">
              <h5 class="card-title">{{ movie.title }}</h5>
            </div>
          </div>
        </div>
      </div>
      <div v-else>
        <p>검색 결과가 없습니다.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie'
import HeaderNav from '@/components/common/HeaderNav.vue'

const movieStore = useMovieStore()
</script>

<style scoped>

</style>