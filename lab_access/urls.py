from django.urls import path
from .views import log_access

urlpatterns = [
    path('log_access/', log_access, name= 'log_access'),
]