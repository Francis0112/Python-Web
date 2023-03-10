
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
    path("add_cars/", views.add_cars),
    path("view_cars/<int:car_id>/", views.view_car_details),
    path("view_cars/update_car/<int:car_id>/", views.update_car),
    path("display_products/", views.display_products),
    path("display_cars/", views.display_cars),
    path("delete_car/<int:car_id>/", views.delete_car),
    path("delete_product/<int:prod_id>/", views.delete_product),
    path("message/", views.msg),
    path("get_values", views.get_values),
    path("web_api", views.web_api),
    path("weather_api", views.weather_api),
    path("circle_area", views.circle_area),
    path("air_quality_api", views.air_quality_api),
    path("geocoding_api", views.geocoding_api)
]