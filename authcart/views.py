from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request, "auth/register.html")
def login(request):
    return render(request, "auth/login.html")

def logout():
    return

