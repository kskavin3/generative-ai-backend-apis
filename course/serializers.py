from rest_framework import serializers
from course.models import Program,Course,Upload,UploadVideo

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id','slug','title','code','credit','summary','program','level','year','semester','is_elective')

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model=Program
        fields = ('id','title','summary')

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Upload
        fields = ('id','title','course','file','updated_date','upload_time')

class UploadVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=UploadVideo
        fields = ('id','title','slug','course','video','summary','timestamp')