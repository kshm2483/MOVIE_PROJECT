from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Create your views here.
############################ signup ################################

    
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
      
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) 				# 1 ?? 
            return redirect('movies:list')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)
    
########################### login ####################################
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'movies:list') # 해당 코드 수정
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)
    
    
    
############logout ####################


def logout(request):
    auth_logout(request)
    return redirect('movies:list')
    
    


###### 회원정보 수정 및 탈퇴 ###############3
@login_required
def update(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_change_form.is_valid():
            user = user_change_form.save()
            return redirect('people')
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)

    context = {'user_change_form': user_change_form}
    return render(request, 'accounts/update.html', context)


@login_required
def delete(request):
    if request.method == 'POST':
        request.user.delete()
    return redirect('posts:list')

    
############################# 비밀번호 변경 #########################
@login_required
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('posts:list')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/password.html', context)


    
    


    

