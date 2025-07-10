from django.db import models

# Create your models here.
from django.db import models
from accounts.models import CustomUser
from courses.models import Course

class Review(models.Model):
    course      = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    reviewer    = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    rating      = models.PositiveSmallIntegerField()  # 1–5
    comment     = models.TextField(blank=True)
    reviewed_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("course", "reviewer")
