from django.urls import path
from .views import upload_cv

urlpatterns = [
    path('upload/', upload_cv, name='upload_cv'),
]
