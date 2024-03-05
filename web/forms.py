from django import forms
from .models import ContactMessage, Student

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email_id', 'message']
        
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['Student_name', 'register_number', 'class_year','Enter_sem1_percentage','Enter_sem2_percentage','Enter_sem3_percentage','Enter_sem4_percentage','feedback']

   