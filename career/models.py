from django.db import models

class Student(models.Model):

    full_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=10)

    dob = models.DateField()

    gender = models.CharField(max_length=10)

    college = models.CharField(max_length=100)

    degree = models.CharField(max_length=50)

    year = models.CharField(max_length=20)

    password = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
    

class Assessment(models.Model):

    student = models.ForeignKey(Student,on_delete=models.CASCADE)

    q1=models.IntegerField()
    q2=models.IntegerField()
    q3=models.IntegerField()
    q4=models.IntegerField()
    q5=models.IntegerField()
    q6=models.IntegerField()
    q7=models.IntegerField()
    q8=models.IntegerField()
    q9=models.IntegerField()
    q10=models.IntegerField()

    q11=models.IntegerField()
    q12=models.IntegerField()
    q13=models.IntegerField()
    q14=models.IntegerField()
    q15=models.IntegerField()
    q16=models.IntegerField()
    q17=models.IntegerField()
    q18=models.IntegerField()
    q19=models.IntegerField()
    q20=models.IntegerField()

    q21=models.IntegerField()
    q22=models.IntegerField()
    q23=models.IntegerField()
    q24=models.IntegerField()
    q25=models.IntegerField()
    q26=models.IntegerField()
    q27=models.IntegerField()
    q28=models.IntegerField()
    q29=models.IntegerField()
    q30=models.IntegerField()

    created=models.DateTimeField(auto_now_add=True)


class CareerRecommendation(models.Model):

    student=models.ForeignKey(Student,on_delete=models.CASCADE)

    career=models.CharField(max_length=100)

    skills=models.TextField()

    courses=models.TextField()

    jobs=models.TextField()

    accuracy=models.FloatField()

    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.career
    


