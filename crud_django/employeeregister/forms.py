from django import forms
from .models import Employee

<<<<<<< HEAD
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('fullname','mobile_no','emp_code','position')
        labels = {
            'fullname':'Full Name',
            'emp_code':'EMP. Code'
        }
        
    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False
        
        
=======
class Employee_form(forms.ModelForm):
    class meta:
        model = Employee
        fields = '__all__'
>>>>>>> 4656793f087924959e111ab607ecbf7722f9f038
