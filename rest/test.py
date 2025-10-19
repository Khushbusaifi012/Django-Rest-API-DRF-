import requests
Base_URl="http://127.0.0.1:8000/"
ENDPOINT="apijson3/"
r=requests.get(Base_URl+ENDPOINT)
data=r.json()
print("Data from Django Application:")
print("Employee Number:",data['eno'])
print("Employee Name:",data['ename'])
print("Employee Salary:",data['esal'])
print("Employee Address:",data['eaddr'])