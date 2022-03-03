from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('home',views.home),
    path('alpha',views.alpha),
    path('login',views.login),
    path('su',views.su),


]