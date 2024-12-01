from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import ParentSignUpForm, FacilitatorSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import ChildRegistrationForm

def parent_signup(request):
    if request.method == 'POST':
        form = ParentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('vaccination:record_list')  # Use the namespace
    else:
        form = ParentSignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def facilitator_signup(request):
    if request.method == 'POST':
        form = FacilitatorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('vaccination:record_list')  # Use the namespace
    else:
        form = FacilitatorSignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


# Custom login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('vaccination:record_list')  # Redirect to the desired page after login
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# Register child view

def register_child(request):
    if request.method == 'POST':
        form = ChildRegistrationForm(request.POST)
        if form.is_valid():
            child = form.save(commit=False)
            child.parent = request.user.parent  # Assuming the user is a parent
            child.save()
            return redirect('vaccination:record_list')  # Redirect to where you want after saving
    else:
        form = ChildRegistrationForm()
    
    return render(request, 'registration/register_child.html', {'form': form})
