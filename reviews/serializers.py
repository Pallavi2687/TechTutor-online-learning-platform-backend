from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Review
        # ✨ only the fields that actually exist on your model
        fields = ['id', 'course', 'rating', 'comment']
        read_only_fields = ['id']
