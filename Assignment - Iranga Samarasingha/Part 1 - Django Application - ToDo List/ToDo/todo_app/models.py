"""
Date: Fri Jan 27th, 2015 
@author: Iranga Samarasingha

"""

from django.db import models

class Task(models.Model): # Class for todo task
         
    title = models.CharField(max_length=100, unique=False) # Title of the todo task
    assigned_date =  models.DateTimeField('Date Assigned') # Date of the task created
    due_date =  models.DateTimeField('Due Date') # Due date of the task
    description = models.TextField() # More descriptive information about the task
    completed = models.BooleanField(default=False); # Boolean field - if task is completed or not
    assignedby = models.CharField('Assigned By', max_length=30, blank=True, null=True)  # Name of the person who assigned the task
    assignedto = models.CharField('Assigned To', max_length=30, blank=True, null=True)  # Name of the person who is responsible of completing the task
 
    def __unicode__(self):  # Returns the string
        return self.title
