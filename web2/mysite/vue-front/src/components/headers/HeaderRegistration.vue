<template>
    
<header>
    <div class="container">
        <ul>
            <li><router-link to="../"><img src="../../assets/images/laptoplogo.png" class="logo" alt="laptop"></router-link></li>
            <li><router-link to="../"><b/>Home</router-link></li>
            <li>
                <router-link to="../login/"><b/>Login</router-link>
            </li>
            <li>
                <router-link to="../contact/"><b/>Contact</router-link>
            </li>
            <li><router-link to="../signup/" class="btn"><span>Sign up</span></router-link></li>
        </ul>
    </div>
</header>
</template>

<style>
li{
    font-weight: bold;
}
</style>