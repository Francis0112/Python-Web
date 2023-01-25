from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('hello/', views.hello),
    path('hacker/', views.hackerman),
    path('login/', views.login)
]

