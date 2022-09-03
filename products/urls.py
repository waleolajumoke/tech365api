from django.urls import path
from products import views

urlpatterns = [
    path('api/v1/all-products', views.home, name='home'),
    path('', views.index, name='index'),
]
