from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", views.signup, name="signup"),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('my-blogs/', views.UserBlogsListView.as_view(), name='my-blogs'),
]
