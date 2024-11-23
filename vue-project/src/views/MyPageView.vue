<template>
  <HeaderNav/>
  <div class="container">
    <div class="mypage-container">

      <div class="profile-container">
        <p class="hello">안녕하세요. {{ username }}님!</p>
        <div class="img-box">
          <img src="#" alt="프로필 이미지">
        </div>
        <p class="level">{{ username }}님의 level</p>
      </div>
      
      <div class="userinfo">
        <div class="my-favorites components">
          <p class="favorite"> My Favorites</p>
          <LikeMovies />
        </div>
        <div class="my-comments components">
          <p class="favorite">My Comments</p>
          <commentMovies/>
        </div>
      </div>
    </div>
  </div>
  
</template>

<script setup>
import HeaderNav from '@/components/common/HeaderNav.vue';
import { useUserStore } from '@/stores/user';
import { storeToRefs } from 'pinia';
import { useAuthStore } from '@/stores/auth';
import LikeMovies from '@/components/movie/LikeMovies.vue';
import commentMovies from '@/components/movie/commentMovies.vue';

const userStore = useAuthStore()

const {username} = storeToRefs(userStore)
console.log(username.value, '님의 마이페이지')


</script>

<style scoped>
.mypage-container {
  width: 100%;
  /* border: 1px solid white; */
  display: flex;
  flex-direction: column;
  margin-top: 50px;
  /* justify-content: center; */
  /* align-items: center; */
}

.profile-container {
  width: 50%;
  height: 100%;
  /* border: 1px solid red; */
  display: flex;
  flex-direction: column;
  align-self: center;
  justify-content: center;
  align-items: center;
}

.hello {
  font-size:2em;
  font-family: 'Noto Sans KR';
  color: white;
  font-weight: lighter;
}

.img-box {
  width: 300px;
  height: 300px;
  background-color: white;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.level {
  font-size: 1.2em;
  color: white;
  font-family: 'Noto Sans KR';
  font-weight: lighter;
  padding-top: 20px;
  margin-bottom: 0;
}

.useinfo {
  border: 1px solid yellow;

}
.components {
  margin-top: 50px;
}

.favorite {
  color: white;
  font-size: 2em;
  font-family: 'Krona One';
}
</style>