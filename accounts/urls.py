from django.urls import path

from accounts import views

urlpatterns = [
    path('<int:pk>/', views.UserRetrieveUpdateDestroyView.as_view()),
    path('login/', views.UserLoginView.as_view()),
    path('logout/', views.UserLogoutView.as_view()),
    path('', views.UserListCreateView.as_view()),
]
