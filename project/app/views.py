from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
# Create your views here.


class CertificateList(ListView):
    model = Certificate
    template_name = 'list.html'
    context_object_name = 'certificate'
