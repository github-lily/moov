<template>
  <div>
    <h1>Main Movie Page</h1>
    <RouterLink :to="{name:'tmdbPopular'}">인기 순위</RouterLink> |
    <RouterLink :to="{name:'tmdbTopRated'}">역대 순위</RouterLink>
    <hr>
    <!-- <RouterLink :to="{ name: 'CreateView' }">Create</RouterLink> -->
    <RouterView />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useMovieStore } from '@/stores/movie'
import { RouterLink } from 'vue-router'

const store = useMovieStore()

onMounted(() => {
  // mount 되기전에 store에 있는 전체 게시글 요청 함수를 호출
  store.getMovies()
})
</script>

<style>

</style>
