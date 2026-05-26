from rest_framework .views import APIView
from rest_framework import response, status
from .models import Hospital,Patient
from .serializers import hospitalserializer

class detailedview(APIView):
    def get(self,request):
        hospital=Hospital.objects.all()
        serilaizer=hospitalserializer(hospital,many=True)
        return self.response(serilaizer.data)
    
    def post(self,request):
        serializer=hospitalserializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data)
        return response(serializer.errors)

class detailed(APIView):
    def get(self,request,pk):
        hos=Hospital.objects.get(id=pk)
        serial=hospitalserializer(hos)
        return response(serial.data)
    
    def post(self,request,pk):
        # hos=Hospital.objects.get(id=pk)
        serializer=hospitalserializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return response(serializer.data)
        
    def get(self,request,pk):

        hsp=Hospital.objects.get(id=pk)
        serializer=hospitalserializer(hsp)
        return response(serializer.data)


        
        
    
        


