
from django.urls import path
from . import views


urlpatterns = [
    path('wakaru/', views.wakaru),
    path('hello/', views.hello),
    path('send/', views.send),
    path('about/', views.about)
]

