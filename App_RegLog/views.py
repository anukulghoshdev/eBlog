
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm #use SignUpForm and UserProfileChange form in forms.py

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# from django.contrib import messages
# from django.contrib.auth import update_session_auth_hash

from  App_RegLog.forms import SignUpForm, UserProfileChange, profile_pic
# SetPasswordForm -> old pass enter korte hobe na
# PasswordChangeForm -> old pass enter korte hobe
# PasswordResetForm ->  email er through te pass set korbe(advanced)



def sign_up(request):
    form  = SignUpForm()
    registered = False
    if request.method == 'POST':
        form  = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
    dict = {'form': form, 'registered':registered}
    return render(request, 'App_RegLog/signup.html', context=dict)


def login_page(request):
    Auth_form = AuthenticationForm()
    if request.method == 'POST':
        Auth_form = AuthenticationForm(data=request.POST)
        if Auth_form.is_valid():
            username = Auth_form.cleaned_data.get('username')
            password = Auth_form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    return render(request, 'App_RegLog/login.html', context={'form':Auth_form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('RegLog:login'))

@login_required
def profile(request):
    return render(request, 'App_RegLog/userprofile.html', context={})

@login_required()
def user_change(request):
    current_user = request.user
    form = UserProfileChange(instance=current_user)
    if request.method == 'POST':
        form = UserProfileChange(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserProfileChange(instance=current_user)
            return HttpResponseRedirect(reverse('RegLog:profile'))
    return render(request, 'App_RegLog/change_profile.html', context={ 'form': form })

@login_required
def pass_change(request):
    changed = False
    current_user = request.user
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            user = form.save()
            changed = True
            # update_session_auth_hash(request, user)  # Important!
            # messages.success(request, 'Your password was successfully updated!')

    return render(request, 'App_RegLog/change_pass.html', context={'form': form, 'changed': changed })

@login_required
def pro_pic(request):
    form = profile_pic()
    if request.method == 'POST':
        form = profile_pic(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('RegLog:profile'))
    return render(request, 'App_RegLog/add_pro_pic.html', context={'form': form})

@login_required
def change_pro_pic(request):
    form = profile_pic(instance=request.user.userinfo)
    if request.method == 'POST':
        form = profile_pic(request.POST, request.FILES, instance=request.user.userinfo)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('RegLog:profile'))
    return render(request, 'App_RegLog/add_pro_pic.html', context={'form':form})
