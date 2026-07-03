from django.contrib import admin

from .models import Student
from .models import Assessment
from .models import CareerRecommendation

admin.site.register(Student)
admin.site.register(Assessment)
admin.site.register(CareerRecommendation)

