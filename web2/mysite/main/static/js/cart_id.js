const Itemid = localStorage.getItem('id');


fetch(`http://127.0.0.1:8000/main/goods/id/${Itemid}`)
    .then((cart) => cart.json())
    .then((cart) => {
        document.getElementById('name').innerHTML = cart.good_name;
        document.getElementById('img').src = `/static${cart.image}`;
    });

fetch('http://127.0.0.1:8000/main/prices/')
    .then((price) => price.json())
    .then((price) => {
        for (let i = 0; i < price.length; i += 1) {
            if (String(price[i].good_name2.id) === Itemid) {
                document.getElementById('price').innerHTML = `${price[i].price_sell} ₴`;
            }
        }
    });
