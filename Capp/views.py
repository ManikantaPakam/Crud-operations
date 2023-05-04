from django.shortcuts import render,redirect
from Capp.models import Employee
from Capp.forms import EmployeeForm

# Create your views here.

def home_view(request):
    employees=Employee.objects.all()
    return render(request,"Capp/home.html",{'e':employees})

def form_view(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    return render(request,"Capp/forms.html",{'form':form})

def thankyou_view(request):
    return render(request,'Capp/thankyou.html')

def delete_view(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/home')

def update_view(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/home')
    return render(request,'Capp/update.html',{'employee':employee})