from rest_framework import serializers
from books.models import Books, Employees


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Employees
        fields = "__all__"
        
        # fields = (
        #     'creat_at', 
        #     'actualized_at', 
        #     'active', 
        #     'book', 
        #     'name', 
        #     'email', 
        #     'business_unity',
        #     'type_function'
        # )

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = "__all__"
        
        # fields = (
        #     'creat_at', 
        #     'actualized_at', 
        #     'active', 
        #     'title', 
        #     'url'
        # )
