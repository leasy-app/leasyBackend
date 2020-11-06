from rest_framework import serializers
from .models import File2

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File2
        fields = "__all__"
