<template>
  <div>
    <h1>Detail</h1>
    <div v-if="movie">
      <p>제목 : {{ movie.title }}</p>
      <p>개요 : {{ movie.overview }}</p>
      <p>개봉일 : {{ movie.release_date }}</p> 

      <!-- <MovieComment /> -->
    </div>
    <div v-else>
      <p>Loading...</p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useMovieStore } from '@/stores/movie'
import { useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import MovieComment from '@/components/movie/MovieComment.vue'

const store = useMovieStore()
const authStore = useAuthStore()
const route = useRoute()
const movie = ref(null)



// DetailView가 마운트되기전에 DRF로 단일 게시글 조회를 요청 후 응답데이터를 저장
onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/movies/${route.params.id}/`,
    headers: {
      Authorization:`Token ${authStore.token}`
    }
  })
    .then((res) => {
      // console.log(res.data)
      movie.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})

</script>

<style>

</style>
