from django.urls import path

from . import views

urlpatterns =[
    path('course/', views.courses,name='courses'),
    path('<int:course_id>', views.course,name='course'),
    path('<search>', views.search,name='search')
]