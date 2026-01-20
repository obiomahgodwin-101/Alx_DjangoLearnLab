from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # LOGIN after registration
            return redirect("login")
        else:
            messages.error(request, "Registration failed. Please check your details.")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # LOGIN
            return redirect("login")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")

