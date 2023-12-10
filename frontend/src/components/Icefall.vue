<script setup>
  import {ref} from 'vue';


  const icefallLeft = ref(null);
  const icefallRight = ref(null);

  window.addEventListener('scroll', () => {
    icefallLeft.value.style.top = `calc(${window.scrollY * 0.51}px - 325vw)`;
    icefallRight.value.style.top = `calc(${window.scrollY * 0.51}px - 325vw)`;
  });
</script>

<template>
  <img class="icefall left" ref="icefallLeft" src="@/assets/icefall.svg"/>
  <img class="icefall right" ref="icefallRight" src="@/assets/icefall.svg"/>
</template>

<style scoped>
  .icefall {
    position: fixed;
    width: 15%;
    left: 2%;
    filter: drop-shadow(0px 5px 5px #4e5f92);
    z-index: -1;
    top: -325vw;
    &.left {
      left: 2%;
    }
    &.right {
      left: 83%;
      transform: scaleX(-1);
    }
  }
</style>
