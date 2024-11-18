import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const movies = ref([])                  // 영화 목록 담을 리스트
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)               // 토큰을 받아서 저장할 변수

  const router = useRouter()

  // 로그인 여부 확인
  const isLogin = computed(()=> {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

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

  // 회원가입 요청 액션
  const signUp = function(payload) {
    const {username, password1, password2} = payload

    axios ({
      method:'post',
      url:`${API_URL}/movies/signup/`,
      data: {
        username, password1, password2
      }
    })
      .then((res) => {
        console.log(res)
        console.log('회원가입 성공')
      })
      .catch((err) => {
        console.log(err)
      })
  }


  // 로그인 성공하면 token 변수에 토큰을 저장
  const logIn = function(payload) {
    const {username, password} = payload

    axios ({
      method:'post',
      url:`${API_URL}/accounts/login/`,
      data: {
        username, password,
      }
    })
      .then((res) => {
        token.value = res.data.key
        router.push({name : 'MovieView'})
        console.log('로그인 성공')
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
  // 로그아웃
  const logOut = function() {
    axios({
      method:'post',
      url:`${API_URL}/accounts/logout/`,
      headers : {Authorization:`Token ${token.value}`}
    })
    .then(res=> {
      console.log(res.data)
      token.value = null
      router.push({name:'LogInView'})
    })
    .catch(err=>console.log(err))
  }
  return { movies, API_URL, getMovies,signUp, logIn, logOut, token, isLogin }
}, { persist: true })
