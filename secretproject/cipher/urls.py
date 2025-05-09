# cipher/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Bosh sahifa (home view)
    path('sezar/', views.sezar, name='sezar'),
    path('vejiner/', views.vejiner, name='vejiner'),
    path('hill/', views.hill, name='hill'),
    path('affine/', views.affine_cipher, name='affine_cipher'),  # Affine Cipher sahifasi
    path('about_algorithms/', views.about_algorithms, name='about_algorithms'),
    path('sezor/', views.caesar_view, name='caesar'),
    path('vejiner1/', views.vigenere_view, name='vigenere'),
    path('hill1/', views.hill_algorithm_detail, name='hill_algorithm_detail'),
    path('affin/', views.affine_view, name='affine'),
    path('about_algorithms/', views.about_algorithms_view, name='about_algorithms'),
]

