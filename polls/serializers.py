from rest_framework import serializers
from .models import File3


class MyFileSerializer(serializers.ModelSerializer):

    class Meta():
        model = File3
        fields = ('file', 'description', 'uploaded_at')