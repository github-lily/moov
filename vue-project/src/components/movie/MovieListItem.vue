<template>
  <div class="movie-card">
    <div class="poster-container">

      <img class="poster" :src="poster" alt="영화포스터" >
      
      <!-- 마우스를 올릴 경우 -->
      <div class="overlay">

        <div class="movie-info" @click="goToDetail(movie)">
          <h3 class="movie-title">{{ movie.title }}</h3>
          <p class="overview">{{ truncateOverview(movie.overview) }}</p>

          <button 
            class="likebtn" 
            :class="{ 'liked': isLiked }" 
            @click.stop="toggleLike">
             &#x2665;
          </button>

        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter()
const props = defineProps({
  movie:Object
})

// 포스터 이미지 URL 설정
const poster = `https://image.tmdb.org/t/p/w500/${props.movie.poster_path}`

// 줄거리가 150자를 넘어갈 경우
const truncateOverview = (text) => {
  if (text.length > 150) {
    return text.slice(0, 150) + '...'
  }
  return text

}
const isLiked = ref(false)

const toggleLike = () => {
  isLiked.value = !isLiked.value
}


// 영화 클릭 시 DetailView로 이동
const goToDetail = (movie) => {
  router.push({
    name:'DetailView', params:{id:props.movie.id}})
}


</script>

<style>
.movie-card {
  width: 100%;
  transform-origin: center;
  padding: 10px;
}

.poster-container {
  position: relative;
  width: 90%;
  border-radius: 20px;
  overflow: hidden;
  transition: transform 0.3s ease;
}

.poster {
  width: 100%;
  height: auto;
  display: block;
  border-radius: 20px;
  transition: transform 0.3s ease;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: linear-gradient(
    to bottom, 
    rgba(0, 0, 0, 0.2),   
    rgba(0, 0, 0, 0.5),   
    rgba(0, 0, 0, 0.8),    
    rgba(0, 0, 0, 0.8)    
  );
  opacity: 0;
  transition: opacity 0.3s ease;
  display: flex;
  align-items: flex-end;
  justify-content: center;
}

.movie-info {
  color: white;
  width: 100%;
  height: 100%;
  padding: 20px;
  text-align: left;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-items: flex-start;
  margin-bottom: 10px;
  gap: 10px;
}

.movie-title {
  font-size: 1.2em;
  margin: 0;
  font-weight: bold;
  width: 100%;
  font-family: 'NoTo Sans KR';
  font-weight: light;
}

.overview {
  font-size: 0.8em;
  line-height: 1.4;
  margin: 0;
  padding: 0 10px;
  padding: 0;
  width: 100%;
  font-family: 'NoTo Sans KR';
  font-weight: lighter;
}

.poster-container:hover .overlay {
  opacity: 1;
}

.poster-container:hover  {
  transform: scale(1.05);
}

.likebtn {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  color: white;
  transition: color 0.3s ease;
  align-self: center;
}

.likebtn.liked {
  color: red;
}
</style>
