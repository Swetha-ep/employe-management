from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from.forms import *
# Create your views here.



#<----------- Landing page-------------------->
def home_page(request):
    return render(request,'home.html')





# <------------Add-and-employee--------------->
def add_emp(request):
    frm = EmployeeForm()
    if request.POST:
        frm =EmployeeForm(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect('homepage')
        print(frm.errors)
       
    return render(request,'add.html',{'frm':frm})





# <--------------Remove-an-employee------------->
def remove_emp(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            try:
                emp = Employees.objects.get(name=name)
                emp.delete()
                return redirect('homepage')
            except Employees.DoesNotExist:
                return render(request,'remove.html',{'error_message' :f"Employee with name '{name}' does not exist."})
    return render(request,'remove.html')






# <-----------------View-an-employee-------------->
def view_emp(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            try:
                emp = Employees.objects.get(name=name)
                return render(request,'view.html',{'employee':emp})
            except:
                return render(request,'view.html',{'error_message' :f"Employee with name '{name}' does not exist."})
    return render(request,'view.html')





# <------------------List-an-employee--------------->
def list_emp(request):
    emp_data = Employees.objects.all()
    return render(request,'list.html',{'emp_datas':emp_data})