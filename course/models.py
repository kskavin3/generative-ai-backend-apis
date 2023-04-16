from django.db import models

# Create your models here.

class Program(models.Model):
    id= models.IntegerField(primary_key=True,unique=True)
    title = models.CharField(max_length=150, unique=True)
    summary = models.TextField(null=True, blank=True)


class Course(models.Model):
    id= models.IntegerField(primary_key=True,unique=True)
    slug = models.SlugField(blank=True, unique=True)
    title = models.CharField(max_length=200, null=True)
    code = models.CharField(max_length=200, unique=True, null=True)
    credit = models.IntegerField(null=True, default=0)
    summary = models.TextField(max_length=200, blank=True, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    level = models.CharField(max_length=25, null=True)
    year = models.IntegerField( default=0)
    semester = models.CharField(max_length=200)
    is_elective = models.BooleanField(default=False, blank=True, null=True)

class Upload(models.Model):
    id= models.IntegerField(primary_key=True,unique=True)
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    file = models.FileField(upload_to='course_files/')
    updated_date = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    upload_time = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)



class UploadVideo(models.Model):
    id= models.IntegerField(primary_key=True,unique=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    video = models.FileField(upload_to='course_videos/')
    summary = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

