from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        """Allow read-only for all, edit only for staff."""
        if self.action in ['list', 'retrieve', 'by_course']:
            return [AllowAny()]
        return [IsAdminUser()]

    @action(detail=False, methods=['get'], url_path='by-course/(?P<course_id>[^/.]+)')
    def by_course(self, request, course_id=None):
        lessons = Lesson.objects.filter(course_id=course_id)
        serializer = self.get_serializer(lessons, many=True)
        return Response(serializer.data)


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        """Anonymous users may LIST courses.
        Authenticated users may RETRIEVE.
        Only staff can CREATE, UPDATE, DELETE."""
        if self.action == "list":
            return [AllowAny()]
        if self.action == "retrieve":
            return [IsAuthenticated()]
        return [IsAdminUser()]
