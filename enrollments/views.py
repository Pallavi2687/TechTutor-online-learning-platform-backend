from rest_framework import viewsets, permissions, serializers
from .models import Enrollment
from .serializers import EnrollmentSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
      user = self.request.user
      course_id = self.request.query_params.get('course')
      qs = Enrollment.objects.filter(student=user)
      if course_id:
        qs = qs.filter(course__id=course_id)  # ✅ filter by course ID
      return qs


    def perform_create(self, serializer):
        if Enrollment.objects.filter(
            student=self.request.user, course=serializer.validated_data['course']
        ).exists():
            raise serializers.ValidationError('Already enrolled')
        serializer.save(student=self.request.user)
    def get_serializer_context(self):
        return {'request': self.request}
    
