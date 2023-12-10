<script setup>
  defineProps({})
</script>

<template>
  <p><slot/></p>
</template>

<style scoped>
  p {
    margin: 0;
    margin-top: 6rem;
    font-family: 'Fugaz One', serif;
    font-size: 2.5rem;
    color: #6176b6;
    filter: drop-shadow(0px 0px 0.5px #4e5f92);
  }
</style>
