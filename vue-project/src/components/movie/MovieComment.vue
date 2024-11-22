<template>
  <div class="comments-section">
    <h3>Comments</h3>
    <ul>
      <li v-for="comment in comments" :key="comment.id">
        <p><strong>{{ comment.username }}</strong>: {{ comment.content }}</p>
        <div v-if="authStore.user.id === comment.user">
          <button @click="editComment(comment)">Edit</button>
          <button @click="deleteComment(comment.id)">Delete</button>
        </div>
      </li>
    </ul>
    <div>
      <textarea v-model="newComment" placeholder="Write a comment..."></textarea>
      <button @click="addComment">Post Comment</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useMovieStore } from '@/stores/movie'

const props = defineProps({
  movieId : Number
})

const authStore = useAuthStore()
const movieStore = useMovieStore()
const movieId = props.movieId // 현재 영화 ID를 경로에서 가져옴
const comments = ref([])
const newComment = ref('')
console.log('comment component',props.movieId)

// 댓글 가져오기
const fetchComments = async () => {
  try {
    await movieStore.getMovieComments(movieId) // movieId를 전달
    comments.value = movieStore.comments
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
.comments-section {
  padding: 20px;
  background-color: #fff;
  border-radius: 10px;
}
</style>
