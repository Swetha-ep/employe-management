from django import forms
from django.forms import ModelForm
from .models import Employees

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18 or age > 100:
            raise forms.ValidationError("Age must be between 18 and 100.")
        return age
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.replace(' ', '').isalpha():
            raise forms.ValidationError("Name must contain only letters.")
        return name
