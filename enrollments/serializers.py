from rest_framework import serializers
from .models import Enrollment

class EnrollmentSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title', read_only=True)
    thumbnail_url = serializers.SerializerMethodField()

    class Meta:
        model = Enrollment
        fields = ['id', 'course', 'course_title', 'progress', 'enrolled_on', 'thumbnail_url']

    def get_thumbnail_url(self, obj):
        request = self.context.get('request')
        if obj.course.thumbnail:
            return request.build_absolute_uri(obj.course.thumbnail.url)
        return ''
