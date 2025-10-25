import requests
BASE_URL="http://127.0.0.1:8000"
ENDPOINT="/empdetails/"
def get_resource(id):
    resp=requests.get(BASE_URL+ENDPOINT+id+'/')
    print(resp.status_code)
    print(resp.json())
id=input("Enter Employee id:")
get_resource(id)