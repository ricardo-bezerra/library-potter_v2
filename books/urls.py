from django.urls import path
from books.views import BookAPIView, EmployeeAPIView

urlpatterns = [
    path('books/', BookAPIView.as_view(), name='books'),
    path('employees/', EmployeeAPIView.as_view(), name='employees')
]