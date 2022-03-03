from django.urls import URLPattern, path
from . import views
app_name = 'learn'

urlpatterns = [
    path('learn',views.learn,name='learn'),
    path('techer',views.teacher,name='techer'),
    path('viewtcr',views.view_techer,name='deatails'),


]