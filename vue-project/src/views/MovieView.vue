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

    <div class="recom">
      <h3>Today's recommendation</h3>
        <!-- 장르 선택 -->
          <select id="genre-select" v-model="selectedGenre" class="custom-select">
            <option value="" selected disabled hidden class="placeholder-option">All Genre</option>
            <option class="lists" v-for="genre in genres" 
            :key="genre.id" :value="genre.name">{{ genre.name }}</option>
          </select>
    </div>
      
      <!-- 필터된 영화들만 출력 -->
      <MovieList :movies="filteredMovies"/>

  </div>
</template>

<script setup>
import { onMounted, ref, computed, watch } from 'vue'
import MovieList from '@/components/movie/MovieList.vue';
import { useMovieStore } from '@/stores/movie'
import HeaderNav from '@/components/common/HeaderNav.vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import { storeToRefs } from 'pinia';
import { useUserStore } from '@/stores/user';


const goToTest = () => {
  router.push({name:'TestView'})
}


const router = useRouter()
const store = useMovieStore()
const authStore = useAuthStore()
const userStore = useUserStore()
const {username} = storeToRefs(authStore)

console.log(username.value, '님의 메인페이지')
const movies = ref([])
const selectedGenre = ref("")

const filteredMovies = computed(() => {
  if(!selectedGenre.value) {
    return movies.value
  }
  return movies.value.filter(movie => 
  movie.genres.some(genre => genre.name === selectedGenre.value))  //장르리스트 중 하나라도 맞으면 넣겠다.
})

// 영화 장르 (id와 name이 매칭된 형태로 저장)
const genres = ref([
  { id: 28, name: "액션" },
  { id: 12, name: "어드벤처" },
  { id: 16, name: "애니메이션" },
  { id: 35, name: "코미디" },
  { id: 80, name: "범죄" },
  { id: 99, name: "다큐멘터리" },
  { id: 18, name: "드라마" },
  { id: 10751, name: "가족" },
  { id: 14, name: "판타지" },
  { id: 36, name: "역사" },
  { id: 27, name: "공포" },
  { id: 10402, name: "음악" },
  { id: 9648, name: "미스터리" },
  { id: 10749, name: "로맨스" },
  { id: 878, name: "SF" },
  { id: 10770, name: "TV 영화" },
  { id: 53, name: "스릴러" },
  { id: 10752, name: "전쟁" },
  { id: 37, name: "서부" }
])

console.log('movie:', store.movies)

// 사용자 정보, 영화 정보 가져오기
onMounted(async () => {
  store.getMovies();
  movies.value = store.movies;
  
  if (authStore.token) {
    userStore.getUser()
    console.log('현재 로그인한 유저 정보:', userStore.user)
    console.log('유저의 토큰:', authStore.token)
  } else {
    console.log('로그인이 필요합니다.')
  }
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


.recom  {
  display: flex;
  padding: 20px 0;}

.custom-select {
  background-color: transparent;
  /* border-radius: 5px;
   */
  color: white;
  padding: 8px;
  font-family: 'NoTo Sans KR';
  border: none;
  border-bottom: 0.1px solid rgb(161, 161, 161);
  /* text-align: center; */
}

.custom-select:focus {
  outline: none;
}

h3 {
  font-size: 2em;
  font-family: 'Krona One';
  color: white;
  margin-right: 100px;
}

.lists {
  background-color: rgb(54, 54, 54); 
  color: white;           
  font-family: 'NoTo Sans KR';
  font-weight: lighter;
  /* text-align: center; */
  /* padding: auto; */
}
</style>
