<template>
    <div>

        <div class="products">

        <div class="inline" id="inline">
            
            <div class="item" v-for="(name,index) in names" v-bind:name="name">
                <h1>{{name.good_name}}</h1>
                
                <div>
                <p>screen: {{properties[index].screen}}</p>
                <p>cpu: {{properties[index].cpu}}</p>
                <p>battery: {{properties[index].battery}}</p>
                </div>
                <img width="300px" height="370px" :src="require(`../assets${name.image}`)" >
                <h4>{{prices[index].price_sell}} $</h4>
                
                <router-link :to="'../cart/'+name.id+'/'"><button id="but1" type="button" class="btn btn-warning" v-on:click="$emit('set_storage',name.id)" >buy</button></router-link>
                
            </div>
            
            </div>
        </div>
    </div>
</template>

<script>
// import NamesItem from '@/components/NamesItem'
export default {
    props: ['names','properties','prices'],
    data(){
        return{
            showing: true,
            id: this.$route.name.id
            
        }
    },
    mounted(){
        setTimeout(()=>{
            this.showing = true;
        },1000)
    }
    // methods:{
    // Toggle(){
    //     console.log(this.show);
    //   this.show = true;
    // }
    // components: {
        // NamesItem
    // }
}

</script>

<style>
p{
    font-weight: bold;
}
h4{
    color: white;
    margin-top: 20px;
    padding: 10px;
    border-bottom: 2px solid black;
    text-align: center;
    background: rgba(18,18,29,0.41);
}
</style>>