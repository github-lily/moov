<template>
  <div class="container">
    <HeaderNav/>
    <div class="movie-container">
      <div class="movie-poster"></div>
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
import { useMovieStore } from '@/stores/movie'
import { useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import MovieComment from '@/components/movie/MovieComment.vue'
import HeaderNav from '@/components/common/HeaderNav.vue'

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

const poster = `https://image.tmdb.org/t/p/w500/${movie.poster_path}`

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
