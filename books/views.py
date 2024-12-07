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
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response({"message": "Created with success!"}, status=status.HTTP_201_CREATED)
        # return Response({"id": serializer.data['id'], "book": serializer.data['title']}, status=status.HTTP_201_CREATED)
    
class EmployeeAPIView(APIView):
    def get(self, request):
        employees = Employees.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
            serializer = EmployeeSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return Response({"message": "Created with success!"}, status=status.HTTP_201_CREATED)
            # return Response({"id": serializer.data['id'], "employee": serializer.data['name']}, status=status.HTTP_201_CREATED)