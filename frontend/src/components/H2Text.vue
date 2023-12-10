<script setup>
  defineProps({})
</script>

<template>
  <p><slot/></p>
</template>

<style scoped>
  p {
    margin: 0;
    margin-top: 1rem;
    font-family: 'Fugaz One', serif;
    font-weight: 900;
    font-size: 1.7rem;
    color: #6176b6;
  }
</style>
