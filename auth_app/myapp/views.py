from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm

# Create your views here.
def login_user(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in.')
            return render(request, 'main.html')

        else:
            messages.error(request, 'Invalid Logs')


    return render(request, 'home.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return render(request, 'main.html')


def register_user(request):
        if request.method == 'POST':
            # send everything in the post request to the signup form
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                # authenticate and login newly created user
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(request, username=username, password=password)
                login(request, user)
                messages.success(request, 'Congrats you have signed up successfully')
                return render(request, 'main.html')
        form = SignUpForm()
        context_dictionary = {'form': form}
        return render(request, 'register.html', context_dictionary)
