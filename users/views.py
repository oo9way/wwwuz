from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Ro'yxatdan o'tdingiz")
            return redirect(reverse("app:home"))
        messages.error(request, "Qaytadan urining", extra_tags='danger')

    form = RegistrationForm()
    return render(request, 'registration.html', {'form':form})


def sign_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Hisobingizga muvaffaqiyatli kirildi')
                return redirect(reverse("app:home"))
            else:
                messages.error(request, "Login yoki parol xato")
        else:
            messages.error(request, "Login yoki parol xato")
    
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})


def sign_out(request):
    logout(request)
    messages.info(request, 'Hisobingizdan chiqildi')
    return redirect('app:home')