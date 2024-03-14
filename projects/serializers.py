from rest_framework import serializers
from .models import Projec

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projec
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at',)
