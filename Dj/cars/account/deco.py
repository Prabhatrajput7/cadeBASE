from django.shortcuts import render, redirect

def redir(fx):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return fx(request, *args, **kwargs)
    return wrapper