from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('hello/', views.hello),
    path('hackerman/', views.hackerman),
    path('login/', views.login),
    path('add/', views.add)
]

