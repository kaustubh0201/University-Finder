from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('products/', views.product, name = "products"),
    path('customer/<str:pk_test>/', views.customer, name = "customer"),

    path('create_order/<str:pk>/', views.create_order, name = "create_order"),
    path('update_order/<str:pk>/', views.update_order, name = "update_order"),
    path('delete_order/<str:pk_t>/', views.delete_order, name = "delete_order"),
    path('login/', views.loginPage, name = "login"),
    path('logout/', views.logoutUser, name = 'logout'),
    path('register/', views.registerPage, name = "register"),
    path('user/', views.userPage, name = "user-page"),


    
]