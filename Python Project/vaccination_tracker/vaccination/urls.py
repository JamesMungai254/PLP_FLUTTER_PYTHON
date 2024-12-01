from django.urls import path
from . import views

app_name = 'vaccination' 

urlpatterns = [
    path('', views.record_list, name='record_list'),
    path('add/', views.add_record, name='add_record'),
]
