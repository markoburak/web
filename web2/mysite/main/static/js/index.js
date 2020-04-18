const ButtonList = [];


fetch('http://127.0.0.1:8000/main/goods/')
    .then((goods) => goods.json())
    .then((goods) => {
        for (let i = 1; i < goods.length + 1; i += 1) {
            document.getElementById(`name${String(i)}`).innerHTML = goods[i - 1].good_name;
            document.getElementById(`img${String(i)}`).src = `/static${goods[i - 1].image}`;
            document.getElementById(`link${String(i)}`).href = `cart/id/${goods[i - 1].id}`;
            ButtonList.push(goods[i - 1].id);
        }

        function getAttribute(locId) {
            localStorage.setItem('id', locId);
        }


        const ButtonsLink = document.querySelectorAll('.btn-warning');

        for (let i = 0; i < ButtonsLink.length; i += 1) {
            ButtonsLink[i].onclick = function () {
                getAttribute(ButtonList[i]);
            };
        }
    });
fetch('http://127.0.0.1:8000/main/prop_mobile/')
    .then((props) => props.json())
    .then((props) => {
        for (let i = 1; i < props.length + 1; i += 1) {
            document.getElementById(`screen${String(i)}`).innerHTML = `screen: ${props[i - 1].screen}`;
            document.getElementById(`cpu${String(i)}`).innerHTML = `cpu: ${props[i - 1].cpu}`;
            document.getElementById(`battery${String(i)}`).innerHTML = `battery: ${props[i - 1].battery}`;
        }
    });
fetch('http://127.0.0.1:8000/main/prices/')
    .then((prices) => prices.json())
    .then((prices) => {
        for (let i = 1; i < prices.length + 1; i += 1) {
            document.getElementById(`price${String(i)}`).innerHTML = `${String(prices[i - 1].price_sell)} ₴`;
        }
    });
