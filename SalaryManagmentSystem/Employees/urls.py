from django.urls import path
from .views import EmployeeByRegionAndTeamView

urlpatterns = [
    path('employees/', EmployeeByRegionAndTeamView.as_view(), name='list'),
]