<template>
    
<header>
    <div class="container">
        <ul>
            <li><img src="../../assets/images/cart.png"  class="cart"></li>
            <li><img src="../../assets/images/laptoplogo.png" class="logo" alt="laptop"></li>
            <li><b/>Home</li>
            <li>
                <router-link to="login/"><b/>Login</router-link>
            </li>
            <li>
                <router-link to="contact/"><b/>Contact</router-link>
            </li>
            <li><router-link to="signup/" class="btn"><span>Sign up</span></router-link></li>
        </ul>
    </div>
</header>
</template>

<style>
li{
    font-weight: bold;
}
</style>