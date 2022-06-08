from django.contrib import admin
from django.urls import path
from eyecolourwheel.quickstart import views

urlpatterns = [
    path('eyeColourWheel/',
         views.EyeColourList.as_view({'get': 'list', 'post': 'create'})),
]
