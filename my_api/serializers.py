from rest_framework import serializers
from .models import School, Major, Material


class SchoolSerializer(serializers.ModelSerializer):
    """定义序列化器"""

    class Meta:
        model = School
        fields = '__all__'


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'
        extra_kwargs = {  # 修改字段选项
            'downloads': {
                'read_only': True  # 只进行反序列化
            }
        }
