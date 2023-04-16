from django.urls import path
from course import views


urlpatterns=[
    path('course',views.courseApi),
    path('course/<int:pk>/',views.courseApi),
    path('program',views.programApi),
    path('program/<int:pk>/',views.programApi),
    path('upload',views.uploadApi),
    path('upload/<int:pk>/',views.uploadApi),
    path('uploadvideo',views.uploadVideoApi),
    path('uploadvideo/<int:pk>/',views.uploadVideoApi)
]