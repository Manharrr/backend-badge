from rest_framework import serializers
from .models import Hospital,Patient

class hospitalserializer(serializers.ModelSerializer):
    class Meta:
        Model=Hospital
        fields='__all__'


class patientserializer(serializers.ModelSerializer):


    class Meta:
        Model=Patient
        field='__all__'
