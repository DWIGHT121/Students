from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.info, name='infor'),
    path('login/', views.login, name="login"),
]
