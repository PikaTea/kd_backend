from django.urls import path
from .views import FileViews

urlpatterns = [
    path('file/upload_text', FileViews.upload_text),
]