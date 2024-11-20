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
      <MovieList/> 
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import MovieList from '@/components/movie/MovieList.vue';
import { useMovieStore } from '@/stores/movie'
import HeaderNav from '@/components/common/HeaderNav.vue';
import { useRouter } from 'vue-router';

const router = useRouter()
const store = useMovieStore()

const goToTest = () => {
  router.push({name:'TestView'})
}

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
