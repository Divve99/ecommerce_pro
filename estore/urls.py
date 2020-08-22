from django.urls import path
from estore import views

urlpatterns = [
    path('', views.home, name="home"),
    path('', views.contact, name='contact')
]