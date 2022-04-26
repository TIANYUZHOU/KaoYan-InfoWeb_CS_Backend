from rest_framework import serializers

from user.models import User
from .models import School, Major, Material, Collect, Link


class SchoolSerializer(serializers.ModelSerializer):
    """定义序列化器"""

    class Meta:
        model = School
        fields = '__all__'


# 学校外键序列化器
class ForSchoolSerializer(serializers.ModelSerializer):
    """定义序列化器"""

    class Meta:
        model = School
        fields = ['schName']
        extra_kwargs = {  # 修改字段选项
            'schName': {
                'read_only': True  # 只进行序列化
            }
        }


# 资料-用户外键序列化器
class MaterialsUsersProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
        extra_kwargs = {  # 修改字段选项
            'username': {
                'read_only': True  # 只进行序列化
            }
        }


class MajorSerializer(serializers.ModelSerializer):
    school = ForSchoolSerializer()

    class Meta:
        model = Major
        fields = '__all__'


# 资料上传序列化器
class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'
        extra_kwargs = {  # 修改字段选项
            'downloads': {
                'read_only': True  # 只进行反序列化
            },
            'file': {
                'write_only': True  # 只进行反序列化
            },
        }


# 资料查询序列化器
class MaterialInfoSerializer(serializers.ModelSerializer):
    school = ForSchoolSerializer()
    user = MaterialsUsersProfileSerializer()

    class Meta:
        model = Material
        exclude = ['file']  # 除此字段外


class CollectUsersProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
        extra_kwargs = {  # 修改字段选项
            'username': {
                'read_only': True  # 只进行序列化
            },
            'id': {
                'read_only': True  # 只进行序列化
            }
        }


# 学校多对多序列化器
class MTMSchoolSerializer(serializers.ModelSerializer):
    """定义序列化器"""

    class Meta:
        model = School
        fields = ['id']
        extra_kwargs = {  # 修改字段选项
            'schName': {
                'read_only': True  # 只进行序列化
            }
        }


# 用户信息-用户收藏序列化器
class InfoCollectSerializer(serializers.ModelSerializer):
    school = SchoolSerializer(many=True)
    user = CollectUsersProfileSerializer()

    class Meta:
        model = Collect
        fields = '__all__'


# 用户收藏序列化器
class CollectSerializer(serializers.ModelSerializer):
    # school = MTMSchoolSerializer(many=True)
    # user = CollectUsersProfileSerializer()

    class Meta:
        model = Collect
        fields = '__all__'
        # extra_kwargs = {  # 修改字段选项
        #     'user': {
        #         'read_only': True  # 只进行序列化
        #     }
        # }


# 友情链接序列化器
class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = '__all__'
