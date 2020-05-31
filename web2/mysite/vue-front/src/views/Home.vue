<template>
  <div>
    <!-- <Names/> -->

    <Header/>
    <Names
    v-bind:names="names"
    v-bind:properties="properties"
    v-bind:prices="prices"
    v-on:set_storage="SetStorage"
    />

    <Footer/>

    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import Names from '@/components/Names'
import Header from '@/components/headers/Header'
import Footer from '@/components/Footer'
export default {
  name: 'App',
  data() {
    return{
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
       
      this.prices = prices;
    });
  },
  components: {
    // HelloWorld
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
</style>