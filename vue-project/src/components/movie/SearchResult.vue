<template>
  <div>
    <HeaderNav />
    <div class="container">
      <h2 class="search-title">
        "{{ searchKeyword }}" 에 대한 검색 결과입니다.
      </h2>
      <MovieList 
        :movies="filteredMovies"
        v-if="filteredMovies.length > 0"
      />
      <p v-else class="no-results">
        검색 결과가 없습니다.
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRoute } from 'vue-router';
import { useMovieStore } from '@/stores/movie';
import HeaderNav from '../common/HeaderNav.vue';
import MovieList from './MovieList.vue';

const route = useRoute();
const movieStore = useMovieStore();
const searchKeyword = computed(() => route.params.keyword);

const filteredMovies = ref([]);

onMounted(async () => {
  // 모든 영화 데이터 가져오기
  await movieStore.getMovies();
  
  // 검색어로 영화 필터링
  const keyword = searchKeyword.value.toLowerCase(); //대소문자 무시
  filteredMovies.value = movieStore.movies.filter(movie => 
    movie.title.toLowerCase().includes(keyword)
  );
});
</script>

<style scoped>
.container {
  /* display: flex; */
  /* flex-direction: row; */
  justify-content: center;
  align-items: center;
  width: 100%;
}

.search-title {
  color: white;
  text-align: center;
  font-family: 'NoTo Sans Kr';
  font-size: 1.5em;
  padding: 20px;
  font-weight: lighter;

}

.no-results {
  color: white;
  text-align: center;
  font-size: 1em;
  font-family: 'NoTo Sans Kr';
  font-weight: lighter;

}
</style>