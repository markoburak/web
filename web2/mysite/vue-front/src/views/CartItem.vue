<template>

  <div>
    
    <HeaderCartItem/>
    
    	<div class="products">

			<div class="inline1">
				<div class="item">
<!--					{{object1.good_name}}-->
                        
					<h1 id="name">{{names[id].good_name}}</h1>
<!--					{{object2.price_sell}}-->
					<p id="price">{{prices[id].price_sell}}$</p>
						<div class="prod_img">
<!--							'/static{{object1.image}}'-->
							<img width="300px" height="370px" :src="require(`../assets${names[id].image}`)" >
						</div>

				</div>
				<div class="forma_for_buy">
					<form action="">
						<h1>Full Name</h1>
						<input type="text" name="" placeholder="Full name">
						<h1>Email</h1>
						<input type="text" name="" placeholder="Enter Email">
						<br>
						<button type="button" class="btn btn-warning">buy</button>

					</form>

				</div>
			</div>
		</div>
    
     
  </div>
</template>

<script>
import HeaderCartItem from '@/components/headers/HeaderCartItem'
export default {
    data() {
    return{
      loading : true,
      id: 0,
      names: [],
      prices: []
    }
  },
  mounted() {
    this.id = localStorage.id -1;
    fetch('http://127.0.0.1:8000/main/goods/')
    .then((goods) => goods.json())
    .then((goods) => {
      
      this.names = goods;
    });


    fetch('http://127.0.0.1:8000/main/prices/')
    .then((prices) => prices.json())
    .then((prices) => {
      this.prices = prices;
      this.loading = false;

    });
  },
    components: {
    // HelloWorld
    HeaderCartItem,
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

body {
  background: #1f2131 !important;
}

body .products {
  padding-top: 70px;
  padding-bottom: 70px;
}

body .products .inline1 {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
      -ms-flex-pack: justify;
          justify-content: space-between;
  margin-bottom: 40px;
}

body .products .inline1:last-child {
  margin-bottom: 0;
}

body .products .inline1 .item {
  position: absolute;
  left: 17%;
  top: 20%;
  padding-top: 30px;
  padding-right: 20px;
  padding-bottom: 30px;
  padding-left: 20px;
  border: 4px solid #ff9810;
}

body .products .inline1 .item h1 {
  color: white;
  font-family: 'Courier New', Courier, monospace;
}

body .products .inline1 .item p {
  color: #919191;
}

body .products .inline1 .item .prod_img img {
  width: 300px;
  height: 370px;
}

@media (max-width: 700px) {
  body .products .inline1 .item {
    margin-top: 60px;
    position: absolute;
    top: 20%;
    left: 3%;
    padding-top: 30px;
    padding-right: 20px;
    padding-bottom: 30px;
    padding-left: 20px;
    border: 4px solid #ff9810;
  }
  body .products .inline1 .item h1 {
    color: white;
    font-family: 'Courier New', Courier, monospace;
  }
  body .products .inline1 .item p {
    color: #919191;
  }
  body .products .inline1 .item .prod_img img {
    width: 300px;
    height: 370px;
  }
}

body .products .inline1 .forma_for_buy {
  position: absolute;
  left: 58%;
  top: 20%;
}

body .products .inline1 .forma_for_buy h1 {
  color: cornsilk;
}

body .products .inline1 .forma_for_buy input {
  width: 100%;
  margin-bottom: 20px;
}

body .products .inline1 .forma_for_buy input[type="text"] {
  border: none;
  border-bottom: 1px solid #fff;
  background: transparent;
  outline: none;
  height: 40px;
  color: #fff;
  font-size: 16px;
}

body .products .inline1 .forma_for_buy button {
  margin-top: 40px;
}

@media (max-width: 700px) {
  body .products .inline1 .forma_for_buy {
    margin-top: 200px;
    margin-bottom: 180px;
    position: absolute;
    top: 99%;
    left: 10%;
  }
  body .products .inline1 .forma_for_buy h1 {
    color: cornsilk;
  }
  body .products .inline1 .forma_for_buy input {
    width: 100%;
    margin-bottom: 20px;
  }
  body .products .inline1 .forma_for_buy input[type="text"] {
    border: none;
    border-bottom: 1px solid #fff;
    background: transparent;
    outline: none;
    height: 40px;
    color: #fff;
    font-size: 16px;
  }
  body .products .inline1 .forma_for_buy button {
    margin-top: 40px;
  }
}


body #page-container {
  position: relative;
  min-height: 100vh;
}

body #content-wrap {
  padding-bottom: 2.5rem;
  /* Footer height */
}

body #footer {
  position: absolute;
  bottom: -100px;
  width: 100% !important;
  height: 14%;
  /* Footer height */
  background: black !important;
}

@media (max-width: 700px) {
  body #footer {
    bottom: -800px;
  }
}

body #footer .images {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: center;
      -ms-flex-pack: center;
          justify-content: center;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
}

body #footer .images img {
  width: 35px;
  margin: 12px;
}

body #footer .credits {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: center;
      -ms-flex-pack: center;
          justify-content: center;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  color: white;
}

#footer{
    position: absolute;
    top: 100%;
}

</style>