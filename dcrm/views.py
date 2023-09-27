from django.shortcuts import render

def index(request):
    return render(request, "dcrm/index.html")

def contact(request):
    return render(request, "dcrm/contact.html")
