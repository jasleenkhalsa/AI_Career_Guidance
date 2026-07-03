from django.shortcuts import render, redirect

from .forms import StudentForm
from .models import Student

from .ml.predict import predict
from .career_data import CAREER_DATABASE

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


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

    if request.method == "POST":

        # Read all answers
        answers = []

        for i in range(1, 31):
            answers.append(int(request.POST.get(f"q{i}", 3)))

        # Convert answers into 10 features
        features = [

            sum(answers[0:3]) / 3,
            sum(answers[3:6]) / 3,
            sum(answers[6:9]) / 3,
            sum(answers[9:12]) / 3,
            sum(answers[12:15]) / 3,
            sum(answers[15:18]) / 3,
            sum(answers[18:21]) / 3,
            sum(answers[21:24]) / 3,
            sum(answers[24:27]) / 3,
            sum(answers[27:30]) / 3

        ]

        # AI Prediction
        category, probability = predict(features)

        confidence = round(max(probability) * 100, 2)

        # Fetch career details
        career_info = CAREER_DATABASE.get(category)

        # Feature scores for chart
        feature_scores = {
            "Openness": features[0],
            "Conscientiousness": features[1],
            "Extraversion": features[2],
            "Agreeableness": features[3],
            "Neuroticism": features[4],
            "Numerical": features[5],
            "Spatial": features[6],
            "Perceptual": features[7],
            "Abstract": features[8],
            "Verbal": features[9],
        }

        return render(
            request,
            "result.html",
            {
                "category": category,
                "confidence": confidence,
                "career": career_info,
                "feature_scores": feature_scores,
            }
        )

    return redirect("/questionnaire/")

def contact(request):
    return render(request, 'contact.html')

def logout(request):

    request.session.flush()

    return redirect('/login/')
