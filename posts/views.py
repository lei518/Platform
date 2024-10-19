from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.is_active = False  # Set user as inactive until admin approval
            user.save()
            messages.success(request, 'Registration successful! Please wait for admin approval.')
            return redirect('home')  # Redirect after successful registration
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

def approve_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()
    return redirect('user_approved')


def home(request):
    return render(request, 'home.html')  # Create a home.html template