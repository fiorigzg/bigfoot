<script setup>
  import { ref } from 'vue';
  import { useBoxplotChoose } from '@/stores/boxplotChoose.js';


  const boxplotChooseStore = useBoxplotChoose();

  const fromYear = ref(null);
  const toYear = ref(null);
  const statisticText = ref(null);

  const onGetClick = () => {
    fetch('http://127.0.0.1:5000/statistic', {
      method: 'POST',
      mode: "cors",
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        fromYear: parseInt(fromYear.value.value),
        toYear: parseInt(toYear.value.value),
        param: boxplotChooseStore.boxplotParam
      })
    }).then(res => {
      return res.json();
    }).then(data => {
      (data);
      statisticText.value.innerHTML = `Mean - ${Math.round(data.mean * 100)/100}, median - ${Math.round(data.median * 100)/100}`;
    });
  }
</script>

<template>
  <div id="statistic-block">
    <p>Get statistic for choosed param</p>
    <input type="number" ref="fromYear" placeholder="From year"/>
    <input type="number" ref="toYear" placeholder="To year"/>
    <button @click="onGetClick">Get</button>
    <p style="margin-top: 10px; margin-bottom: 30px;" ref="statisticText">Mean - 0, median - 0</p>
  </div>
</template>

<style scoped>
  #statistic-block {
    position: relative;
    width: 100%;
    p {
      margin: 0;
      font-family: 'Fugaz One', serif;
      font-weight: 900;
      font-size: 1.7rem;
      color: #6176b6;
    }
    input {
      width: 150px;
      height: 40px;
      outline: none;
      border: none;
      border-radius: 5px;
      text-align: center;
      margin: 0;
      font-family: 'Fugaz One', serif;
      font-weight: 900;
      font-size: 1rem;
      color: #6176b6;
      margin-left: 20px;
      margin-top: 10px;
    }
    button {
      width: 154px;
      height: 40px;
      outline: none;
      border: none;
      border-radius: 5px;
      text-align: center;
      margin: 0;
      font-family: 'Fugaz One', serif;
      font-weight: 900;
      font-size: 1rem;
      color: #6176b6;
      background-color: white;
      cursor: pointer;
      margin-left: 20px;
      margin-top: 10px;
      transition: all 0.2s ease-in-out;
      &:hover {
        background-color: #6176b6;
        color: white;
      }
    }
  }
</style>