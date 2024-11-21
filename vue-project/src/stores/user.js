import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios'
import { useMovieStore } from '@/stores/movie'

export const useUserStore = defineStore('user', () => {
	const API_URL = 'http://127.0.0.1:8000'
    const movieStore = useMovieStore()
    const user = ref([])
    let isLike = ref(false)
    let isMovieLike = ref(false)

    const getUser = function () {
        axios({
            method: 'get',
            url: `${API_URL}/accounts/user`,
            headers: {
            Authorization: `Token ${movieStore.token}`
            }
        })
        .then((res) => {
            user.value = res.data
        })
        .catch((err) => console.log(err))
    }

	return { user, isLike, isMovieLike, getUser }
}, { persist: true })
