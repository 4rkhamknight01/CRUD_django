from django.shortcuts import render
from .forms import Employee_form
# Create your views here.

def employee_list(request):
    return render(request, "employee_register/employee_list.html")


# get and post api's from form
def employee_form(request):
    form = Employee_form()
    return render(request, "employee_register/employee_form.html", {'form':form})

#deleting a record
def employee_delete(request):
    return