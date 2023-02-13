
from django.urls import path
from . import views

urlpatterns = [
    path('wakaru/', views.wakaru),
    path('hello/', views.hello),
    path('send/', views.send),
    path('about/', views.about),
    path('pizza/', views.pizza),
    path("view_products/<int:prod_id>/", views.view_product_details),
    path("add_product/", views.add_product),
    path("search/", views.search),
    path("add_cars/", views.add_cars),
    path("view_cars/<int:car_id>/", views.view_car_details),
    path("display_products/", views.display_products),
    path("display_cars/", views.display_cars),
    path("delete_car/<int:car_id>/", views.delete_car),
    path("delete_product/<int:prod_id>/", views.delete_product),
    path("message/", views.msg)
]

