from django import forms
from .models import Employee

class Employee_form(forms.ModelForm):
    class meta:
        model = Employee
        fields = '__all__'