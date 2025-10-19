from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def emp_data_view(request):
    emp_data={
        'eno':101,
        'ename':'sachin',
        'esal':10000,
        'eaddr':'pune'

        # 'eno':102,
        # 'ename':'dhoni',
        # 'esal':20000,
        # 'eaddr':'ranchi',  #always last one will be considered
    }


import json
def emp_data_jsonview(request):
    emp_data={
        'eno':103,
        'ename':'sachin',
        'esal':10000,
        'eaddr':'pune'
    }
    json_data=json.dumps(emp_data)

    return HttpResponse(json_data,content_type="application/json")

from django.http import JsonResponse
def emp_data_jsonview2(request):
    emp_data={
        'eno':10355,
        'ename':'khushbu',
        'esal':10000,
        'eaddr':'pune'
    }
    return JsonResponse(emp_data)

from django.views.generic import View
class JsonCBV(View):
    def get(self,request,*args,**kwargs):
        emp_data={
            'eno':10355,
            'ename':'khushbu',
            'esal':10000,
            'eaddr':'pune'
        }
        return JsonResponse(emp_data)