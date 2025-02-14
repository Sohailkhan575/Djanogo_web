from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse


def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

@login_required(login_url='login')  # Ensure 'login' matches your URL name in urls.py
def contact(request):
    if not request.user.is_authenticated:
        return redirect("login")  # This is redundant but for extra safety

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"New Message from {name} ({email}): {message}")
        return redirect("contact")  # Refresh after submitting

    return render(request, "contact.html")

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            next_page = request.GET.get("next", "contact")  # Redirect to intended page
            return redirect(next_page)
    return render(request, "login.html")


def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=email).exists():
            messages.error(request, "This email is already registered.")
        else:
            user = User.objects.create_user(username=email, password=password, first_name=name)
            user.save()
            login(request, user)
            return redirect(reverse("contact"))  # Redirect after signup
    
    return render(request, "signup.html")

def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect("login")
