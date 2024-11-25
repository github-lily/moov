<template>
  <div>
    <HeaderNav />
    <h2 style="color: white;">{{ username }}님이 좋아요한 영화 </h2>
    <ul>
      <!-- 영화 목록 -->
      <!-- <li v-for="movie in likedMovies" :key="movie.id">
        {{ movie.title }}
      </li> -->
    </ul>
  </div>
</template>

<script setup>
import HeaderNav from '@/components/common/HeaderNav.vue'
import { useRoute } from 'vue-router'
import { ref, onMounted } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useUserStore } from '@/stores/user'
import { storeToRefs } from 'pinia'

const route = useRoute()
const authStore = useAuthStore()
const userStore = useUserStore()
const { username } = storeToRefs(authStore)
const { user } = storeToRefs(userStore)
const likedMovies = ref([])



// onMounted(async () => {
//   console.log('해당 유저 정보:', user.value)
//   try {
//     // 사용자 정보 가져오기
//     await userStore.getUser()
    
//     // 사용자의 좋아요 영화 목록 가져오기
//     axios({
//       method: 'get',
//       url: `http://127.0.0.1:8000/movies/likemovies/${username.value}/`,
//       headers: {
//         Authorization: `Token ${authStore.token}`
//       }
//     })
//     .then((res) => {
//       likedMovies.value = res.data
//       console.log('좋아요한 영화 목록:', likedMovies.value)
//     })
//     .catch((err) => {
//       console.error('좋아요 영화 목록 가져오기 실패:', err)
//     })
//   } catch (error) {
//     console.error('Error:', error)
//   }
// })

</script>

<style scoped>
/* h1 {
  font-family: 'Krona One';
  text-align: center;
  color: white;
  font-size: 20px;
} */
</style>