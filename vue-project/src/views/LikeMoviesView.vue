<template>
  <div>
    <h2>좋아요한 영화 (전체 목록)</h2>
    <ul>
      <li v-for="movie in movies" :key="movie.id">
        {{ movie.title }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      movies: [],
    }
  },
  methods: {
    async fetchAllMovies() {
      const username = this.$store.state.auth.username // 사용자 이름
      const response = await axios.get(`/accounts/mypage/${username}/like_movies_list/`)
      this.movies = response.data
    },
  },
  mounted() {
    this.fetchAllMovies()
  },
}
</script>

<style scoped>
h1 {
  font-family: 'Krona One';
  text-align: center;
  color: white;
  font-size: 20px;
}
</style>