<template>
  <div class="container">
    <HeaderNav />

    <div class="movie-container">
      <div class="movie-poster">
        <img v-if="moviePoster" :src="moviePoster" alt="Movie Poster">
        <p v-else>Loading...</p>
      </div>

      <div class="movie-contents"></div>
    </div>

    <div class="comments-container">
      <p class="comment-title">Comments</p>
      <div class="comments-list">
        <div class="comments"></div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref, computed } from 'vue'
import { useMovieStore } from '@/stores/movie'
import { useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import HeaderNav from '@/components/common/HeaderNav.vue'

const store = useMovieStore()
const authStore = useAuthStore()
const route = useRoute()
const movie = ref(null)

const moviePoster = computed(() => {
  return movie.value && movie.value.poster_path
    ? `https://image.tmdb.org/t/p/w500/${movie.value.poster_path}`
    : null
})

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/movies/${route.params.id}/`,
    headers: {
      Authorization: `Token ${authStore.token}`
    }
  })
    .then((res) => {
      movie.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})
</script>

<style scoped>
.movie-container {
  height: 500px;
  width: 100%;
  /* background-color: white; */
  border: 1px solid white;
  border-radius: 50px;
  display: flex;
  justify-content: space-between;
  align-items: stretch;
}

.movie-poster {
  height: 100%;
  width: 50%;
  padding: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}

img {
  height: 100%;
}

.movie-contents {
  height: 100%;
  width: 50%;
  background-color: rgb(126, 126, 126);
}

/* comment */
.comment-title {
  margin: 20px 0;
  font-family: 'Krona One';
  font-size: 20px;
  color: white;
}

.comments-list {
  width: 100%;
  background-color: #7c7c7c;
  height: 100vh;
}
</style>
