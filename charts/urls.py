from django.contrib import admin
from django.urls import path
from chartjs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name= 'home'),
    path('index', views.IndexView.as_view(),name= 'graphs'),
    path('test-api', views.get_data),
]
