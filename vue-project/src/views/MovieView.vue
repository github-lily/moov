<template>
  <div class="container">
      <nav class="navbar navbar-expand-lg bg-body-tertiary" >

        <div class="container-fluid">
          <a class="navbar-brand" href="#">MOOV.</a>
          
          <!-- 화면 줄어들 때 -->
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>

          <div class="collapse navbar-collapse" id="navbarSupportedContent">

            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link" aria-current="page" href="#" >홈</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">내가 찜한 리스트</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" >마이페이지</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" >로그아웃</a>
              </li>
            </ul>

            <!-- 검색 창 -->
            <form class="d-flex" role="search">
              <input class="movieSearch" placeholder="영화를 검색해보세요!">
              <button class="btn" type="submit">
                <i class="fas fa-search"></i>
              </button>
            </form>
          </div>

        </div>

      </nav>
      <div class="intro">
        <div class="intro-left">
          <p class="introtext">Learn English,<br> Enjoy Movies,<br> Love the Journey!</p>
          <p class="introtext2">
            At Moov. we help you learn English through carefully selected movies <br> that match your proficiency level. <br> Start you journey toda
          </p>
        </div>
        <div class="intro-right">
          <div class="mainmovie"></div>
          <div class="test"></div>
        </div>
      </div>
    <RouterView />
  </div>

</template>

<script setup>
import { onMounted } from 'vue'
import { useMovieStore } from '@/stores/movie'
import { RouterLink } from 'vue-router'

const store = useMovieStore()

onMounted(() => {
  // mount 되기전에 store에 있는 전체 게시글 요청 함수를 호출
  console.log('before getmovies')
  
  store.getMovies()
  console.log('end of getmovies')
})
</script>

<style scoped>

/* nav bar */
body {
  position: relative;
}

.contanier {
    width: 100%;
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
}

.bg-body-tertiary {
  background-color: rgb(255, 255, 115) !important; 
}

.navbar-brand {
  font-size: 20px;
  font-family: 'Krona One';
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

/* --------------------------------------------------------- */
/* nav bar 하단 */
.intro {
  width: 100%;
  height: 500px;
  display: flex;
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
</style>
