import { createRouter, createWebHistory } from 'vue-router'

import MovieView from '@/views/MovieView.vue'
import DetailView from '@/views/DetailView.vue'
import CreateView from '@/views/CreateView.vue'
import SignUpView from '@/views/accounts/SignUpView.vue'
import LogInView from '@/views/accounts/LogInView.vue'
import TmdbTopRated from '@/components/tmbd/TmdbTopRated.vue'
import TmdbPopular from '@/components/tmbd/TmdbPopular.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // 메인페이지
    {
      path: '/',
      name: 'MovieView',
      component: MovieView,
      children : [
        {
          path : "popular",
          name : "tmdbPopular",
          component : TmdbPopular
        },
        {
          path : "toprated",
          name : "tmdbTopRated",
          component : TmdbTopRated
        },
      ]
    },
    {
      path: '/movies/:id',
      name: 'DetailView',
      component: DetailView
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    }
  ]
})

export default router
