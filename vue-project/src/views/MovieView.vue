<template>
  <div class="container">
    <HeaderNav />
    <div class="intro">
      <div class="intro-left">
        <p class="introtext">Learn English,<br> Enjoy Movies,<br> Love the Journey!</p>
        <p class="introtext2">
          At Moov. we help you learn English through carefully selected movies <br> that match your proficiency level. <br> Start you journey toda
        </p>
      </div>
      <div class="intro-right">
        <div class="mainmovie"></div>
        <button class="test" @click="goToTest">TEST &#9654</button>
      </div>
    </div>
    <h3>Today's recommendation</h3>
    <div class="movielist">
      <div>
        <label for="genre-select">Select Genre: </label>
        <select id="genre-select" v-model="selectedGenre">
          <option value="">All Genre</option>
          <option v-for="genre in genres" :value="genre">{{ genre }}</option>
        </select>
      </div>
      <!-- 영화 12개만 출력 -->
      <MovieList :movies="filteredMovies.slice(0,12)"/>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue'
import MovieList from '@/components/movie/MovieList.vue';
import { useMovieStore } from '@/stores/movie'
import HeaderNav from '@/components/common/HeaderNav.vue';
import { useRouter } from 'vue-router';

const router = useRouter()
const store = useMovieStore()

const goToTest = () => {
  router.push({name:'TestView'})
}
// 영화 장르
const genres = ref(["액션", "모험", "애니메이션", "코미디", "범죄", "다큐멘터리", "드라마", "가족", "판타지", "역사", "공포", "음악", "미스터리", "로맨스", "SF", "TV 영화", "스릴러", "전쟁", "서부"])
const selectedGenre = ref("")

// 장르별 필터
const filteredMovies = computed(() => {
  if (!selectedGenre.value) {
    return store.movies
  }
  return store.movies.filter(movie => movie.genre.includes(selectedGenre.value))
})


onMounted(() => {
  // mount 되기전에 store에 있는 전체 게시글 요청 함수를 호출
  console.log('before getmovies')
  
  store.getMovies()
  
  console.log(store.movies)
  console.log('end of getmovies')

})
</script>

<style scoped>

body {
  position: relative;
}

.contanier {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

/* --------------------------------------------------------- */
/* nav bar 하단 */
.intro {
  width: 100%;
  height: 500px;
  display: flex;
  margin-bottom: 30px;
}

.intro-left {
  height: 100%;
  width: 70%;
  margin-right: 20px;
  background-color: white;
  border-radius: 20px;
}

.intro-right {
  height: 100%;
  width: 30%;
  border-radius: 20px;
  display: flex;
  flex-direction: column;
}

.mainmovie {
  width: 100%;
  height: 50%;
  background-color: white;
  border-radius: 20px;
  margin-bottom: 20px;
}

.test {
  width: 240px;
  height: 240px;
  background-color: rgb(255, 255, 115) !important; 
  border-radius: 50%;
  align-self: flex-end;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: 'Krona One';
  border: none;
}

.introtext {
  padding-left: 3%;
  padding-top: 5%;
  font-size: 70px;
  font-family: 'Krona One';
  line-height: 80px;
  letter-spacing: -0.1em;
}

.introtext2 {
  padding-left: 3%;
  padding-top: 12%;
  font-family: 'Krona One';
  line-height: 19px;
  letter-spacing: -0.1em;
  align-self: end;
  color: rgb(148, 148, 148);
}

h3 {
  font-size: 2em;
  font-family: 'Krona One';
  color: white;
  margin-bottom: 20px;
}



</style>
