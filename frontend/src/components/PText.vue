<script setup>
  defineProps({})
</script>

<template>
  <p>&nbsp;&nbsp;&nbsp;<slot/></p>
</template>

<style scoped>
  p {
    margin: 0;
    margin-top: 1rem;
    font-family: 'Montserrat', sans-serif;
    font-size: 1rem;
    /* font-family: 'Fugaz One', serif; */
    /* font-size: 1.7rem; */
    color: #464c5f;
    font-weight: 900;
  }
</style>
