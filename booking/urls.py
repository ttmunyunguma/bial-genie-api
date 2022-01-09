from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookingsView.as_view()),
]
