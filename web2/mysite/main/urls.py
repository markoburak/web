from django.urls import path, include
from . import views

urlpatterns = [
	path('',views.index,name ='index'),

	path('cart/id/<int:pk>/', views.cart_pk, name='cart'),

	path('login/', views.login, name='login'),

	path('contact/', views.contact, name='contact'),

	path('signup/', views.signup, name='signup'),

	path('goods/', views.get_post_goods),

	path('goods/id/<int:pk>/', views.get_put_delete_goods),

	path('product_type/', views.get_post_product_type),

	path('product_type/id/<int:pk>/', views.get_put_delete_product_type),

	path('prop_laptop/', views.get_post_prop_laptop),

	path('prop_laptop/id/<int:pk>/', views.get_put_delete_prop_laptop),

	path('prop_mobile/', views.get_post_prop_mobile),

	path('prop_mobile/id/<int:pk>/', views.get_put_delete_prop_mobile),

	path('prices/', views.get_post_prices),

	path('prices/id/<int:pk>/', views.get_put_delete_prices),

	path('counterparties/', views.get_post_counterparties),

	path('counterparties/id/<int:pk>/', views.get_put_delete_counterparties),

]
