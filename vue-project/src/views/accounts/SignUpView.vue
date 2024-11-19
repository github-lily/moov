<template>
  <div class="container">
    <h1 class="title">MOOV.</h1>

    <form>
      <div>
        <label class="label" for="username">사용자 이름 </label> 
        <input class="input" type="text" id="username" v-model.trim="username">
      </div><br>
      <div>
        <label class="label" for="password1">비밀번호 </label> 
        <input  class="input" type="password" id="password1" v-model.trim="password1">
      </div><br>
      <div>
        <label class="label" for="password2">비밀번호 확인 </label> 
        <input  class="input" type="password" id="password2" v-model.trim="password2">
      </div><br>

      <input class="btn"  type="submit" value="SignUp">
    </form>

  </div>
</template>

<script setup>
import { ref } from 'vue';

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)

</script>

<style>

</style>