from django.shortcuts import render

# Create your views here.

def employee_list(request):
    return render(request, "employee_register/employee_list.html")


# get and post api's from form
def employee_form(request):
    return render(request, "employee_register/employee_form.html")

#deleting a record
def employee_delete(request):
    return