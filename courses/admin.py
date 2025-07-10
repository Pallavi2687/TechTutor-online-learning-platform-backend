from django.contrib import admin

# Register your models here.
# courses/admin.py
from .models import Course
from .models import Lesson
admin.site.register(Course)


admin.site.register(Lesson)
