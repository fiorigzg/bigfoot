<script setup>
  import { defineProps, ref } from 'vue'
  import { useScreenSize } from '@/stores/screenSize.js';


  const screenSizeStore = useScreenSize();

  const props = defineProps({
    height: {
      type: String,
      required: true
    },
  });

  const code = ref(null);

  const wheel = (e) => {
    code.value.scrollTo({
      left: code.value.scrollLeft + (e.deltaY < 0 ? -20 : 20)
    });
  };
</script>

<template>
  <!-- <div :style="{width: screenSizeStore.width + 'px', height: height + 'px'}" @wheel.prevent="wheel"> -->
  <div :style="{width: screenSizeStore.width + 'px', height: height + 'px'}">
    <svg :style="{width: screenSizeStore.width + 'px', height: height + 'px'}">
      <path class="ice" :d="`
        M 20,0
        ${screenSizeStore.width/2 - 10},0
        ${screenSizeStore.width/2},10
        ${screenSizeStore.width/2 + 10},0
        ${screenSizeStore.width - 10},0
        ${screenSizeStore.width},20
        ${screenSizeStore.width},35
        ${screenSizeStore.width - 10},50
        ${screenSizeStore.width},60
        ${screenSizeStore.width},${height-20}
        ${screenSizeStore.width-10},${height}
        ${screenSizeStore.width - 100},${height}
        ${screenSizeStore.width - 115},${height-10}
        ${screenSizeStore.width - 130},${height}
        10,${height}
        0,${height-10}
        0,${height+10}
        0,${height/2-15}
        10,${height/2-20}
        0,${height/2-30}
        0,20
        Z
      `"/>
      <path class="blique" :d="`
        M ${screenSizeStore.width - 100},10
        ${screenSizeStore.width - 20},10
        ${screenSizeStore.width - 20},50
        ${screenSizeStore.width - 30},30
        Z
      `"/>
      <path class="blique" :d="`
        M 10,${height- 100}
        10,${height - 20}
        50,${height - 20}
        30,${height - 30}
        Z
      `"/>
      <path class="blique" :d="`
        M 20,20
        20,150
        30,110
        50,120
        23,25
        200,150
        190,120
        200,100
        30,23
        180,50
        180,30
        200,20
        Z
      `"/>
      <path class="blique" :d="`
        M ${screenSizeStore.width - 20},${height - 20}
        ${screenSizeStore.width - 20},${height - 200}
        ${screenSizeStore.width - 50},${height - 50}
        ${screenSizeStore.width - 100},${height - 20}
        Z
      `"/>
    </svg>
    <pre v-highlightjs><code :style="{
      width: screenSizeStore.width - 60 + 'px',
      height: height - 60 + 'px',
      left: '15px',
      top: '15px'
    }" class="python" ref="code"><slot></slot></code></pre>
  </div>
</template>

<style scoped>
  div {
    margin-top: 1rem;
  }
  code {
    position: relative;
    font-size: 1rem;
    overflow: hidden;
    /* overflow-y: scroll; */
    /* font-family: 'Montserrat', sans-serif; */

    &::-webkit-scrollbar { width: 0; height: 0; }
    -ms-overflow-style: none;
    overflow: -moz-scrollbars-none;
    scrollbar-width: none;
  }
  svg {
    position: absolute;
    margin-top: 0;
    z-index: 10;
  }
  .ice {
    fill: rgba(151, 151, 252, 0.476);
  }
  .blique {
    fill: rgba(255, 255, 255, 0.355);
  }
</style>
