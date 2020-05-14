from django.contrib.auth import login as auth_login, authenticate, logout


def login_web_user(request, username, password):
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return True
        else:
            return False
    else:
        return False


def logout_web_user(request):
    logout(request)
    return
