<template>
  <div>
    <h1>LogIn Page</h1>
    <form>
      <div>
        <label for="username">username : </label>
        <input type="text" id="username" v-model.trim="username">
      </div><br>
      <div>
        <label for="password">password : </label>
        <input type="password" id="password" v-model.trim="password">
      </div><br>

      <input type="submit" value="LogIn" >
    </form>
  </div>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth';
import { ref } from 'vue';

const store = useAuthStore()
const username = ref(null)
const password = ref(null)





</script>

<style>

</style>
