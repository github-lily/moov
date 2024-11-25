import { createRouter, createWebHistory } from 'vue-router'

import MovieView from '@/views/MovieView.vue'
import DetailView from '@/views/DetailView.vue'
import SignUpView from '@/views/accounts/SignUpView.vue'
import LogInView from '@/views/accounts/LogInView.vue'
import WelcomeView from '@/views/WelcomeView.vue'
import TestPreView from '@/views/TestPreView.vue'
import TestView from '@/views/TestView.vue'
import LikeMoviesView from '@/views/LikeMoviesView.vue'
import MovieComment from '@/components/movie/MovieComment.vue'
import MyPageView from '@/views/MyPageView.vue'
import SearchResult from '@/components/movie/SearchResult.vue'

const router = createRouter({

  
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // 첫 화면
    {
      path: '/',
      name: 'WelcomeView',
      component: WelcomeView
    },
    // 메인페이지
    {
      path: '/movies',
      name: 'MovieView',
      component: MovieView,
    },
    // 상세페이지
    {
      path: '/movies/:id',
      name: 'DetailView',
      component: DetailView,
      props: true
    },
    // 회원가입
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    // 로그인
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    // 테스트 시작 예고 페이지
    {
      path: '/testpreview',
      name: 'TestPreView',
      component: TestPreView
    },
    // 테스트 페이지
    {
      path: '/test',
      name: 'TestView',
      component: TestView
    },
    // 좋아요한 페이지 목록
    {
      path: '/mypage/:username/likemovieslist/',
      name: 'LikeMoviesView',
      component: LikeMoviesView, 
      props:true
    },

    // 사용자가 댓글 단 영화 목록
    {
      path: '/movies/:username/comments',
      name: 'MovieComment',
      component: MovieComment
    },
    // 마이페이지
    {
      path: '/MyPage/',
      name: 'MyPage',
      component: MyPageView
    },
    // 프로필 이미지 변경
    // {
    //   path: '/upload_img/:username',
    //   name: 'profileImg',
    //   component: ProfileImgChange
    // },
<<<<<<< HEAD
=======
    
>>>>>>> 24029fa6bd8c673291a8382d18501212edceba80
    //영화 검색 페이지
    {
      path: '/search/:keyword',
      name: 'SearchResults',
      component: SearchResult
    }

  ]
})

export default router
