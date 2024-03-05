from . import views
from django.urls import path

urlpatterns = [
    path('contact/',views.contact,name='contact'),
    path('student/',views.student,name='student'),
    path('home/',views.home,name='home'),
    path('faculty/',views.faculty,name='faculty'),
    path('course/',views.course,name='course'),
]
