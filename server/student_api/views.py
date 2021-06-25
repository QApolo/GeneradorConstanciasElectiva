from student_api.models import StudentModel
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from student_api.serializers import StudentSerializer

from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework.response import Response
from django.forms.models import model_to_dict

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
    #permission_classes = [permissions.IsAuthenticated]


@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def registerStudent(request):
    if request.method == 'POST':
        try:
            stud = StudentModel.objects.get(pk=request.data.get('id'))                
            serializer = StudentSerializer(stud, data=request.data)
        except StudentModel.DoesNotExist:        
            serializer = StudentSerializer(data=request.data)
        
        if serializer.is_valid():
            rows = request.data.get('rows').split('^')
            for r in rows:
                print(r)
            serializer.save()
            return Response(request.data)
        return JsonResponse(serializer.errors, status=400)


@api_view(["PUT"])
@permission_classes((permissions.AllowAny,)) #change to IsAuthenticated
def validateStudent(request, idstudent):
    if request.method == 'PUT':
        try:
            stud = StudentModel.objects.get(pk=idstudent)                
            stud.validated = True
            serializer = StudentSerializer(stud, data=model_to_dict(stud))
        except StudentModel.DoesNotExist:        
            return JsonResponse({}, status=400)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({}, status=200)
        return JsonResponse(serializer.errors, status=400)
