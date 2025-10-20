from django.shortcuts import render
from django.views.generic import View
<<<<<<< HEAD
from testapp.models import Employee, College
=======
from testapp.models import Employee,College
>>>>>>> master
import json
from django.http import HttpResponse

# Create your views here.
class EmployeeDetailsCBV(View):
     def get(self,request,id,*args,**kwargs):
          emp=Employee.objects.get(id=id)
          emp_data={
               'eno':emp.eno,
               'ename':emp.ename,
               'esal':emp.esal,
               'eaddr':emp.eaddr,
          }
          json_data=json.dumps(emp_data)
          return HttpResponse(json_data,content_type='application/json')

class CollegeDetailsCBV(View):
    def get(self, request, id, *args, **kwargs):
        college = College.objects.get(id=id)
        college_data = {
            'cname': college.cname,
            'ccourse': college.ccourse,
            'csubjects': college.csubjects,
            'clocation': college.clocation,
        }
        json_data = json.dumps(college_data)
        return HttpResponse(json_data, content_type='application/json')
