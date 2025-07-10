from django.conf import settings
from django.db import models
from courses.models import Course   # adjust import if needed

class Enrollment(models.Model):
    student      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course       = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress     = models.PositiveIntegerField(default=0)
    enrolled_on  = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')   # 🔒 no double enroll
