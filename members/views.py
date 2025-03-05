from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models

# Create your views here.
def user_login(request):
    errors = {}
    if request.method == "POST":
        # take the email and password from the form
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Checks if the user email already exist 
        try:
            user = models.CustomUser.objects.get(email=email)
        except models.CustomUser.DoesNotExist:
            user = None

        # If user exist then login in the page
        if user is not None and user.check_password(password):
            login(request, user)
            return redirect("index")
        else:
            errors["invalid"] = "Email or password incorrect"

    return render(request, "members/login.html", {"errors": errors})

def user_signup(request):
    errors = {}
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # If the user email already exist, then is an error
        if models.CustomUser.objects.filter(email=email).exists():
            errors["email"] = "Email already in use"

        # If the username already exist, then is an error
        if models.CustomUser.objects.filter(username=username).exists():
            errors["username"] = " Username already exist"

        if errors:
            return render(request, "members/signup.html", {"errors": errors})
        
        user = models.CustomUser.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
        messages.success(request, "succes you now will be redirected to the login page")
        return redirect("login")
    
    else:       
        return render(request, "members/signup.html", {"errors": errors})