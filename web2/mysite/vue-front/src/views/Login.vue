<template>

  <div class=".page">
    <HeaderLogin/>
    <Loader2 v-if="loader"/>
    <div id="page-container" v-else>
		<div id="content-wrap">
				<div class="loginbox">
          	<img src="../assets/images/account.png" class="avatar">
            <div>
            <h1 @click="show = !show">Login Here</h1>
            </div>
            <transition>
              <div v-if="show">
             <form action="">
							<p>Username</p>
							<input  type="text" name="" placeholder="Enter Username">
							<p>Password</p>
							<input type="text" name="" placeholder="Enter Password">
							<input type="submit" name="" value="Login">
							<a href="../signup">Register</a><br>
						</form>
              </div>
            </transition>
            
				</div>
		</div>
    </div>
    <Footer/>
  </div>
</template>

<script>
import Loader2 from '@/components/Loader2'
import HeaderLogin from '@/components/headers/HeaderLogin'
import Footer from '@/components/Footer'
export default {
  data() {
    return{
      show:false,
      loader : true
    }
  },
  mounted() {
    setTimeout(() =>{
      this.loader = false;
    },500)
    
  },
  components: {
    Loader2,
    HeaderLogin,
    Footer,
  }
}
</script>

<style>

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

.page{
  position: fixed;
  width: inherit;
}
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

body {
  background: #1f2232 !important;
}

body .loginbox {
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

body .loginbox p {
  margin: 0;
  padding: 0;
  font-weight: bold;
}

body .loginbox input {
  width: 100%;
  margin-bottom: 20px;
}

body .loginbox input[type="text"], body .loginbox input[type="password"] {
  border: none;
  border-bottom: 1px solid #fff;
  background: transparent;
  outline: none;
  height: 40px;
  color: #fff;
  font-size: 16px;
}

body .loginbox input[type="submit"] {
  border: none;
  outline: none;
  height: 40px;
  background: #ff9810;
  color: #fff;
  font-size: 18px;
  border-radius: 20px;
}

body .loginbox input[type="submit"]:hover {
  cursor: pointer;
  background: #1f2232;
  color: white;
}

body .loginbox a {
  text-decoration: none;
  font-size: 12px;
  line-height: 20px;
  color: grey;
}

body .loginbox a:hover {
  color: #ffc107;
}

body .avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  position: absolute;
  top: -50px;
  left: calc(35%);
}

body h1 {
  margin: 0;
  padding: 0 0 20px;
  text-align: center;
  font-size: 22px;
}

body #page-container {
  position: relative;
  min-height: 100vh;
}



</style>