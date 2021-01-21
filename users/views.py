from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile
from django.db.utils import IntegrityError
from users.forms import ProfileForm

import pdb

def login_view(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(req, username=username, password=password)
        if user:
            login(req, user)
            return redirect('feed')
        else:
            return render(req,'users/login.html', {'error':'Invalid user'})
    return render(req,'users/login.html')

@login_required  ## Para que no pueda hacer logout de una sesion que no se ha iniciado
def logout_view(req):
    logout(req)
    return redirect('login')


def signup_view(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        password_conf = req.POST.get('password_confirmation')
        name = req.POST.get('name')
        lastname = req.POST.get('lastname')
        email = req.POST.get('email')

        if password != password_conf:
            return render(req,'users/signup.html', {'error': "Passwords didn't match"})
        else: 
            try:
                user = User.objects.create_user(username=username, password=password)
            except IntegrityError:
                return render(req,'users/signup.html', {'error': "User already exists"})

            user.first_name = name
            user.last_name = lastname
            user.email = email
            user.save()

            profile = Profile(user=user)
            profile.save() ## Siempre que se cree algo se debe guardar asi

            return redirect('login')

    return render(req,'users/signup.html')

@login_required
def update_profile(req):
    profile = req.user.profile
    if req.method == 'POST':
        form = ProfileForm(req.POST, req.FILES)
        ##pdb.set_trace()
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']

            profile.save()

            return redirect('update_profile')
    else :
        form = ProfileForm()
        print(form.errors)

    return render(
        request=req,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': req.user,
            'form': form
            },
        )