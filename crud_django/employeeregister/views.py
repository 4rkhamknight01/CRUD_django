from django.shortcuts import render
from .forms import EmployeeForm
# Create your views here.

def employee_list(request):
    return render(request, "employeeregister/employee_list.html")


# get and post api's from form
def employee_form(request):
    form = EmployeeForm()
    return render(request, "employeeregister/employee_form.html", {'form':form})

#deleting a record
def employee_delete(request):
    return