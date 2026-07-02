from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def questionnaire(request):
    return render(request, 'questionnaire.html')

def result(request):
    return render(request, 'result.html')

def contact(request):
    return render(request, 'contact.html')