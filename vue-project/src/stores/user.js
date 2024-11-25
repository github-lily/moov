import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios'
import { useMovieStore } from '@/stores/movie'
import { useAuthStore } from './auth'

export const useUserStore = defineStore('user', () => {
	const API_URL = 'http://127.0.0.1:8000'
    const movieStore = useMovieStore()
    const authStore = useAuthStore()
    const user = ref([])
    let isLike = ref(false)
    let isMovieLike = ref(false)
    const likedMovies = ref([])

    //11.25 비동기로 수정
    const getUser = async function () {
        if (!authStore.token) {
            console.error('User is not authenticated: No token found')
            return null;
          }

        try {
            const response = await axios.get(`${API_URL}/accounts/user`, {
                headers: {
                    Authorization: `Token ${authStore.token}`,
                },
            });
            user.value = response.data; // Pinia 상태 업데이트
            return response.data; // 사용자 정보 반환
        } catch (error) {
            console.error('Failed to fetch user data:', error);
            return null; // 실패 시 null 반환
        }
    }

    // 좋아요 기능 구현
    const likeMovies = function() {
        axios ({
            method:'post',
            url:`${API_URL}/movies/:movie_id/likemovies`,
            headers: {
                Authorization: `Token ${authStore.token}`
                }
        })
        .then((res)=> {
            likedMovies.value = res.data
        })
    }

	return { user, isLike, isMovieLike, getUser }
}, { persist: true })
