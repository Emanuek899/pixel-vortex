from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("sign-in/", views.user_signup, name="sign-in")
]