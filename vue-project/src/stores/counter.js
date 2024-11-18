import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const movies = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref('60bef4280ca8898de183bf2df8d1e306e11d11f6')
  const router = useRouter()
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
    // const username = payload.username
    // const password1 = payload.password1
    // const password2 = payload.password2

    // 구조분해할당 방법
    const {username, password1, password2} = payload

    axios ({
      method:'post',
      url:`${API_URL}/movies/signup/`,
      data: {
        // username : username,
        // password1 : password1,
        // password2 : password2
        // 단축 객체 형태( 객체와 이름이 같을 경우 )
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


  // 회원가입 요청 액션
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
        // console.log(res)
        // console.log('로그인 성공')
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
  return { movies, API_URL, getMovies,signUp, logIn, token, isLogin }
}, { persist: true })
