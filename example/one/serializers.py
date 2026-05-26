from rest_framework import serializers
from .models import Hospital,Patient

class hospitalserializer(serializers.ModelSerializer):
    class Meta:
        Model=Hospital
        fields='__all__'