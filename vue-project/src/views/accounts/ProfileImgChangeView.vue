<!-- 선배 파일 그대로 가져옴! 확인 후 수정해야함..근데 이건 안중요하니까 일단 미뤄둡시다요 -->

<template>
    <div class="profileImg">
      <!-- <p>{{ this.profile.profile_img }}</p>
      <p>{{ this.profile.username }}</p>
      
      <p>{{ isEditing }}</p>
      <p>{{ payload.username }}</p>
      <p>{{ payload.profile_img }}</p> -->
      <div class="container">
        <h1>Profile Image</h1>
        <div class="profile">
          <div class="showImg">
            <div class="before">
              <img v-if="profile.profile_img" :src="profile.profile_img">
              <img v-else src="@/assets/default_profile.jpg">
              <div class="change">변경 전</div>
            </div>
            <div class="after">
              <img v-if="payload.profile_img" :src="payload.profile_img">
              <img v-else src="@/assets/default_profile.jpg">
              <div class="change">변경 후</div>
            </div>
          </div>
          <div class="input">
            <input class="form-control" type="text" v-model="payload.profile_img" placeholder="이미지 주소를 넣어주세요!">
            <button class="yp-btn yp-btn-white" @click="onUpdate">Update</button>
            <router-link :to="{ name: 'profile', params: { username: profile.username} }">
              <button class="yp-btn yp-btn-white">Cancel</button>
            </router-link>
          </div>
        </div>
        
      </div>
      <!-- <button @click="switchIsEditing">Cancle</button> -->
  
      <!-- <span v-if="!isEditing">
        <button @click="switchIsEditing">Edit</button> |
      </span> -->
    </div>
  </template>
  
  <script>
  import { mapGetters, mapActions } from 'vuex'
  export default {
    name: 'profile_img',
    props: {
      profile_img: String,
    },
    computed: {
        ...mapGetters(['profile', 'notMyAccount', 'isFollowing', 'currentUser']),
    },
    data() {
      return {
        isEditing: false,
        payload: {
          username: this.$route.params.username,
          profile_img: '',
        },
      }
    },
    methods: {
      ...mapActions(['fetchProfile', 'followProfile', 'updateImg',]),
      switchIsEditing() {
        this.isEditing = !this.isEditing
      },
      onUpdate() {
        this.updateImg(this.payload)
        this.isEditing = false
      }
    },
    created () {
      const payload = { username: this.$route.params.username }
      this.fetchProfile(payload)
    }
  
  }
  </script>
  
  <style scoped>
  @import 'https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap';
    * {
      font-family: 'Noto Sans KR',  sans-serif;
      font-weight: 500;
    }
    .profileImg{
      height: 800px;
      background-color: #fff6ea;
    }
    h1{
      padding-top: 30px;
      padding-left: 200px;
      padding-right: 200px;
      margin-bottom: 50px;
    }
    .change {
      margin-bottom: 50px;
      color: gray;
    }
    input {
      width: 600px;
      display: flex;
      justify-content: center;
      align-items: center;
    }
  
      img {
      border-radius: 70%;
      margin-right: 15px;
      width: 300px;
      height: 300px;
    }
    .profile {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }
    .showImg {
      display: flex;
    }
    .before {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      margin-right: 100px;
    }
    .after {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }
    .input {
      display: flex;
    }
  
    /* 버튼 css */
      /* Buttons */
    
    #sub,
    #sub:hover,
    #sub:focus,
    #sub:active {
      color: rgb(0, 0, 0);
      text-decoration: none;
      outline: none;
      background-color: rgb(255, 255, 255);
      border-radius: 5px;
    }
  
    #sub {
      font-family: 'Noto Sans KR', sans-serif;
      font-weight: 500;
      position: relative;
      height: 40px;
      width: 90px;
      z-index: 1;
    }
  
    #sub:before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      /* border: 2px solid #fff; */
      border-radius: 5px;
      z-index: -1;
      /* transform: skew(-6deg); */
      background: none;
      transition: 0.3s background ease, 0.3s border ease;
    }
  
    .yp-btn,
    .yp-btn:hover,
    .yp-btn:focus,
    .yp-btn:active {
      color: rgb(0, 0, 0);
      text-decoration: none;
      outline: none;
      background-color: rgb(255, 255, 255);
      border-radius: 5px;
      border: 1.5px solid lightgray;
    }
  
    .yp-btn {
      font-family: 'Noto Sans KR', sans-serif;
      font-weight: 500;
      position: relative;
      height: 43.1px;
      width: 120px;
      z-index: 1;
    }
    .yp-btn.yp-btn-xs {
      padding: 4px 15px;
    }
    .yp-btn.yp-btn-sm {
      padding: 8px 20px;
    }
    .yp-btn.yp-btn-md {
      padding: 15px 40px;
    }
    .yp-btn.yp-btn-lg {
      padding: 15px 50px;
    }
    .yp-btn.yp-btn-full {
      margin-left: 0;
      margin-right: 0;
      width: 100%;
    }
    .yp-btn:before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      /* border: 2px solid #fff; */
      border-radius: 5px;
      z-index: -1;
      /* transform: skew(-6deg); */
      background: none;
      transition: 0.3s background ease, 0.3s border ease;
    }
  
  
    .yp-btn-white:hover,
    .yp-btn-white:focus,
    .yp-btn-white.focus,
    .yp-btn-white:active,
    .yp-btn-white.active {
      color: rgb(0, 0, 0);
      border: 1px solid #fff;
    }
    .yp-btn-white:hover:before,
    .yp-btn-white:focus:before,
    .yp-btn-white.focus:before,
    .yp-btn-white:active:before,
    .yp-btn-white.active:before {
      /* border: 1px solid #fff; */
      border-radius: 5px;
      background: #FFD2E2;
    }
  
    input:checked + label {
      background: #FFD2E2;
      border-radius: 5px;
      color: black;
    }
  
    label {
      display: flex;
      justify-content: center;
      align-items: center;
      -webkit-user-select:none;
      -moz-user-select:none;
      -ms-user-select:none;
      user-select:none;
      cursor: pointer;
    }
  </style>