import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'
import router from '@/router'

export const useAuthStore = defineStore('auth', () => {
  
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)               // 토큰을 받아서 저장할 변수
  const router = useRouter()
  const username = ref('')
  
  
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
    const {username: signUpUsername, password1, password2} = payload
    
    axios ({
      method:'post',
      url:`${API_URL}/accounts/signup/`,
      data: {
        username: signUpUsername, password1, password2
      }
    })
    .then((res) => {
      console.log(res)
      console.log(signUpUsername, '님 회원가입 성공')
      username.value = signUpUsername
      router.replace({name:'TestPreView'})
    })
    .catch((err) => {
      console.log(err)
    })
  }
  
  
  // 로그인 성공하면 token 변수에 토큰을 저장
  const logIn = function(payload) {
    const {username: loginUsername, password} = payload
    
    axios ({
      method:'post',
      url:`${API_URL}/accounts/login/`,
      data: {
        username: loginUsername, password,
      }
    })
    .then((res) => {
      token.value = res.data.key
      username.value = loginUsername
      router.push({name : 'MovieView'})
      console.log(loginUsername,'님 로그인 성공')
    })
    .catch((err) => {
      console.log(err)
      alert(' 사용자 정보가 없습니다!')
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
      username.value=''
      router.push('/')
    })
    .catch(err=>console.log(err))
  }

  function setUsername(newUsername) {
    username.value = newUsername
  }

  return { API_URL, signUp, logIn, logOut, token, isLogin, setUsername, username}
}, { persist: true })

