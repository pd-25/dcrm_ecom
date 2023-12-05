from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    if (request.method =="post"):
        print('hrre')
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        if password != confirmPassword:
            return HttpResponse('password dont match')

        
        try:
            if User.objects.get(username=name):
                 return HttpResponse('user exist')
        except Exception as identifier:
            return HttpResponse(identifier)

        user = User.objects.create_user(name, email, password)
        user.save()
        return HttpResponse('user created')
    print('th')
    return render(request, "auth/register.html")
def login(request):
    return render(request, "auth/login.html")

def logout():
    return

