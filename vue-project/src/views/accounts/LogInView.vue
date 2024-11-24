<template>
  <div class="container">
    <h1>MOOV.</h1>
    <form class="form" @submit.prevent="logIn">
      <p>사용자 이름 </p>
      <input type="text" id="username" v-model.trim="username"  placeholder="이름을 입력하세요.">
      <p>비밀번호 </p>
      <input class="secondinput" type="password" id="password" v-model.trim="password" placeholder="비밀번호를 입력하세요.">
      <!-- <input type="submit" value="Log In" > -->
      <div>
        <button class="btn btn-primary" type="submit">Log In</button>
      </div>
      <!-- <p v-if="errorMessage" class="error">{{ errorMessage }}</p> -->
      <a href="#" @click="goToSignUp">회원가입</a>
    </form>
  </div>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
// import { errorMessages } from 'vue/compiler-sfc';

const store = useAuthStore()
const username = ref(null)
const password = ref(null)
const router = useRouter()
const errorMessage = ref(null)

const logIn = function() {
  const payload = {
    username : username.value,
    password : password.value
  }
  store.logIn(payload)
}

const goToSignUp = () => {
  router.push({name:'SignUpView'})
}


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

.secondinput {
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

.error {
  color: red;
  font-size: 12px;
  margin-top: 10px;
}

</style>
