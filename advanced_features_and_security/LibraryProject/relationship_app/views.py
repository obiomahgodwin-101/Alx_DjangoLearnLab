from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import CustomUser


# ---------------------------
# Registration Form
# ---------------------------
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password')
        p2 = cleaned_data.get('password2')

        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data


# ---------------------------
# Register View
# ---------------------------
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            CustomUser.objects.create_user(email=email, password=password)
            messages.success(request, "Account created! You can now log in.")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


# ---------------------------
# Login View
# ---------------------------
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('username')  # NOTE: username holds email in this form
            password = form.cleaned_data.get('password')

            user = authenticate(request, email=email, password=password)

            if user:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('register')  # change to your home page later
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Invalid form submission.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


# ---------------------------
# Logout View
# ---------------------------
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')

