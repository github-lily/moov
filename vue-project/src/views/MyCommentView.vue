<template>
  <div class="my-comments-container">
    <HeaderNav />
    <h2>My Comments</h2>
    <div v-if="comments.length === 0">No comments yet.</div>
    <ul>
      <li v-for="comment in comments" :key="comment.id">
        <p>Movie: {{ comment.movie_title }}</p>
        <p>{{ comment.content }}</p>
        <button @click="deleteComment(comment.id)">Delete</button>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useMovieStore } from '@/stores/movie'

const authStore = useAuthStore()
const movieStore = useMovieStore()
const comments = ref([])

const fetchComments = async () => {
  try {
    const response = await movieStore.getUserComments(authStore.user.id)
    comments.value = response.data
  } catch (error) {
    console.error(error)
  }
}

const deleteComment = async (commentId) => {
  try {
    await movieStore.deleteComment(commentId)
    comments.value = comments.value.filter(comment => comment.id !== commentId)
  } catch (error) {
    console.error(error)
  }
}

onMounted(() => {
  fetchComments()
})
</script>

<style scoped>
.my-comments-container {
  padding: 20px;
  background-color: #f4f4f4;
  min-height: 100vh;
}
</style>
