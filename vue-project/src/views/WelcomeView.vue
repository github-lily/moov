<template>
  <div class="box">
    <div class="backtext">
      Learn English, <br>
      Enjoy Movies, <br>
      Love the journey!
    </div>
    <div class="container" >
      <h1>MOOV.</h1>
        <p>계정이 이미 있으신가요?</p>
        <button class="btn btn-primary" type="submit" @click="goToLogIn">Log In <small class="tr">&#9654</small></button>  
        <p>계정이 없으신가요?</p>
        <button class="btn btn-primary" type="submit" @click="goToSignUp">Sign Up <small class="tr">&#9654</small></button>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter()

const goToSignUp = () => {
  router.push({name:'SignUpView'})
}

const goToLogIn = () => {
  router.push({name:'LogInView'})
}
</script>

<style scoped>

.backtext {
  color: rgb(54, 54, 54);
  position: absolute;
  left: 30px;
  top: 100px;
  font-size: 5vw;
  font-family: 'Krona One';
}

.container {
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 300px;
  position: relative;
}


h1 {
  font-size: 100px;
  width: 500px;
  /* border-bottom: 2px solid black; */
  text-align: center;
  margin-bottom: 50px;
  color: white;
  font-family: 'Krona One';
}
.btn {
  border-radius: 50px;
  font-size: 20px;
  width: 500px;
  margin-bottom: 20px;
  background-color: rgb(255, 255, 115);
  border: none;
  color: black;
  font-family: 'Krona One';
  padding: 5px 0;
}

.btn:hover {
  background-color: rgb(238, 238, 19);
}

.tr {
  font-size: 10px;
  vertical-align: middle;
}

p {
  font-size: 12px;
  margin-bottom: 2px;
  color: rgb(200 , 200, 200);
  font-family: 'Noto Sans KR';

}
</style>