from rest_framework import serializers
from .models import File2

class MyFileSerializer(serializers.ModelSerializer):

    class Meta():
        model = File2
        fields = ('file')