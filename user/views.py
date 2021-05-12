<<<<<<< Updated upstream

from django.shortcuts import render, redirect

from user.forms.user_form import UserCreateForm


=======
from django.shortcuts import render
from user.models import Profile
>>>>>>> Stashed changes
def index(request):
    return render(request, 'user/register.html')


def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance = profile,data=request.POST)
        if fomr.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=profile)
    })

def register(request):
    if request.method == "POST":
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreateForm()
    })
