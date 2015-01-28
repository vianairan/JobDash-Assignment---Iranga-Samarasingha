"""
Date: Jan 27th, 2015 
@author: Iranga Samarasingha

"""
from todo_app.models import Task
from django.shortcuts import render_to_response
from django.utils import timezone
from datetime import datetime
        
def Index(request):
   # This functions handles the requests from main Form
   # Request - 'status' --> Status update of a todo item (done/pending)
   # Request - 'todo' --> Addition of a new todo item to the list
    msg = "Please complete the fields and click [Add] button.";
    if request.method == "POST": 
        try:
            if 'status' in request.POST:   # 
                task = Task.objects.get(pk = request.POST['status']) # Filter the item based on pk
                task.completed = not task.completed # update the status of the item
                task.save()  
                
                msg = "Status change is successful !";
                
            
            elif 'todo' in request.POST:
                unicode_list = request.POST.getlist("todo[]") # Obtain the list of request parameters
                str_list = [str(x) for x in unicode_list]   # Convert unicode list into a list of strings
                
                new_title = str_list[0];
                new_assignedto = str_list[1];
                new_due_date_str = str_list[2];
                new_description = str_list[3];
                        
                if not Task.objects.filter(title=new_title).exists(): # Check if the title of the item already exists in the database
                
                    new_due_date = ConvertTimeStrToDate(new_due_date_str) # Convert the date time string into datetime object

                    if new_due_date>timezone.now(): # Check if due date is in the future
                        # Create a new task based on input parameters
                        task =  Task(title=new_title, assignedto=new_assignedto, due_date=new_due_date, description=new_description, assigned_date=timezone.now(),  assignedby=request.user.get_username())
                        task.save()  
                        msg = "New ToDo item is added !";  
                    else:
                        msg = "Error: Due date must be in future. Please check the due date.";  # Error msg if due date is already passed
                else:
                    msg = "Error: Item already exist. Please try a different title.";  # Error msg if title already exists
                
        except Task.DoesNotExist:
                pass  
            
    task_list = Task.objects.all();
    return render_to_response("todo_app/index.html", {'todo_list':task_list, 'msg':msg})  # Returns the list of todo items 
    
def ConvertTimeStrToDate(date_str):
    # Purpose: This function converts the date string into a datetime object
    # Input Args: 
    #    date_str - date string (Type: String) 
    # Output Args: 
    #    date_object - date object (Type: datetime)       
         
    time_zone = timezone.get_current_timezone()
    date_obj = time_zone.localize(datetime.strptime(date_str, '%Y-%m-%d'))
    
    return date_obj