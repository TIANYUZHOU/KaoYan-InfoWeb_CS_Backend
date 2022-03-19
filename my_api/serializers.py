from rest_framework import serializers
from .models import School


class SchoolSerializer(serializers.ModelSerializer):
    """定义序列化器"""

    class Meta:
        model = School
        fields = '__all__'
