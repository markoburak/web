<template>

  <div>
    <HeaderContact/>
    <Loader3 v-if="load"/>
    <div v-else>
    <div id="page-container">
		<div id="content-wrap">
				<div class="contactbox">
						<img src="../assets/images/contact.png" class="avatar">
						<h1>Contacts:</h1>
						<h3>burakmarko@gmail.com</h3>
						<div class="im_cen">
							<a href="https://t.me/Mark0_0"><img src="../assets/images/telegram.png" alt=""></a><br>
							<a href="https://www.facebook.com/profile.php?id=100008011452308"><img src="../assets/images/facebook.png" alt=""></a><br>
							<a href="https://www.instagram.com/0_0mark0_0/?hl=uk"><img src="../assets/images/insta.png" alt=""></a><br>
						</div>
					</div>
		</div>
    </div>
    <Footer/>
    </div>
  </div>
</template>

<script>
import Loader3 from '@/components/Loader3'
import HeaderContact from '@/components/headers/HeaderContact'
import Footer from '@/components/Footer'
export default {
    data() {
    return{
      load : true
    }
  },
  mounted() {
    setTimeout(() =>{
      this.load = false;
    },2000)
    
  },
  components: {
    // HelloWorld
    Loader3,
    HeaderContact,
    Footer,
  }
}
</script>

<style>


@media only screen and (min-width: 600px) {
  .contactbox {
    display: inline;
  }
}

@media (max-width: 700px) {
  .inline1 {
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
        -ms-flex-direction: column;
            flex-direction: column;
    -webkit-box-align: center;
        -ms-flex-align: center;
            align-items: center;
  }
  .inline1 .forma_for_buy {
    position: relative;
  }
  .inline1 .item {
    border: 2px solid crimson;
    position: relative;
  }
  .inline1 .item img {
    width: 10%;
  }
}

@media (max-width: 700px) {
  .inline {
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
        -ms-flex-direction: column;
            flex-direction: column;
    -webkit-box-align: center;
        -ms-flex-align: center;
            align-items: center;
  }
  .item {
    margin: 0;
    margin-bottom: 25px;
  }
  .item:last-child {
    margin-bottom: 0;
  }
}


.contactbox {
  width: 320px;
  height: 420px;
  background: #000000;
  color: #ffffff;
  top: 50%;
  left: 50%;
  position: absolute;
  -webkit-transform: translate(-50%, -50%);
          transform: translate(-50%, -50%);
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  padding: 70px 30px;
}

.contactbox h1 {
  border-bottom: 2px solid #ff9810;
  padding: 3px;
}

.contactbox h3 {
  border-bottom: 1px solid #ff9810;
  color: #ff9810;
}

.contactbox h3:hover {
  background: grey;
  color: honeydew;
}

.contactbox a img {
  padding: 5px;
  border: 1px solid #ff9810;
  width: 50px;
  margin: 20px;
}

.contactbox .im_cen {
  left: 35%;
  position: absolute;
  top: 40%;
}

.avatar {
  width: 130px;
  position: absolute;
  top: -50px;
  left: calc(30%);
}

h1 {
  margin: 0;
  padding: 0 0 20px;
  text-align: center;
  font-size: 22px;
}

#page-container {
  position: relative;
  min-height: 100vh;
}

#content-wrap {
  padding-bottom: 2.5rem;
  /* Footer height */
}


</style>