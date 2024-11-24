<template>
  <div class="commented-movies">
    <div v-if="loading" class="text-center p-4">
      <p>Loading...</p>
    </div>
    
    <div v-else-if="error" class="text-center p-4 text-red-600">
      {{ error }}
    </div>
    
    <div v-else class="movie-grid">
      <div v-if="!commentedMovies?.length" class="text-center p-4">
        <p>아직 댓글을 단 영화가 없습니다.</p>
      </div>
      
      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <div v-for="movie in commentedMovies" :key="movie.id" 
          class="movie-card p-4 border rounded-lg shadow-md hover:shadow-lg transition-shadow">
          <div class="relative">
            <img 
              :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" 
              :alt="movie.title"
              class="w-full h-48 object-cover rounded-md"
              @error="handleImageError"
            >
            <div class="absolute bottom-0 left-0 right-0 bg-black bg-opacity-70 text-white p-2">
              <h3 class="text-lg font-semibold truncate">{{ movie.title }}</h3>
            </div>
          </div>
          
          <div class="mt-2">
            <p class="text-sm text-gray-600 line-clamp-2">{{ movie.overview }}</p>
            <button 
              @click="goToMovieDetail(movie.id)"
              class="mt-2 px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 transition-colors w-full"
            >
              상세보기
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import axios from 'axios'

const router = useRouter()
const authStore = useAuthStore()
const commentedMovies = ref([])
const loading = ref(true)
const error = ref(null)

const getCommentedMovies = async () => {
  try {
    loading.value = true
    error.value = null
    
    // API URL에서 username이 제대로 전달되는지 확인
    const username = authStore.username
    if (!username) {
      throw new Error('사용자 정보를 찾을 수 없습니다.')
    }
    
    const response = await axios({
      method: 'get',
      url: `${import.meta.env.VITE_API_URL}/api/v1/movies/${username}/comments/`,
      headers: {
        Authorization: `Token ${authStore.token}`
      }
    })
    
    if (response.data) {
      commentedMovies.value = response.data
      console.log('Fetched commented movies:', response.data)
    }
  } catch (err) {
    error.value = '영화 목록을 불러오는데 실패했습니다.'
    console.error('Error fetching commented movies:', err)
  } finally {
    loading.value = false
  }
}

const handleImageError = (event) => {
  event.target.src = '/placeholder-movie.jpg'
}

const goToMovieDetail = (movieId) => {
  router.push({ name: 'DetailView', params: { id: movieId }})
}

onMounted(async () => {
  await getCommentedMovies()
})
</script>

<style scoped>
.movie-grid {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
}

.movie-card {
  background: white;
  transition: all 0.3s ease;
}

.movie-card:hover {
  transform: translateY(-2px);
}

.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>