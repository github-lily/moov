<template>
  <div class="container">

    <h1>MOOV.</h1>

    <form @submit.prevent="signUp">
      <p>사용자 이름 </p> 
      <input class="input" type="text" id="username" v-model.trim="username" placeholder="이름을 입력하세요.">

      <p>비밀번호 </p> 
      <input  class="input" type="password" id="password1" v-model.trim="password1" placeholder="비밀번호를 입력하세요.">

      <p>비밀번호 확인 </p> 
      <input  class="input thirdinput" type="password" id="password2" v-model.trim="password2" placeholder="비밀번호를 입력하세요.">

      <input class="btn"  type="submit" value="SignUp">
    </form>
    <a href="#" @click="goToLogIn">이미 회원이신가요?</a>
  </div>
</template>

<!-- @click="goToTestPreView" -->
<script setup>
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import { ref } from 'vue';

const store = useAuthStore()

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)

const router = useRouter()

const signUp = function() {
  const payload = {
    username : username.value,
    password1 : password1.value,
    password2 : password2.value,
  }
  store.signUp(payload)
}

const goToLogIn = () => {
  router.push({name:'LogInView'})
}

// const goToTestPreView = () => {
//   router.push({name:'TestPreView'})
// }
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;;
  width: 400px;
}

h1 {
  font-size: 50px;
  width: 400px;
  text-align: center;
  border-bottom: 2px solid white;
  margin-bottom: 50px;
  color: white;
  font-family: 'Krona One';
}

.form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 400px;
}

p {
  color: rgb(200, 200, 200);
  margin-bottom: 0;
  width: 100%;
  /* text-align: left; */
  font-size: 12px;
  font-family: 'NoTo Sans Kr';

}

input {
  width: 100%;
  height: 40px;
  margin-bottom: 10px;
  border-radius: 50px;
  padding-left: 20px;
}

.thirdinput {
  margin-bottom: 30px;
}

input::placeholder {
  color: rgb(200, 200, 200);        
  font-size: 14px;    
  font-family: 'NoTo Sans Kr';

}

.btn {
  width: 400px;
  background-color: rgb(255, 255, 115);
  color:black;
  border: none;
  border-radius: 50px;
  font-family: 'Krona One';
  margin-bottom: 20px;
}

.btn:hover {
  background-color: rgb(238, 238, 19);
}
a {
  color: white;
  font-size: 12px;
  font-family: 'NoTo Sans Kr';
}
</style>