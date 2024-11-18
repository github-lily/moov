<template>
  <div>
    <h1>Movie Page</h1>
    <RouterLink :to="{ name: 'CreateView' }">Create</RouterLink>
    <MovieList />
  </div>
</template>

<script setup>
import MovieList from '@/components/MovieList.vue'
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'

const store = useCounterStore()

onMounted(() => {
  // mount 되기전에 store에 있는 전체 게시글 요청 함수를 호출
  store.getMovies()
})
</script>

<style>

</style>
