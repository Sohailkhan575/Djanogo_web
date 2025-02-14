from django.contrib import admin
from django.urls import path
from home import views
from .views import contact, login_view, signup, logout_view



urlpatterns = [
    path('',views.home, name='home'),
    path('home',views.home, name='home'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path("login/",views.login_view, name="login"),
    path("signup/",views.signup, name="signup"),
    path('logout/',views.logout_view, name='logout'),

]