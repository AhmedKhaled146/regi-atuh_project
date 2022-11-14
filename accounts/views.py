from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, UserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.


# @login_required(login_url='login')
def index(request):
    return render(request, 'home/index.html')

def Register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created successfully for " + user)
            user = authenticate(request, user=user)
            # login(request, user)
            return redirect('accounts:login')
    else:
        form = CreateUserForm()

    context = {'form': form,
               'title': "register",}
    return render(request, 'registration/register.html', context)

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('accounts:profile')
        else:
            messages.info(request, "Username or Password is Incorrect")

    context={'title': 'Login',}
    return render(request, 'registration/login.html', context)


@login_required(login_url = '/login/')
def profile_user(request):
    profile = Profile.objects.get(user=request.user)


    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile )
        user_form = UserForm(request.POST, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            # myprofile = profile_form.save(commit=False)
            # myprofile.user = request.user
            # myprofile.save()
            profile_form.save()

    else:
        profile_form = ProfileForm(instance=profile )
        user_form = UserForm(instance=request.user)

    context = {'title': 'Profile',
               'user_form': user_form,
               'profile_form': profile_form,
               'profile': profile,}

    return render(request, 'registration/profile.html', context)

@login_required(login_url = '/login/')
def Logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html')
