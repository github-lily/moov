<template>
  <div class="comments-section">
    <div class="comments-create">
      <textarea v-model="newComment" placeholder="  댓글을 달아보세요!"></textarea>
      <button @click="addComment">등록</button>
    </div>
    <ul>
      <li v-for="comment in comments" :key="comment.id">
        <p style="color: white;" ><strong>{{ comment.username }}</strong>: {{ comment.content }}</p>
        <!-- <div v-if="user.username === comment.username">
          <button @click="editComment(comment)">Edit</button>
          <button @click="deleteComment(comment.id)">Delete</button>
        </div> -->
      </li>
    </ul>
  </div>
</template>

<script setup> 
import { ref, onMounted, computed, watch } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useMovieStore } from '@/stores/movie'
import { defineProps } from 'vue';
import { useUserStore } from '@/stores/user';

const props = defineProps({
  movieId:String
})

// console.log(props.movieId) 38나옴

const userStore = useUserStore()
const authStore = useAuthStore()
const movieStore = useMovieStore()
const movieId = props.movieId // 현재 영화 ID를 경로에서 가져옴

const comments = ref([])
const newComment = ref('')


// 댓글 가져오기
const fetchComments = async () => {
  await movieStore.getMovieComments(props.movieId) // 영화 ID에 맞는 댓글 가져오기
  comments.value = movieStore.comments // 댓글 업데이트
}


// movieId 변경 시 댓글 새로 고침
watch(
  () => props.movieId,
  (newId, oldId) => {
    if (newId !== oldId) {
      fetchComments() // 댓글 목록 새로고침
    }
  },
  { immediate: true }
)

const user = computed(()=> {
  return userStore.user
}) 

console.log('comment', user)


// 댓글 추가
const addComment = async () => {
  if (!newComment.value.trim()) return
  await movieStore.addComment(props.movieId, newComment.value)
  await fetchComments() // 댓글 추가 후 댓글 목록 새로고침
  newComment.value = '' // 입력창 초기화
}

//댓글 삭제하기
// const deleteComment = async (commentId) => {
//   try {
//     await movieStore.deleteComment(commentId)
//     await fetchComments() // 댓글 목록 새로고침
//     comments.value = movieStore.comments
//   } catch (error) {
//     console.error(error)
//   }
// }


// 초기 데이터 로드
onMounted(() => {
  if (props.movieId) fetchComments()
})


</script>

<style scoped>
.comments-create {
  padding: 20px;
  border-radius: 10px;
  width: 100%;
  display: flex;
  justify-content: space-between;
}
textarea {
  width: 100%;
  height: 40px;
  margin-right: 10px;
  font-size: 16px;
  /* border-radius: 5px; */
  border: none;
  border-bottom: 1px solid #ccc;
  background-color: transparent;
  display: block;
  box-sizing: border-box;
  color: white;
}

textarea::placeholder {
  font-size: 16px;
  color: #888; 
  font-family: 'Noto Sans KR' ;
}

textarea:focus {
  border: none;
  outline: none;
  border-bottom: 1px solid #ccc;
}

button {
  width: 10%;
  font-family: 'Noto Sans KR';
  border: none;
  border-radius: 50px;
  background-color: #fff;
}
</style>
