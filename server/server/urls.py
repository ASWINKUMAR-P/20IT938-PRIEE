from django.contrib import admin
from django.urls import path,include
from django.shortcuts import redirect
from app import urls

urlpatterns = [
    path('', lambda request: redirect('login'), name='redirect_home'),
    path('admin/', admin.site.urls),
    path('',include('app.urls'))
]
