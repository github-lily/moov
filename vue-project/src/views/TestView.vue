<template>
  <div> 
    <h1>Test Page</h1>
    <!-- 나중에 지울 코드 -->
    <RouterLink :to="{name:'MovieView'}">Go Movies</RouterLink>

    <!-- chat gpt english level test -->
    <div class="chat-box">
      <!-- 주고 받는 데이터를 실시간(stream)으로 출력 -->
      <div v-for="(message, index) in chatMessages" :key="index" class="message">
          <p><strong>{{ newUser.username }}</strong> {{ message.user }}</p>
          <p><strong>Tester:</strong> {{ message.ai }}</p>
      </div>
    </div>
    <!-- error message 출력 -->
    <!-- <div v-if="errorMessage" class="error">
      <p>{{ errorMessage }}</p>
    </div> -->
    <div class="input-box">
      <input
        v-model="userMessage"
        type="text"
        placeholder="Type your message"
        @keyup.enter="sendMessage"
      />
      <button @click="sendMessage">Send</button>
    </div>
  </div>
</template>

<script>
import { RouterLink } from 'vue-router';
import MovieView from './MovieView.vue';
import axios from "axios"
import { errorMessages } from 'vue/compiler-sfc';
import { useUserStore } from '@/stores/user';


export default {
  data() {
    return {
      userMessage: "",
      chatMessages: [],
      errorMessages:"", //에러 메시지를 저장
      stream: null, // EventSource 객체
      newUser: null,    // 사용자 정보를 저장
    };
  },
  methods: {
    
    // user 정보 가져오기
    async getUserInfo() {
        const userStore = useUserStore();
        const newUser = await userStore.getUser(); // 데이터를 비동기로 가져옴
        if (newUser) {
            this.newUser = newUser; // 가져온 데이터를 컴포넌트 상태에 저장
        } else {
            console.error("Failed to fetch user info.");
        }
    },

    sendMessage() {
      if (!this.userMessage.trim()) return;

      // Add user message to chat
      this.chatMessages.push({ user: this.userMessage, ai: "" });

      // Stream AI response
      const eventSource = new EventSource("http://127.0.0.1:8000/api/chat/stream-chat/");
      this.stream = eventSource;

      // 연결이 성공적으로 됐을 때 호출
      eventSource.onopen = () => {
        console.log("Connection opened");
        this.errorMessage = ""; // 연결 성공 시 에러 메시지 초기화
      };

      // 서버에서 데이터가 도착했을 때 호출
      eventSource.onmessage = (event) => {
        const lastMessage = this.chatMessages[this.chatMessages.length - 1];
        lastMessage.ai += event.data; // Append AI's response chunk
      };

      // 연결 중 문제가 발생했을 때 호출
      eventSource.onerror = (error) => {
        console.error("EventSource error:", error);

        // 에러 메시지 표시
        this.errorMessage = "Connection error. Please try again later.";

        // EventSource 닫기
        eventSource.close();
      };

      // input 창 초기화
      this.userMessage = ""; 
    },
  },

  // 컴포넌트가 로드될 때 사용자 정보를 가져오기
  mounted() {
    this.getUserInfo();
  },

  // 컴포넌트가 파괴될 때 EventSource 연결 닫기
  beforeDestroy() {
    if (this.stream) {
      this.stream.close();
    }
  },
};

</script>

<style>
h1 {
  color: white;
}
</style>

<!-- gpt가 만들어준 스타일 -->
.chat-box {
  height: 300px;
  overflow-y: scroll;
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
}

.message {
  margin-bottom: 10px;
}

.input-box {
  display: flex;
  gap: 10px;
}

input {
  flex: 1;
  padding: 5px;
  border: 1px solid #ccc;
}

button {
  padding: 5px 10px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}