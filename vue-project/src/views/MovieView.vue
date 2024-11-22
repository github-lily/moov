<template>
  <div class="container">
    <HeaderNav />
    <div class="intro">
      <div class="intro-left">
        <p class="introtext">Learn English,<br> Enjoy Movies,<br> Love the Journey!</p>
        <p class="introtext2">
          At Moov. <br> we help you learn English through carefully selected movies <br> that match your proficiency level. <br> Start you journey today.
        </p>
      </div>
      <div class="intro-right">
        <div class="mainmovie"></div>
        <button class="test" @click="goToTest">TEST &#9654</button>
      </div>
    </div>
    <h3>Today's recommendation</h3>
    <div>
      <!-- 장르 선택 -->
      <div>
        <select id="genre-select" v-model="selectedGenre">
          <option value="" selected disabled hidden>All Genre</option>
          <option v-for="genre in genres" 
          :key="genre.id" :value="genre.name">{{ genre.name }}</option>
        </select>
      </div>
      <!-- 영화 12개만 출력 -->
      <MovieList :movies="filteredMovies.slice(0,12)"/>
    </div>

      <!-- 영화 목록 -->
    <!-- <MovieList :movies="paginatedMovies" /> -->

  </div>
</template>

<script setup>
import { onMounted, ref, computed, watch } from 'vue'
import MovieList from '@/components/movie/MovieList.vue';
import { useMovieStore } from '@/stores/movie'
import HeaderNav from '@/components/common/HeaderNav.vue';
import { useRouter } from 'vue-router';

const router = useRouter()
const store = useMovieStore()
const movies = ref([])

const goToTest = () => {
  router.push({name:'TestView'})
}


// // 장르별 필터
// const filteredMovies = computed(() => {
//   if (!selectedGenre.value) {
//     return store.movies
//   }
//   return store.movies.filter(movie => movie.genre.includes(selectedGenre.value))
// })


onMounted(() => {
  // mount 되기전에 store에 있는 전체 게시글 요청 함수를 호출
  // console.log('before getmovies')
  
   store.getMovies()
  movies.value = store.movies;
  
  // console.log(store.movies)
  // console.log('end of getmovies')

})

// 영화 장르 (id와 name이 매칭된 형태로 저장)
const genres = ref([
  { id: 28, name: "Action" },
  { id: 12, name: "Adventure" },
  { id: 16, name: "Animation" },
  { id: 35, name: "Comedy" },
  { id: 80, name: "Crime" },
  { id: 99, name: "Documentary" },
  { id: 18, name: "Drama" },
  { id: 10751, name: "Family" },
  { id: 14, name: "Fantasy" },
  { id: 36, name: "History" },
  { id: 27, name: "Horror" },
  { id: 10402, name: "Music" },
  { id: 9648, name: "Mystery" },
  { id: 10749, name: "Romance" },
  { id: 878, name: "Science Fiction" },
  { id: 10770, name: "TV Movie" },
  { id: 53, name: "Thriller" },
  { id: 10752, name: "War" },
  { id: 37, name: "Western" }
])
const selectedGenre = ref("")

console.log('movie:', store.movies)

// 장르별 필터
const filteredMovies = computed(() => {
  if (!selectedGenre.value) {
    return store.movies.value || [];
  }
  
  return (store.movies.value || []).filter(movie => 
    movie.genre && movie.genre.includes(selectedGenre.value)
  );
});
// const filteredMovies = computed(()=> {
//   return store.movies.filter(function(movie) {
//     console.log('movieGenre:', movie.genres)
//     return movie.genre === selectedGenre.value})
// })

watch(selectedGenre, () => {
  currentPage.value = 1;
});

// // filteredMovies를 장르별로 필터링
// const filteredMovies = computed(() => {
//   if (!selectedGenre.value) {
//     // store.movies가 배열인지 확인하고, 배열이 아닌 경우 빈 배열 반환
//     return Array.isArray(store.movies) ? store.movies : [];
//   }
//   // 선택된 장르와 일치하는 영화만 필터링하고, 배열인지 확인
//   const selectedGenreId = genres.value.find(genre => genre.name === selectedGenre.value)?.id;
//   return Array.isArray(store.movies) 
//     ? store.movies.filter(movie => movie.genres.includes(selectedGenreId))
//     : []; // 배열이 아닌 경우 빈 배열 반환
// });



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
    position: relative;
    overflow: visible;
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
