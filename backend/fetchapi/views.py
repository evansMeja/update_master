from django.shortcuts import render
from django.http import *
import urllib.request, json

def getdata(request): 
    with urllib.request.urlopen("http://13.233.237.220:8091/getOemdetailsById?oem_id=100") as url:
        data = json.loads(url.read().decode())
        print(data)
        return JsonResponse(data,safe=False)
        