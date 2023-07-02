from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from core.models import *


# Create your views here.
def index(request):
    course_objs = course.objects.all()
    return render(request,'index.html',{'course_objs':course_objs})
def PDF(request):
    if request.method=='GET':
        
        ids=request.GET.get('id')
        course_objs=course.objects.get(id=ids)
        pdf_object=PDF_var.objects.filter(module=course_objs)
        print(pdf_object)
        return render(request,'course.html',{'pdf_object':pdf_object,'course_objs':course_objs})

    return HttpResponse("invalid")
