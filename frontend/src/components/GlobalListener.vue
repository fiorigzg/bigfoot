<script setup>
  import { useScreenSize } from '@/stores/screenSize.js';


  const screenSizeStore = useScreenSize();

  let timer;
  window.onresize = () => {
    if (timer) {
      window.clearTimeout(timer);
    }

    timer = setTimeout(() => {
      screenSizeStore.setWidth(window.innerWidth > 750 ? window.innerWidth * 0.5 : window.innerWidth * 0.9);
    }, 100);
  }  
</script>

<template>
</template>

<style scoped>
</style>
