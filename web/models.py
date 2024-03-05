from django.db import models

class Student(models.Model):
    
    YEAR_CHOICES=[
        ('1','I-YEAR'),
        ('2','II-YEAR'),
    ]
    Student_name=models.CharField(max_length=100)
    register_number=models.CharField(max_length=20,unique=True)
    class_year=models.CharField(max_length=16, choices=YEAR_CHOICES, default='1')
    Enter_sem1_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Enter_sem2_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Enter_sem3_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Enter_sem4_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    feedback = models.TextField()

    def __str__(self):
        return self.Student_name
    
class ContactMessage(models.Model):
    name=models.CharField(max_length=100)
    email_id=models.EmailField()
    message=models.TextField()
    
    def __str__(self):
        return self.name
