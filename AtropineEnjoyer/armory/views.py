from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
from catalog.models import Character, AllClass


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('archetype')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')

# replaced by IndexArchetypeList
# def user_character_list(request):
#     if request.user.is_authenticated:
#         character_list = Character.objects.filter(owner=request.user.id)
#         return render(request, 'add_character.html', context={'character_list': character_list})
#     else:
#         return 0


def add_character(request):
    all_classes = AllClass.objects.all()
    return render(request, 'add_character.html', {'all_classes': all_classes})
