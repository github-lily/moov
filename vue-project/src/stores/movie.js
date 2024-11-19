import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useMovieStore = defineStore('movie', () => {
  const movies = ref([])                  // 영화 목록 담을 리스트
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref('eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxNTkzZTYxYWQxMDIyNDZhOTM1MzdiZjgwZjQ1OTYwMSIsIm5iZiI6MTczMTk3NzQ1NS44OTU0MDYsInN1YiI6IjY3MzZlNDVlMjk1NGQyNjQ3NjI1YTc0YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mKWeZNUGw2sPFImPftyZMH1hqp__bu1zYpVJxpw4bdQ')               // 토큰을 받아서 저장할 변수

  const router = useRouter()

  // DRF로 전체 게시글 요청을 보내고 응답을 받아 movies에 저장하는 함수
  const getMovies = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/movies/`,
      headers : {
        Authorization : `Token ${token.value}`
      }
    })
      .then((res) => {
        // console.log(res.data)
        movies.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  return { movies, API_URL, getMovies, token,  }
}, { persist: true })
