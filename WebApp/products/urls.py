
from django.urls import path
from . import views


urlpatterns = [
    path('wakaru/', views.wakaru),
    path('hello/', views.hello),
    path('send/', views.send),
    path('about/', views.about),
    path('pizza/', views.pizza),
    path("product/", views.view_product_details),
    path("add/", views.add_product),
    path("search/", views.search),
    path("add_cars/", views.add_cars)
]

