<template>
  <div class="movie-card">
    <button @click="goToDetail(movie)">
      <img class="poster" :src="poster" alt="영화포스터" >
    </button>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter()
const props = defineProps({
  movie:Object
})

// 포스터 이미지 URL 설정
const poster = `https://image.tmdb.org/t/p/w500/${props.movie.poster_path}`


// 영화 클릭 시 DetailView로 이동
const goToDetail = () => {
  router.push({name:'DetailView', params:{id:props.movie.id}})
}


</script>

<style>
.movie-card {
  width: 100%;
  transform-origin: center;
  padding: 10px;
}

.poster {
  width: 90%;
  height: auto;
  display: block;
  border-radius: 20px;
  transition: transform 0.3s ease;
}

.poster:hover {
  transform: scale(1.05); 
}

</style>
