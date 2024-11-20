<template>
    <div class="comment-section">
      <h2>Comments</h2>
      
      <!-- 댓글 목록 -->
      <div v-if="comments.length">
        <div v-for="comment in comments" :key="comment.id" class="comment">
          <p><strong>{{ comment.user.username }}</strong>: {{ comment.content }}</p>
          <p class="comment-meta">{{ comment.created_at | formatDate }}</p>
  
          <!-- 수정 및 삭제 버튼 (작성자만 보이도록) -->
          <div v-if="isAuthor(comment.user.id)">
            <button @click="editComment(comment)">Edit</button>
            <button @click="deleteComment(comment.id)">Delete</button>
          </div>
        </div>
      </div>
      <div v-else>
        <p>No comments yet. Be the first to comment!</p>
      </div>
  
      <!-- 댓글 작성 폼 -->
      <form @submit.prevent="submitComment">
        <textarea v-model="newComment" placeholder="Write a comment..." required></textarea>
        <button type="submit">Submit</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  import { useRoute } from 'vue-router';
  import { useAuthStore } from '@/stores/auth';
  import { useMovieStore } from '@/stores/movie';
  
  const route = useRoute();
  const authStore = useAuthStore();
  const movieStore = useMovieStore();
  
  const comments = ref([]);
  const newComment = ref('');
  const moviePk = route.params.id;
  
  // 댓글 목록 조회 함수
  const fetchComments = async () => {
    try {
      const response = await axios.get(`${movieStore.API_URL}/api/v1/movies/${moviePk}/comments/`, {
        headers: {
          Authorization: `Token ${authStore.token}`
        }
      });
      comments.value = response.data;
    } catch (error) {
      console.error('Error fetching comments:', error);
    }
  };
  
  // 댓글 작성 함수
  const submitComment = async () => {
    if (!newComment.value.trim()) return;
    
    try {
      const response = await axios.post(`${movieStore.API_URL}/api/v1/movies/${moviePk}/comments/`, 
        { content: newComment.value },
        {
          headers: {
            Authorization: `Token ${authStore.token}`
          }
        }
      );
      comments.value.push(response.data);
      newComment.value = '';
    } catch (error) {
      console.error('Error submitting comment:', error);
    }
  };
  
  // 댓글 삭제 함수
  const deleteComment = async (commentId) => {
    try {
      await axios.delete(`${movieStore.API_URL}/api/v1/comments/${commentId}/`, {
        headers: {
          Authorization: `Token ${authStore.token}`
        }
      });
      comments.value = comments.value.filter(comment => comment.id !== commentId);
    } catch (error) {
      console.error('Error deleting comment:', error);
    }
  };
  
  // 작성자인지 확인하는 함수
  const isAuthor = (userId) => {
    return userId === authStore.user?.id;
  };
  
  // 컴포넌트가 마운트될 때 댓글 목록을 가져옴
  onMounted(() => {
    fetchComments();
  });
  </script>
  
  <style scoped>
  .comment-section {
    margin-top: 20px;
  }
  .comment {
    border-bottom: 1px solid #ddd;
    padding: 10px 0;
  }
  .comment-meta {
    font-size: 0.8em;
    color: #666;
  }
  textarea {
    width: 100%;
    margin: 10px 0;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ddd;
  }
  button {
    padding: 8px 15px;
    margin-right: 5px;
    background-color: #007bff;
    color: white;
    border: none;
    cursor: pointer;
  }
  button:hover {
    background-color: #0056b3;
  }
  </style>
  