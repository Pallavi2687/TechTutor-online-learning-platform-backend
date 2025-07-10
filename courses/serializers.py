from rest_framework import serializers
from .models import Course
from .models import Lesson

class CourseSerializer(serializers.ModelSerializer):
    instructor_name = serializers.CharField(source='instructor.username', read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'price', 'thumbnail', 'instructor_name']

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'