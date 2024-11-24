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
          <div v-if="commentmovies.length > 0">
            <MovieList :movies="commentmovies"/>
          </div>
          <div v-else>
            <p class="no-comment">댓글을 작성해보세요!</p>
          </div>
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
import MovieList from '@/components/movie/MovieList.vue';
import { useMovieStore } from '@/stores/movie';
import { ref, onMounted } from 'vue';
import axios from 'axios';

const userStore = useAuthStore()
const {username} = storeToRefs(userStore)
console.log(username.value, '님의 마이페이지')

const store = useMovieStore()

//로그인 사용자가 작성한 댓글들의 전체 영화목록
const commentmovies = ref([])
const API_URL = 'http://127.0.0.1:8000';

onMounted(() => {
  if (username.value) {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/movies/${username.value}/comments/`,
      headers: {
        Authorization: `Token ${userStore.token}`,
      },
    })
      .then((response) => {
        commentmovies.value = response.data; // 반환된 영화 목록
        console.log('사용자가 댓글 단 영화 목록:',commentmovies.value)
      })
      .catch((error) => {
        console.error('댓글 영화 목록 가져오기 실패:', error);
      });
  }
});

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

.no-comment {
  font-family: 'Noto Sans KR';
  color: rgb(202, 202, 202);
}
</style>