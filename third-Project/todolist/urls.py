from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.menu, name="menu"),
    path('detail/<int:todo_id>/', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('update/<int:todo_id>/', views.update, name="update"),
    path('delete/<int:todo_id>/', views.delete, name="delete"),
]
