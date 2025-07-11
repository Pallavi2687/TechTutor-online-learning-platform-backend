from django.db import models

# Create your models here.

from accounts.models import CustomUser
from cloudinary.models import CloudinaryField

class Course(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail   = CloudinaryField('thumbnail', blank=True, null=True)
    instructor  = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="courses"
    )
    price       = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    video_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title}"
