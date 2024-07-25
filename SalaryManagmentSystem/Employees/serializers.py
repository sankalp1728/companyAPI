from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=20)
    team_name = serializers.CharField(max_length=20)
    region_name = serializers.CharField(max_length=20)
    

    
