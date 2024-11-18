<template>
  <div>
    <h1>Sign Up Page</h1>
    <form>
      <div>
        <label for="username">username : </label>
        <input type="text" id="username" v-model.trim="username">
      </div><br>
      <div>
        <label for="password1">password1 : </label>
        <input type="password" id="password1" v-model.trim="password1">
      </div><br>
      <div>
        <label for="password2">password2 : </label>
        <input type="password" id="password2" v-model.trim="password2">
      </div><br>

      <input type="submit" value="SignUp">
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
