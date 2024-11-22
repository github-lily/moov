<template>
  <div class="comments-section">
    <div class="comments-create">
      <textarea v-model="newComment" placeholder="  댓글을 달아보세요!"></textarea>
      <button @click="addComment">등록</button>
    </div>
    <ul>
      <li v-for="comment in comments" :key="comment.id">
        {{ comment }}
        <p style="color: white;" ><strong>{{ comment.username }}</strong>: {{ comment.content }}</p>
        <div v-if="user.username === comment.username">
          <button @click="editComment(comment)">Edit</button>
          <button @click="deleteComment(comment.id)">Delete</button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup> 
import { ref, onMounted, computed } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useMovieStore } from '@/stores/movie'
import { defineProps } from 'vue';
import { useUserStore } from '@/stores/user';

const props = defineProps({
  movieId:String
})

const userStore = useUserStore()
const authStore = useAuthStore()
const movieStore = useMovieStore()
const movieId = props.movieId // 현재 영화 ID를 경로에서 가져옴

const comments = ref([])
const newComment = ref('')
const commentId = ref(0)
// console.log('comment component',props.movieId)

const user = computed(()=> {
  return userStore.user
}) 

console.log('comment', user)

// 댓글 가져오기
const fetchComments = async () => {
  try {
    await movieStore.getMovieComments(movieId) // movieId를 전달
    comments.value = movieStore.comments
    console.log(comments.value)
  } catch (error) {
    console.error(error)
  }
}

// 댓글 추가
const addComment = async () => {
  if (!newComment.value.trim()) return
  try {
    await movieStore.addComment(movieId, newComment.value) // movieId 포함
    comments.value = movieStore.comments // store에서 업데이트된 comments를 가져옴
    newComment.value = ''
    commentId.value = id++
  } catch (error) {
    console.error(error)
  }
}

const deleteComment = async (commentId) => {
  try {
    await movieStore.deleteComment(commentId)
    comments.value = movieStore.comments
  } catch (error) {
    console.error(error)
  }
}

// 초기 데이터 로드
onMounted(() => {
  fetchComments()
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
