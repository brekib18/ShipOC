
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

from django.shortcuts import render, redirect

from user.forms.profile_form import ProfileForm
from user.forms.user_form import SignUpForm
from user.models import Profile


def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render (request, 'user/profile.html', {
        'form': ProfileForm(instance=profile)
    })


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticated(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'user/register.html', {'form': form})
