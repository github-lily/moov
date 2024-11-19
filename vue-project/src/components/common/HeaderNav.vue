<template>
    <header>
      <!-- <nav v-if="store.isLogin"> -->
        <!-- 로그인 된 상태 -->
        <!-- <RouterLink :to="{ name: 'MovieView' }">Movies</RouterLink> | -->
        <!-- <a href="#" @click.prevent="store.logOut">Logout</a> -->
      <!-- </nav> -->
      <!-- <nav v-else> -->
        <!-- 로그아웃 상태 -->

        <!-- <RouterLink :to="{ name: 'SignUpView' }">SingUp</RouterLink> |
        <RouterLink :to="{ name: 'LogInView' }">LogIn</RouterLink> -->

      <!-- </nav> -->

      <RouterView />

    </header>
  </template>
  

<script setup>
import { RouterView, RouterLink } from 'vue-router'
import { useAuthStore } from '@/stores/auth';

const store = useAuthStore()

</script>

<style scoped>
</style>
