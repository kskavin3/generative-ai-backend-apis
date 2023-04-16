from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from course.models import Program,Course,Upload,UploadVideo
from course.serializers import CourseSerializer,ProgramSerializer,UploadSerializer,UploadVideoSerializer

@csrf_exempt
def courseApi(request,id=0):
    if request.method=='GET':
        courses = Course.objects.all()
        courses_serializer=CourseSerializer(courses,many=True)
        return JsonResponse(courses_serializer.data,safe=False)

@csrf_exempt
def programApi(request,id=0):
    if request.method=='GET':
        programs = Program.objects.all()
        programs_serializer=ProgramSerializer(programs,many=True)
        return JsonResponse(programs_serializer.data,safe=False)

@csrf_exempt
def uploadApi(request,id=0):
    if request.method=='GET':
        uploads = Upload.objects.all()
        uploads_serializer=UploadSerializer(uploads,many=True)
        return JsonResponse(uploads_serializer.data,safe=False)

@csrf_exempt
def uploadVideoApi(request,id=0):
    if request.method=='GET':
        uploadvideos = UploadVideo.objects.all()
        uploadvideos_serializer=UploadVideoSerializer(uploadvideos,many=True)
        return JsonResponse(uploadvideos_serializer.data,safe=False)

