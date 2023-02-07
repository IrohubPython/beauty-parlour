from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('user_login',views.user_login,name='user_login'),
    path('userlogout',views.userlogout,name='userlogout'),
    path('user_register',views.user_register,name='user_register'),
    path('register_user',views.register_user,name='register_user'),
    path('branches/',views.branches,name='branches'),
    path('services/<str:branchname>/',views.services,name='services'),
    path('contact',views.contact,name='contact'),
    path('cart/',views.cart,name='cart'),
    path('cart_data/<int:sid>/',views.cart_data,name='cart_data'),
    path('cart_delete/<int:cartid>/',views.cart_delete,name='cart_delete'),
    path('checkout',views.checkout,name='checkout'),
    path('checkout_data',views.checkout_data,name='checkout_data'),



]