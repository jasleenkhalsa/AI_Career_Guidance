from django.contrib import admin

from .models import Student
from .models import Assessment
from .models import CareerRecommendation
from .models import CareerInfo

admin.site.register(Student)
admin.site.register(Assessment)
admin.site.register(CareerRecommendation)
admin.site.register(CareerInfo)

