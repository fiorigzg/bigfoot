<script setup>
  import H1Text from '@/components/H1Text.vue';
  import PText from '@/components/PText.vue';
  import GlobalListener from '@/components/GlobalListener.vue';
  import Header from '@/components/Header.vue';
  import Footer from '@/components/Footer.vue';
</script>

<template>
  <header>
    <Header/>
    <GlobalListener/>
  </header>

  <main>
    <img id="logo" src="@/assets/bigfoot.svg"/>
    <p id="title-text">Searching for Bigfoot<br/>project 2012</p>
    <H1Text>Introduction</H1Text>
    <PText>This project is a study of the bigfoot sightings dataframe created by the bfro.net forum. It contains various evidences of encounters with bigfoot, which will be analyzed in this project. </PText>
    <H1Text>Used technologies</H1Text>
    <PText>For data analysis, pandas, seaborn and matplotlib are used here. Vue 3 + Vite was chosen as the frontend and Flask as the backend.</PText>
    <H1Text>Theme</H1Text>
    <PText>As a theme for the design, the style of 2000s websites was chosen. That's why the project is called Searching for Bigfoot project 2012</PText>
    <H1Text>Let's start</H1Text>
    <PText>Click on Main page in the page header to start the analysis.</PText>
    <Footer/>
  </main>
</template>
    

<style scoped lang="scss">
  #logo {
    width: 15vw;
    display: block;
    margin: 0 auto 2rem;
    margin-top: 250px;
  }
  #title-text {
    margin: 0;
    font-family: 'Rubik Bubbles', serif;
    font-size: 5rem;
    color: #4e5f92;
    text-align: center;
    margin-top: 40px;
    margin-bottom: 160px;
  }
  @media (max-width: 750px) {
    #logo {
      width: 50vw;
    }
    #title-text {
      font-size: 4rem;
    }
  }
</style>
