from django.urls import path, include
from authcart import views
urlpatterns = [
   path('registration', views.register, name="register"),
   path('login', views.login, name="login"),
   path('logout', views.logout, name="logout"),
]