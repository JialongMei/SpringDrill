from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
from catalog.models import Character, AllClass
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import AccessToken


def user_login(request):
    if request.method == 'POST':
        access_token = request.headers.get('Authorization')
        print(access_token)
        if access_token:
            try:
                print(111)
                # Validate the access token
                access_token_obj = AccessToken(access_token)
                print(222)
                user = access_token_obj.payload.get('user_id')
                print(user)
                print(111)
                if user is not None:
                    # If the access token is valid, log in the user
                    login(request, user)
                    return JsonResponse({'message': 'Login successful'})
                else:
                    return JsonResponse({'error': 'Invalid access token'}, status=400)
            except TokenError:
                return JsonResponse({'error': 'Invalid access token'}, status=400)

        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                refresh = RefreshToken.for_user(user)

                return JsonResponse(
                    {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token)
                    }
                )
                # return redirect('archetype')
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
