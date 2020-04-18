const headers = {
    'Content-Type': 'application/json',
};
const button_list = [];
const start_link = 'http://127.0.0.1:8000/main/'



fetch('http://127.0.0.1:8000/main/goods/')
    .then(goods => {
        console.log(goods);
        return goods.json()
    })
    .then(goods => {
        for (let i = 1; i < goods.length + 1; i += 1) {
            document.getElementById("name" + String(i)).innerHTML = goods[i - 1].good_name;
            document.getElementById("img" + String(i)).src = '/static' + goods[i - 1].image;
            document.getElementById("link" + String(i)).href = 'cart/id/' + goods[i - 1].id;
            button_list.push(goods[i - 1].id);

        }

        function getAttribute(locId) {
            goodId = locId;
            localStorage.setItem('id', goodId);
        }


        const buttons_link = document.querySelectorAll('.btn-warning');

        let goodId = '';

        for (let i = 0; i < buttons_link.length; i += 1) {
            buttons_link[i].onclick = function() {
                getAttribute(button_list[i]);
            }

        }


    });
fetch('http://127.0.0.1:8000/main/prop_mobile/')
    .then(props => {
        console.log(props);
        return props.json()
    })
    .then(props => {

        for (let i = 1; i < props.length + 1; i += 1) {
            document.getElementById('screen' + String(i)).innerHTML = 'screen: ' + props[i - 1].screen;
            document.getElementById('cpu' + String(i)).innerHTML = "cpu: " + props[i - 1].cpu;
            document.getElementById('battery' + String(i)).innerHTML = "battery: " + props[i - 1].battery;

        }


    });
fetch('http://127.0.0.1:8000/main/prices/')
    .then(prices => {
        console.log(prices)
        return prices.json()
    })
    .then(prices => {
        for (let i = 1; i < prices.length + 1; i += 1) {
            document.getElementById('price' + String(i)).innerHTML = String(prices[i - 1].price_sell) + ' ₴';
        }
    });