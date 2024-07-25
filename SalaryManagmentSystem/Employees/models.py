from django.db import models

# Create your models here.

class Region(models.Model):
    name = models.CharField(max_length = 20, unique=True)
    
    def __str__(self):
        return self.name
    
class Team(models.Model):
    name = models.CharField(max_length = 20)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length= 20)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    salary = models.IntegerField()
    
    def __str__(self):
        return self.name
    

    