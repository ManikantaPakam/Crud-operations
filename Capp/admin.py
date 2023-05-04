from django.contrib import admin
from Capp.models import Employee

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esalary','eaddress','eage']

admin.site.register(Employee,EmployeeAdmin)