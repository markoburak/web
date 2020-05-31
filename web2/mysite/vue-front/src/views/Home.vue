<template>
  
  <div class="page">
    <!-- <Names/> -->
    <Header/>
    <Loader v-if="loading"/>
    <div v-else>
      <div>
      <div class="title" @click="show = !show">
        <h1>Best mobile company</h1>
      </div>
      <transition>
      <h3 v-if="show"> Products availiable...<br>
      Below</h3>
      </transition>
      </div>
    <Names
    v-bind:names="names"
    v-bind:properties="properties"
    v-bind:prices="prices"
    v-on:set_storage="SetStorage"
    />

    <Footer/>
    </div>
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import Loader from '@/components/Loader'
import Names from '@/components/Names'
import Header from '@/components/headers/Header'
import Footer from '@/components/Footer'

export default {
  name: 'App',
  data() {
    return{
      show: false,
      loading: true,
      names: [],
      properties: [],
      prices: []
    }
  },
  mounted() {

    fetch('http://127.0.0.1:8000/main/goods/')
    .then((goods) => goods.json())
    .then((goods) => {
      
      this.names = goods;
    });

    fetch('http://127.0.0.1:8000/main/prop_mobile/')
    .then((props) => props.json())
    .then((props) => {
      
      this.properties = props;
    });

    fetch('http://127.0.0.1:8000/main/prices/')
    .then((prices) => prices.json())
    .then((prices) => {
      setTimeout(() => {
      this.prices = prices;
      this.loading = false;

      },1000)
    });
  },
  components: {
    // HelloWorld
    Loader,
    Header,
    Names,
    Footer,
  },
  methods:{
    SetStorage(id){
      localStorage.setItem('id',id)
      console.log(id)
    }
  }
}
</script>

<style>
#app {
  
}

@import "https://cdn.jsdelivr.net/npm/animate.css@3.5.1";

.page{
  position: fixed;
  width: inherit;
}
.title{
  margin-top: 45px;
  color:chocolate;
  text-align: center;
}
h3{
  color:rgb(209, 209, 209);
  text-align: center;
}
.v-enter-active {
  animation: bounceIn 2s;
}
.v-leave-active{
  animation: bounceIn 2s reverse;
}

@keyframes bounceIn{
  0%{
    transform: scale(0.1);
    opacity: 0;
    }
  60%{
    transform: scale(1.2);
    opacity: 1;
  }
  100%{
    transform:(1);

  }
}
.scroll-off {
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    height: 100%;
    max-height: 100vh;
    overflow: hidden;
    padding-bottom: 1px;
}
</style>