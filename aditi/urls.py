
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage,name='Homepage'),
    path('counts',views.count,name='count'),
    path('about',views.about,name='Aboutpage'),
]
