
from django.contrib import admin
from django.urls import path
from height.views import showResult
urlpatterns = [
    path('',showResult)
]
