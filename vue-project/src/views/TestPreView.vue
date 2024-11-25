<template>
  <div class="texts">
    <p class="welcome">Welcome to</p>
    <h1>MOOV.</h1>
    <p class="contexts">반갑습니다. {{username}} 님! <br> {{username}}님에게 맞는 영화를 추천해드릴게요!</p>
  </div>

  <button class="arrow-button" @click="goToTestView">&#8594;</button>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import { storeToRefs } from 'pinia';

const store = useAuthStore()

// storeToRefs로 반응형 상태 추출
const {username} = storeToRefs(store)
const router = useRouter()

// console.log(username.value)

const goToTestView = () => {
  router.push({name: 'TestView'})
}


</script>

<style scoped>
.texts {
  color: white;
  height: 100vh;
  padding-left: 80px;
  padding-top: 100px;
}

.welcome {
  font-size: 2vw;
  margin-bottom: 0;
  font-family: 'Krona One';
}

h1 {
  font-size: 6vw;
  margin-bottom: 30px;
  font-family: 'Krona One';
}

.contexts {
  font-size: 2vw;
  font-family: 'NoTo Sans Kr';
  font-weight: 200;
}

.arrow-button {
  position: absolute;
  bottom: 50px;
  right: 50px;
  background-color: transparent;
  font-size: 10vw;
  color: white;
  border: none;
}
</style>