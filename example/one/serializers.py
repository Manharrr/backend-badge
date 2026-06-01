from rest_framework import serializers
from .models import Hospital,Patient

class hospitalserializer(serializers.ModelSerializer):
    class Meta:
        model=Hospital
        fields='__all__'


class patientserializer(serializers.ModelSerializer):


    class Meta:
        model=Patient
        fields='__all__'
# from rest_framework import serializers
# from .models import patient,hospital


# class hospitalserializer(serializers.ModelSerializer):
#     class Meta:
#         Model=hospital
#         fields='__all__'

# class patientserializer(serializers.ModelSerializer):
#     class Meta:
#         Model=patient
#         fileds='__all__'