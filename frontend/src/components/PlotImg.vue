<script setup>
  import { defineProps } from 'vue';

  
  const props = defineProps({
    name: {
      type: String,
      required: true
    },
    width: {
      type: String,
      default: '100%'
    },
    align: {
      type: String,
      default: 'center'
    }
  });

  const imageName = '/src/assets/plots/' + props.name;
</script>

<template>
  <div :style="{ textAlign: align }">
    <img :src="imageName" :style="{ 
      width: '100%',
      maxWidth: width
    }"/>
  </div>
</template>

<style scoped>
  div {
    width: 100%;
  }
  img {
    margin-top: 2rem;
  }
</style>
