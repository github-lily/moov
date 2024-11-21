<template>
  <div class="container">
    <HeaderNav/>
    <div class="movie-container">
      <div class="movie-poster">
        <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="poster">
      </div>
      <div class="movie-contents"></div>
    </div>

    <p class="comment-title">Comments</p>
    <div class="comments-container">
      <div class="comments"></div>
    </div>
  </div>

</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import { useMovieStore } from '@/stores/movie'
import { useAuthStore } from '@/stores/auth'
import { useUserStore } from '@/stores/user'

import MovieComment from '@/components/movie/MovieComment.vue'
import HeaderNav from '@/components/common/HeaderNav.vue'

const store = useMovieStore()
const userStore = useUserStore()
const authStore = useAuthStore()
const route = useRoute()
const movie = ref(null)


// DetailView가 마운트되기전에 DRF로 단일 게시글 조회를 요청 후 응답데이터를 저장
onMounted(() => {
  store.getMovieDetail()
  userStore.getUser()
})


</script>

<style scoped>
.movie-container {
  height: 500px;
  width: 100%;
  background-color: white;
  display: flex;
  justify-content: space-between;
  align-items: stretch;
}

.movie-poster {
  height: 100%;
  width: 50%;
  background-color: rgb(180, 180, 180);
}

.movie-contents {
  height: 100%;
  width: 50%;
  background-color: rgb(126, 126, 126);
}


/* commnet */
.comment-title {
  margin: 20px 0;
  font-family: 'Krona One';
  font-size: 20px;
  color: white;
}
</style>
