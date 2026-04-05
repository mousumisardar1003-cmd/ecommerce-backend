from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after registration
            return redirect("home")  # redirect to homepage
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})


@login_required
def profile(request):
    return render(request, "profile.html", {"user": request.user})
