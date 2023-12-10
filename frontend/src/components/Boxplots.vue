<script setup>
  import { computed } from 'vue';
  import { useBoxplotChoose } from '@/stores/boxplotChoose.js';


  const boxplotChooseStore = useBoxplotChoose();

  const params = [
    'index',
    'latitude',
    'longitude',
    'number',
    'temperature_high',
    'temperature_mid',
    'temperature_low',
    'dew_point',
    'humidity',
    'cloud_cover',
    'moon_phase',
    'precip_intensity',
    'precip_probability',
    'pressure',
    'uv_index',
    'visibility',
    'wind_bearing',
    'wind_speed',
]

const boxplotParam = computed(() => boxplotChooseStore.boxplotParam);
</script>
<template>
  <div id="boxplots-block">
    <img :src="`src/assets/plots/bp-${boxplotParam}.png`" id="boxplot-img" align="left"/>
    <div id="boxplot-choose">
      <div class="param-btn" v-for="param in params">
        <img src="@/assets/cloud.svg"/>
        <p @click="boxplotChooseStore.setBoxplotParam(param)">{{param}}</p>
      </div>
      <div class="blank-margin"/>
    </div>
  </div>
</template>

<style scoped lang="scss">
  #boxplots-block {
    position: relative;
    width: 100%;
    height: 520px;
  }
  #boxplot-choose {
    position: absolute;
    width: 250px;
    height: 390px;
    margin-left: calc(500px + (100% - 500px) / 2 - 125px);
    margin-top: 70px;
    background-color: #7979d8;
    border-radius: 7px;
    overflow-y: scroll;
    text-align: center;
    outline: 20px solid #4e5f92;
    
    &::-webkit-scrollbar { width: 0; height: 0; }
    -ms-overflow-style: none;
    overflow: -moz-scrollbars-none;
    scrollbar-width: none;

    .param-btn {
      img {
        width: 200px;
        margin-top: 30px;
        filter: drop-shadow(1px 1px 4px #4e5f92);
      }
      p {
        margin-top: -60px;
        font-family: 'Rubik Bubbles', serif;
        font-size: 1.2rem;
        color: #f9fbff;
        filter: drop-shadow(1px 1px 3px #26345c);
        cursor: pointer;

        transition: all 0.1s ease-in-out; 
        &:hover {
          filter: drop-shadow(1px 1px 7px #26345c);
        }
      }
    }
  }
  #boxplot-img {
    position: absolute;
    width: 500px;
    margin-top: 2rem;
  }
  .blank-margin {
    height: 40px;
  }
  @media (max-width: 1550px) {
    #boxplots-block {
      position: relative;
      height: fit-content;
      margin-bottom: 80px;
    }
    #boxplot-img {
      position: relative;
      width: 100%;
      margin-left: -30px;
    }
    #boxplot-choose {
      position: relative;
      top: 20px;
      margin-left: 0px;
      width: 100%;
      height: 160px;
      margin-bottom: 45px;
    }
  }
</style>
