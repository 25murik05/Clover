
from django.views.generic import ListView
from .models import *


class CertificateList(ListView):
    model = Certificate
    template_name = 'list.html'
    context_object_name = 'certificate'


