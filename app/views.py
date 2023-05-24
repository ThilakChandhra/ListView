from django.shortcuts import render
from app.models import *
# Create your views here.
from django.views.generic import TemplateView,ListView

class school(TemplateView):
    template_name='app\home.html'
    
class school_list(ListView):
    model=School
    context_object_name='schoolnames'