from django.shortcuts import render
<<<<<<< HEAD
from .forms import EmployeeForm
=======
from .forms import Employee_form
>>>>>>> 4656793f087924959e111ab607ecbf7722f9f038
# Create your views here.

def employee_list(request):
    return render(request, "employeeregister/employee_list.html")


# get and post api's from form
def employee_form(request):
<<<<<<< HEAD
    form = EmployeeForm()
    return render(request, "employeeregister/employee_form.html", {'form':form})
=======
    form = Employee_form()
    return render(request, "employee_register/employee_form.html", {'form':form})
>>>>>>> 4656793f087924959e111ab607ecbf7722f9f038

#deleting a record
def employee_delete(request):
    return