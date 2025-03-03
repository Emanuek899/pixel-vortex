from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("sign-in/", views.user_signup, name="sign-in"),
    path("logout/", LogoutView.as_view(next_page="index"), name="logout"),
]