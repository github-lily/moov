<template>
  <div>
    <h5>{{ movie.id }}</h5>
    <p>{{ movie.title }}</p>
    <p>{{ movie.content }}</p>
    <RouterLink 
      :to="{ name: 'DetailView', params: { id: movie.id } }"  
    >
      Detail
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
