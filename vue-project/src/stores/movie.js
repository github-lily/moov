import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useAuthStore } from './auth'

export const useMovieStore = defineStore('movie', () => {
  const movies = ref([])                  // 영화 목록 담을 리스트
  const API_URL = 'http://127.0.0.1:8000'

  const router = useRouter()
  const authStore = useAuthStore()

  // DRF로 전체 게시글 요청을 보내고 응답을 받아 movies에 저장하는 함수
  const getMovies = function () {
    console.log(authStore.token)
    console.log('-=================================')
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/movies/`,
      headers : {
        Authorization : `Token ${authStore.token}`
      }
    })
      .then((res) => {
        // console.log(res.data)
        movies.value = res.data
        console.log(movies)
      })
      .catch((err) => {
        console.log(err)
      })
  }
  return { movies, API_URL, getMovies,   }
}, { persist: true })
