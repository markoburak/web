const headers = {
    'Content-Type': 'application/json',
};


const Itemid = localStorage.getItem('id');
console.log(Itemid)

fetch('http://127.0.0.1:8000/main/goods/id/' + Itemid)
    .then(cart => {
        console.log(cart);
        return cart.json()
    })
    .then(cart => {
        document.getElementById('name').innerHTML = cart.good_name;
        document.getElementById('img').src = '/static' + cart.image;

    });

fetch('http://127.0.0.1:8000/main/prices/')
    .then(price => {
        console.log(price);
        return price.json();
    })
    .then(price => {
        var obj;
        console.log(price)
        for (let i = 0; i < price.length; i += 1) {
            if (String(price[i].good_name2.id) === Itemid) {
                document.getElementById('price').innerHTML = price[i].price_sell + ' ₴';
            }
        }
    })