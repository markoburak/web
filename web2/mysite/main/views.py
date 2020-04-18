from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import product_typeSerializers, goodsSerializers, prop_laptopSerializers, prop_mobileSerializers, \
    pricesSerializers, counterpartiesSerializers

from .models import Product_type, Goods, Prop_mobile, Prop_laptop, Prices, Counterparties


def index(request, ):
    # films = Prop_laptop.objects.all()
    # films = Prop_laptop.objects.get(goods_id=4)
    # for film in films:
    #     print(film)
    #     print(film.screen)
    #     print(film.cpu)
    #     print(film.video_card)
    #     print(film.ram)
    # goods = Goods.objects.all()

    # good = Goods.objects.get(id =1)
    goods =Goods.objects.all()
    properties = Prop_mobile.objects.all()
    prices =Prices.objects.all()
    content = {}
    for i in range(1,len(goods)+1):
        content['id'+str(i)] =goods[i-1]
        content['id' + str(i)+'prop'] = properties[i - 1]
        content['id' + str(i) + 'price'] = prices[i - 1]
    print(content['id2'])
    return render(request, 'main/index.html', content)


def cart(request):
    return render(request, 'main/pages/cart.html')

def cart_pk(request, pk):
    goods = Goods.objects.get(id = pk)

    price = Prices.objects.get(goods_id= pk)

    content = {
        'object1': goods,
        'object2' : price
    }
    return render(request, 'main/pages/cart.html',content)

def login(request):
    return render(request, 'main/pages/login.html')


def contact(request):
    return render(request, 'main/pages/contact.html')


def signup(request):
    return render(request, 'main/pages/register.html')


def general_get_post(request, class_name, serializer_name):
    if request.method == 'GET':
        obj = class_name.objects.all()
        serializer = serializer_name(obj, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serelizer = serializer_name(data=request.data)
        if serelizer.is_valid() :
            serelizer.save()
            return Response(serelizer.data,status =status.HTTP_201_CREATED)
        return Response(serelizer.errors,status.HTTP_400_BAD_REQUEST)


def general_get_put_delete(request,attr, class_name, serializer_name):
    try:
        obj =class_name.objects.get(pk= attr)
    except:
        return HttpResponse(status= status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(serializer_name(obj).data)
    elif request.method == 'PUT':
        serializer = serializer_name(obj,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        obj.delete()
        return Response(status = status.HTTP_200_OK)

# ------------------------------
# product_type
# ------------------------------
@api_view(['GET', 'POST'])
def get_post_product_type(request):
    return general_get_post(request, Product_type, product_typeSerializers)

@api_view(['GET', 'PUT', 'DELETE'])
def get_put_delete_product_type(request, pk):
    return general_get_put_delete(request,pk, Product_type, product_typeSerializers)


# ------------------------------
# goods
# ------------------------------
@api_view(['GET', 'POST'])
def get_post_goods(request):
    return general_get_post(request, Goods, goodsSerializers)

@api_view(['GET', 'PUT', 'DELETE'])
def get_put_delete_goods(request, pk):
    return general_get_put_delete(request,pk, Goods, goodsSerializers)


# ------------------------------
# properties laptop
# ------------------------------
@api_view(['GET', 'POST'])
def get_post_prop_laptop(request):
    return general_get_post(request, Prop_laptop, prop_laptopSerializers)

@api_view(['GET', 'PUT', 'DELETE'])
def get_put_delete_prop_laptop(request, pk):
    return general_get_put_delete(request,pk, Prop_laptop, prop_laptopSerializers)

# ------------------------------
# properties mobile
# ------------------------------
@api_view(['GET', 'POST'])
def get_post_prop_mobile(request):
    return general_get_post(request, Prop_mobile, prop_mobileSerializers)

@api_view(['GET', 'PUT', 'DELETE'])
def get_put_delete_prop_mobile(request, pk):
    return general_get_put_delete(request,pk, Prop_mobile, prop_mobileSerializers)


# ------------------------------
# prices
# ------------------------------
@api_view(['GET', 'POST'])
def get_post_prices(request):
    return general_get_post(request, Prices, pricesSerializers)

@api_view(['GET', 'PUT', 'DELETE'])
def get_put_delete_prices(request, pk):
    return general_get_put_delete(request,pk, Prices, pricesSerializers)


# ------------------------------
# counterparties
# ------------------------------
@api_view(['GET', 'POST'])
def get_post_counterparties(request):
    return general_get_post(request, Counterparties, counterpartiesSerializers)

@api_view(['GET', 'PUT', 'DELETE'])
def get_put_delete_counterparties(request, pk):
    return general_get_put_delete(request,pk, Counterparties, counterpartiesSerializers)






