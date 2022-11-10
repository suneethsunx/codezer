from rest_framework.serializers import ModelSerializer

from base.models import CodeFile

class CodeSerializer(ModelSerializer):
    class Meta:
        model = CodeFile
        fields = ['id','title', 'code', 'created_at','link_id']
