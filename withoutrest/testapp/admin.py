from django.contrib import admin
from testapp.models import Employee, College

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eaddr']
admin.site.register(Employee,EmployeeAdmin)

class CollegeAdmin(admin.ModelAdmin):
    list_display=['id','cname','ccourse','csubjects','clocation']
admin.site.register(College,CollegeAdmin)