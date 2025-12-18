from django.urls import path
from .views import gpa_page, delete_subject, edit_subject

urlpatterns = [
    path('', gpa_page, name='gpa_page'),
    path('delete/<int:pk>/', delete_subject, name='delete_subject'),
    path('edit/<int:pk>/', edit_subject, name='edit_subject'),
]
