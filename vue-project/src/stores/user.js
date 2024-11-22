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

    const getUser = function () {
        if (!authStore.token) {
            console.error('User is not authenticated: No token found')
            return
          }

        axios({
            method: 'get',
            url: `${API_URL}/accounts/user`,
            headers: {
            Authorization: `Token ${authStore.token}`
            }
        })
        .then((res) => {
            user.value = res.data
        })
        .catch((err) => console.log('Failed to fetch user data:', err))
    }

	return { user, isLike, isMovieLike, getUser }
}, { persist: true })
