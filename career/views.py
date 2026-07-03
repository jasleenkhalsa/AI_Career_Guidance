from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

from .forms import StudentForm

from django.shortcuts import redirect


def register(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/login/')

        else:
            print(form.errors)   # Add this line

    else:

        form = StudentForm()

    return render(request, 'register.html', {'form': form})

from .models import Student

from django.shortcuts import render, redirect
from .models import Student

def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            student = Student.objects.get(
                email=email,
                password=password
            )

            request.session["student"] = student.id
            return redirect("/questionnaire/")

        except Student.DoesNotExist:
            return render(request, "login.html", {
                "error": "Invalid Email or Password"
            })

    return render(request, "login.html"),{
        "error": "Invalid Email or Password"
    }


def questionnaire(request):

    if 'student' not in request.session:

        return redirect('/login/')

    return render(request,'questionnaire.html')

def result(request):
    return render(request, 'result.html')

def contact(request):
    return render(request, 'contact.html')

def logout(request):

    request.session.flush()

    return redirect('/login/')

