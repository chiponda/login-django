from django.urls import path

from . import views

urlpatterns = [

    path('', views.homepage, name="home"),

    path('register', views.register, name="register"),

    path('my-login', views.my_login, name="login"),

    path('dashboard', views.dashboard, name="dashboard"),

    path('log-out', views.user_logout, name="logout"),
    
]










