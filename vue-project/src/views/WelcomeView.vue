<template>
  <div>
    <button @click="goSignUp">회원가입</button>
    <button @click="goLogIn">로그인</button>
  </div>
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
import { useRouter } from 'vue-router';
// import HeaderNav from './components/common/HeaderNav.vue';

const router = useRouter()
const goSignUp = function() {
  router.push({name:'SignUpView'})
}
const goLogIn = function() {
  router.push({name:'LogInView'})
}
</script>

<style scoped>

</style>