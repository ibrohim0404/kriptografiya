# secretproject/urls.py

from django.contrib import admin
from django.urls import path, include  # include to'g'ri import qilinganini tekshiring

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cipher.urls')),  # cipher app'ining URL'larini uladik
]
