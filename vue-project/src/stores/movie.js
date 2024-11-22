import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter,useRoute } from 'vue-router'
import { useAuthStore } from './auth'

export const useMovieStore = defineStore('movie', () => {
  const movies = ref([])                  // 영화 목록 담을 리스트
  const API_URL = 'http://127.0.0.1:8000'

  const router = useRouter()
  const authStore = useAuthStore()

  // DRF로 전체 게시글 요청을 보내고 응답을 받아 movies에 저장하는 함수
  const getMovies = function () {
    console.log('token',authStore.token)
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
        // console.log(movies)
      })
      .catch((err) => {
        console.log(err)
      })
  }


  // 영화 상세 정보를 받아오는 함수
	const route = useRoute()
	const movie = ref(null)
	const getMovieDetail = function () {
    console.log('route.params.id:', route.params.id) // 현재 경로 파라미터 id 확인
	axios({
		method: 'get',
		url: `${API_URL}/api/v1/movies/${route.params.id}`,
		headers: {
		Authorization: `Token ${authStore.token}`
	}
	})
		.then((res) => {
			movie.value = res.data
      console.log('movie.js',movie.value)
		})
		.catch((err) => {
			console.log(err)
		})
	}

   // 댓글 리스트 요청
   const comments = ref([])
   const getMovieComments = function (movieId) {
     axios({
       method: 'get',
       url: `${API_URL}/api/v1/movies/${movieId}/comments/`,
       headers: {
         Authorization: `Token ${authStore.token}`
       }
     })
       .then((res) => {
         comments.value = res.data
       })
       .catch((err) => {
         console.log(err)
       })
   }
 
   // 댓글 작성
   const addComment = function (movieId, content) {
    console.log('movie.js',movieId)
     axios({
       method: 'post',
       url: `${API_URL}/api/v1/movies/${movieId}/comments`,
       headers: {
         Authorization: `Token ${authStore.token}`
       },
       data: { content }
     })
       .then((res) => {
        console.log(res.data) 
        comments.value.push(res.data)
         
       })
       .catch((err) => {
         console.log('Failed to add comment:', err)
       })
   }
 
   // 댓글 삭제
   const deleteComment = function (commentId) {
     axios({
       method: 'delete',
       url: `${API_URL}/api/v1/comments/${commentId}/`,
       headers: {
         Authorization: `Token ${authStore.token}`
       }
     })
       .then(() => {
         comments.value = comments.value.filter(comment => comment.id !== commentId)
       })
       .catch((err) => {
         console.log(err)
       })
   }


  return { movies, API_URL, getMovies, getMovieDetail, comments, getMovieComments, addComment, deleteComment}
}, { persist: true })