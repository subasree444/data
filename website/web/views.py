from django.shortcuts import render
from .forms import ContactForm, StudentForm
from django.http import JsonResponse

# Create your views here.

def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'success'})

            
    else:
        form=ContactForm()
        
    return render(request, 'contact.html',{'form':form})

def student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'success'})
    else:
        form = StudentForm()
        
    return render(request, 'student.html', {'form': form})


        
        
def home(request):
    return render(request,'home.html')

def faculty(request):
    return render(request,'faculty.html')

def course(request):
    return render(request, 'course.html')