from django.urls import path
from .views import *

urlpatterns = [
    path('certificate/', CertificateList.as_view(), name='cert_list'),
    ]