<template>
  <div>
    <RouterLink 
      :to="{ name: 'DetailView', params: { id: movie.id } }">
      [상세보기]
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  movie: Object
})
</script>

<style>

</style>
