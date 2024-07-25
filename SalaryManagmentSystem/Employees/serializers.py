from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=20)
    salary = serializers.IntegerField()
    team_name = serializers.CharField(max_length=20)
    region_name = serializers.CharField(max_length=20)
    
    
    def to_representation(self, instance):
        return {
            "id": instance.id,
            "name": instance.name,
            "salary": instance.salary,
            "team_name": instance.team.name,
            "region_name": instance.team.region.name  
        }
    

    
