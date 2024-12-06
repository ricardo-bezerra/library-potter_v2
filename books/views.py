from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from books.models import Books, Employees
from books.api.serializers import BookSerializer, EmployeeSerializer

class BookAPIView(APIView):
    def get(self, request):
        books = Books.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    
class EmployeeAPIView(APIView):
    def get(self, request):
        employees = Employees.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
