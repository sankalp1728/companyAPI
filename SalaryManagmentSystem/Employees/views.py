from rest_framework import generics
from rest_framework.response import Response
from .models import Employee, Team, Region
from .serializers import EmployeeSerializer

class EmployeeByTeamView(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        team_name = self.kwargs['team_name']
        return Employee.objects.filter(team__name=team_name)

class EmployeeByRegionView(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        region_name = self.kwargs['region_name']
        return Employee.objects.filter(team__region__name=region_name)
    
    
class EmployeeByRegionAndTeamView(generics.ListAPIView):
    
    def list(self, request):
        employee_queryset = Employee.objects.all()
        team_name = request.query_params.get('team')
        region_name = request.query_params.get('region')
        offset = request.query_params.get('offset')
        limit = request.query_params.get('limit')
        
        if team_name:
            employee_queryset = employee_queryset.filter(team__name=team_name)
        if region_name:
            employee_queryset = employee_queryset.filter(team__region__name=region_name)
        
        
            
        
        