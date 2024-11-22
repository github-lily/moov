<template>
  <div>
    <HeaderNav/>
    <!-- <h1 style="color: white;">마이페이지</h1> -->

    <form action="" @click.prevent="">{{ user }}</form>
    <div class="mypage-container"></div>
  </div>
</template>

<script setup>
import HeaderNav from '@/components/common/HeaderNav.vue';
import { useUserStore } from '@/stores/user';

const userStore = useUserStore()
const user = userStore.getUser()

console.log(user)

</script>

<style scoped>

</style>