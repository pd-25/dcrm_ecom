from django.urls import path, include
from dcrm import views
urlpatterns = [
   path('', views.index, name="home"),
   path('contact', views.contact, name="contact"),
]