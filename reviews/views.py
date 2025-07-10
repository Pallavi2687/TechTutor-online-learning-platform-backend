# reviews/views.py
from rest_framework import viewsets, permissions, serializers
from .models import Review
from enrollments.models import Enrollment
from .serializers import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class   = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset           = Review.objects.all()

    def get_queryset(self):
        course_id = self.request.query_params.get('course')
        return Review.objects.filter(course_id=course_id) if course_id else Review.objects.all()

    def perform_create(self, serializer):
        course = serializer.validated_data['course']
        if not Enrollment.objects.filter(course=course, student=self.request.user).exists():
            raise serializers.ValidationError('Enroll first to review')
        serializer.save(user=self.request.user)   # ← or student=... if model uses student
