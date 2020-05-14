import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from smtp2go.forms import LoginForm
from smtp2go.functions import logout_web_user, login_web_user

log = logging.getLogger(__name__)


def index(request):
    return render(request, 'index.html', {})


def login(request):
    error = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            auth = login_web_user(request, username, password)
            if auth is True:
                return redirect('todo_app_index_page')
            else:
                error = "Invalid Login"
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'error': error})


@login_required
def logout(request):
    logout_web_user(request)
    return redirect('/')
