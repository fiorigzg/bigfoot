<script setup>
  import {ref} from 'vue';


  const iceRef = ref(null);

  window.addEventListener('scroll', () => {
    iceRef.value.style.top = `calc(${window.scrollY * -0.3}px - 150px)`;
  });
</script>

<template>
  <div id="menu" ref="iceRef">
    <img id="ice-img" src="@/assets/icepicks.svg"/>
    <div id="btn-block">
      <a id="btn-1" href="/">
        Home page
      </a>
      <a id="btn-2" href="/research">
        Main page
      </a>
      <a id="btn-3" href="/streamlit">
        Streamlit
      </a>
    </div>
  </div>
</template>

<style scoped lang="scss">
  #menu {
    position: fixed;
    width: 100%;
    top: -150px;
    left: 0;
    #ice-img {
      position: absolute;
      width: 2000px;
      filter: drop-shadow(0px 5px 15px #4e5f92);
      z-index: 15;
    }
    #btn-block {
      position: absolute;
      margin-top: 150px;
      z-index: 16;
      width: 100%;
      a {
        position: absolute;
        margin-top: 30px;
        font-family: 'Fugaz One', serif;
        font-size: 1.9rem;
        color: #e6edfe;
        font-weight: 600;
        cursor: pointer;
        filter: drop-shadow(1px 1px 3px #4e5f92);
        
        transition: all 0.1s ease-in-out; 
        &:hover {
          margin-top: 25px;
          filter: drop-shadow(1px 1px 5px #26345c);
        }
      }

      #btn-1 {
        margin-left: 50px;
      }
      #btn-2 {
        margin-left: calc(50% - 75px);
      }
      #btn-3 {
        margin-left: calc(100% - 200px);
      }
    }
  }
</style>
