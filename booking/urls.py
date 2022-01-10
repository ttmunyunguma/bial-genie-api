from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookingsView.as_view()),
    path('locations/', views.LocationView.as_view()),
    path('flights/', views.LocationView.as_view()),

]
