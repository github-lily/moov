import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useAuthStore = defineStore('auth', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref('eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxNTkzZTYxYWQxMDIyNDZhOTM1MzdiZjgwZjQ1OTYwMSIsIm5iZiI6MTczMTk3NzQ1NS44OTU0MDYsInN1YiI6IjY3MzZlNDVlMjk1NGQyNjQ3NjI1YTc0YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mKWeZNUGw2sPFImPftyZMH1hqp__bu1zYpVJxpw4bdQ')               // 토큰을 받아서 저장할 변수

  const router = useRouter()

  // 로그인 여부 확인
  const isLogin = computed(()=> {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })


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
  return { API_URL, signUp, logIn, logOut, token, isLogin }
}, { persist: true })
