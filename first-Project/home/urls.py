from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:animal_id>', views.read, name='details'),
    path('delete/<int:animal_id>', views.delete, name="delete"),
    path('update/<int:animal_id>', views.update, name="update"),
    path('create/', views.create, name="create"),
]   
