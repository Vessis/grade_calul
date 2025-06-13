
from django.contrib import admin
from django.urls import path, include
from grade_calculator import views  # 앱 이름에 따라 조정
from django.shortcuts import redirect


# urls.py
urlpatterns = [
    path('input/', views.input_student, name='input_student'),
    path('list/', views.student_list, name='student_list'),
    path('', lambda request: redirect('input_student')),
    path('admin/', admin.site.urls),
]

