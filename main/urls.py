from django.urls import path

from . import views

app_name = 'main'


urlpatterns = [
    path('resume/', views.resume, name='resume'),
    path('contact/', views.contact, name='contact'),
    path('', views.index, name='index'),
]
