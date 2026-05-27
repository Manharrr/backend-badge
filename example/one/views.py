from rest_framework .views import APIView
from rest_framework import response
from rest_framework import status

from .models import Hospital,Patient
from .serializers import hospitalserializer,patientserializer

class patientview(APIView):
    def get(self,request):
        patient=Patient.objects.all()
        serializer=patientserializer(patient,many=True)
        return response(serializer.data)
    
    def post (self,request):
        serializer=patientserializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response(serializer.data)
        return response(serializer.error)

class patientdetailedview(APIView):

    def get (self,request,pk):
        patient=patient.objects.get(id=pk)
        serializer=patientserializer(data=request.data)
        return self.response(serializer.data)
    def put(self,request,pk):
        patient=Patient.objects.get(id=pk)
        serializer=patientserializer(patient,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response(serializer.data)
        return response(serializer.error)
    def delete(self,request ,pk):
        pat=Patient.objects.get(id=pk)
        pat.delete()
        return response({'deleted'})
    
        
        


        

    



























# from rest_framework .views import APIView
# from rest_framework import response, status
# from .models import Hospital,Patient
# from .serializers import hospitalserializer

# class detailedview(APIView):
#     def get(self,request):
#         hospital=Hospital.objects.all()
#         serilaizer=hospitalserializer(hospital,many=True)
#         return self.response(serilaizer.data)
    
#     def post(self,request):
#         serializer=hospitalserializer(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return response(serializer.data)
#         return response(serializer.errors)

# class detailed(APIView):
#     def get(self,request,pk):
#         hos=Hospital.objects.get(id=pk)
#         serial=hospitalserializer(hos)
#         return response(serial.data)
    
#     def post(self,request,pk):
#         # hos=Hospital.objects.get(id=pk)
#         serializer=hospitalserializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#             return response(serializer.data)
        
#     def get(self,request,pk):

#         hsp=Hospital.objects.get(id=pk)
#         serializer=hospitalserializer(hsp)
#         return response(serializer.data)


        
        
    
        


