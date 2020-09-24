from django.shortcuts import render

urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
]