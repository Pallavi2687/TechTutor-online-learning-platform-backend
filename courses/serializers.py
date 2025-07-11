# courses/serializers.py
from rest_framework import serializers
from .models import Course
from .models import Lesson
from django.conf import settings

class CourseSerializer(serializers.ModelSerializer):
    instructor_name = serializers.CharField(source='instructor.username', read_only=True)
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'price', 'thumbnail', 'instructor_name']

    def get_thumbnail(self, obj):
        if obj.thumbnail and hasattr(obj.thumbnail, 'url'):
            return obj.thumbnail.url  # This should return the full Cloudinary URL
        return None

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'