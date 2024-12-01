

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def index(request):
    return render(request, 'index.html') 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'), 
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('vaccination/', include('vaccination.urls', namespace='vaccination')),
    path('accounts/', include('django.contrib.auth.urls')),
]
