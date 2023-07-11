from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.home_user, name="home_user"),
    path('register/', views.register_user, name="register"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
]
