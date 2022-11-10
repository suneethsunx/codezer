from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect

def logout(request):
    auth_logout(request)

    return redirect('index')

def login(request):

    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username = email, password = password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'You have been successfully Loged in to Codezer !')
            return redirect('index')

        messages.error(request, 'Account not found, try again.')
        # return HttpResponseRedirect(request.path_info)
        return redirect('index')


def register(request):
    
    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(username = email)
        except:
            user = None
        if user is None:
            new_user = User.objects.create(
                username = email,
                email = email,
            )
            new_user.set_password(password)
            new_user.save()

            auth_login(request, new_user)
            messages.success(request, 'You have been successfully Loged in to Codezer !')
            return redirect('index')

        messages.error(request, 'Account with same email has already exists !')
        return redirect('index')