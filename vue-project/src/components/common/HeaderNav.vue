<template>
  <div>
    <div class="container">
      <nav class="navbar navbar-expand-lg bg-body-tertiary" >

        <div class="container-fluid">
          <a class="navbar-brand" href="#" @click="GoToHome">MOOV.</a>
          
          <!-- 화면 줄어들 때 -->
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>

          <div class="collapse navbar-collapse" id="navbarSupportedContent">

            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link" aria-current="page" href="#" @click="GoToHome" >홈</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#" @click="GoToLikeMovies">내가 찜한 리스트</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#"  @click="GoToMyPage">마이페이지</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#" @click="handleLogout">로그아웃</a>
              </li>
            </ul>
            <!-- 검색창 -->
            <form class="d-flex" role="search" @submit.prevent="handleSearch">
              <input class="movieSearch" placeholder="영화를 검색해보세요!" v-model="searchKeyword">
              <button class="btn" type="submit">
                <i class="fas fa-search"></i>
              </button>
            </form>
            
          </div>

        </div>

      </nav>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import { useMovieStore } from '@/stores/movie';
import { ref } from 'vue';
import { onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router';

const movieStore = useMovieStore()
const authStore = useAuthStore()
const router = useRouter()


const GoToHome = () => {
  router.push({name:'MovieView'})
}

const GoToLikeMovies =  () => {
  router.push({name:'LikeMoviesView'})
}

const GoToMyPage = () => {
  router.push({name:'MyPage'})
}

const handleLogout = () => {
  authStore.logOut()
}

          
const searchKeyword = ref(null)
const movies = ref([])


const handleSearch = async () => {
  // console.log('검색키워드:', searchKeyword.value) //잘 나옴
  movieStore.getMovies();
  movies.value = movieStore.movies;
  
  // 만약 사용자가 검색을 했다면
  if (searchKeyword.value) {
    

    // 새로고침 오류 해결 
    if (searchKeyword.value) {


    // // 먼저 영화 데이터를 가져옵니다
    // await movieStore.getMovies()
    
    // // 검색 결과 페이지로 이동
    // await router.push({
    //   name: 'SearchResults',
    //   params: { keyword: searchKeyword.value }
    // })

    // // 검색 후 입력창 초기화
    // searchKeyword.value = ''

    // 새로고침해야하는 코드
    router.push({
      name: 'SearchResults',
      params: { keyword: searchKeyword.value }
    })


  }
}

// onBeforeRouteUpdate((to, from) => {

//   })
}

</script>

<style scoped>

/* nav bar */

.container {
    width: 100%;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
}

.navbar {
  width: 100%;
  height: 45px;
  margin: 20px 0px;
  border-radius: 50px; 
  padding-left: 50px;
  padding-right: 50px;
  background-color: red;
  position: sticky;
  top: 0;
  z-index: 1000;
}

.bg-body-tertiary {
  background-color: rgb(255, 255, 115) !important; 
}

.navbar-brand {
  font-size: 20px;
  font-weight: bold;
  margin-right: 50px;
}

.nav-link {
  font-family: 'Noto Sans KR';
}

.movieSearch {
  border: none;
  border-bottom: 1px solid gray;
  width: 100%;
  text-align: center;
  background-color: transparent;
  font-family: 'Noto Sans KR';
}

.movieSearch:focus {
  border: none ;
  border-bottom: 1px solid gray;
  outline: none;
}

</style>