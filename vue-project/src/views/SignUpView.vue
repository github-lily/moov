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
html, body {
  height: 100%;
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #000;
  color: #fff;
  /* font-family: Arial, sans-serif; */
}

.title {
  font-size: 40px;
  text-align: center;
  margin-bottom: 30px;
  /* position: relative; */
}

.title::after {
  content: "";
  display: block;
  width: 100%; 
  height: 2px;
  background-color: #fff;
  margin: 10px auto 0;
  max-width: 300px;

}

.container {
  text-align: center;
  padding: 40px;
  border-radius: 8px;
  width: 100%; 
  max-width: 300px;
}

form {
  display: flex;
  flex-direction: column;
  gap: 0px;
  /* width: 100%; */
}

.label {
  font-size: 14px;
  color: #b1b1b1;
  text-align: center;
  display: block;
  margin-bottom: 10px;
}

.input {
  padding: 10px 20px;
  font-size: 14px;
  /* border: 1px solid #ccc; */
  border-radius: 50px;
  background: #fff;
  color: #000;
  width: 100%;
}

.input::placeholder {
  color: #aaa;
}

.btn {
  padding: 10px;
  font-size: 16px;
  background-color: #fdf232;
  color: #000;
  font-weight: bold;
  border: none;
  border-radius: 50px;
  cursor: pointer;
  width: 100%; 
  transition: background-color 0.3s ease;
}

.btn:hover {
  background-color: #e0ca28;
}
</style>