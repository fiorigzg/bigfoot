<script setup>
</script>

<template>
  <div id="menu">
    <img id="github-img" src="@/assets/github.svg"/>
    <a id="github-link" href="https://github.com/fiornrrn">fiornrrn</a>
    <p id="footer-text">Rodikov Maksim, copyright 2023, MIT Licence</p>
  </div>
</template>

<style scoped lang="scss">
  #menu {
    position: relative;
    width: 100vw;
    height: 200px;
    margin-left: -25vw;
    margin-top: 100px;
    background-color: #c2c4f8;
  }
  #github-img {
    position: absolute;
    width: 50px;
    top: 50%;
    left: 10%;
    transform: translate(-50%, -50%);
  }
  #github-link {
    position: absolute;
    top: 50%;
    left: calc(10% + 80px);
    transform: translate(-50%, -50%);
    font-family: 'Fugaz One', serif;
    font-size: 1.2rem;
    color: #4e5f92;
    font-weight: 600;
    cursor: pointer;
  }
  #footer-text {
    position: absolute;
    top: 40%;
    left: 80%;
    transform: translate(-50%, -50%);
    font-family: 'Fugaz One', serif;
    font-size: 1rem;
    color: #4e5f92;
    font-weight: 600;
    text-align: center;
  }
  @media screen and (max-width: 750px) {
    #menu {
      margin-left: -6%;
    }
  }
</style>
