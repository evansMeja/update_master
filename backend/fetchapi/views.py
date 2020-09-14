from django.shortcuts import render
from django.http import *
import urllib.request, json
from django.core import serializers
from .models import *

def getdata(request): 
    # with urllib.request.urlopen("http://13.233.237.220:8091/getOemdetailsById?oem_id=100") as url:
    #     data = json.loads(url.read().decode())
    #     return JsonResponse(data,safe=False)
    qs = table1.objects.all()
    qs_json = eval(serializers.serialize('json', qs))
    
    l =[]
    for i in qs:
        qs = table1.objects.filter(id=i.id)
        qs_json = eval(serializers.serialize('json', qs))
        qs1 = contact_info.objects.filter(owner=i)
        qs1_json = eval(serializers.serialize('json', qs1))
        qs2 = oem_corp_address.objects.filter(owner=i)
        qs2_json = eval(serializers.serialize('json', qs2))
        qs_json[0]['fields']['oem_corp_address']=qs2_json[0]['fields']
        qs_json[0]['fields']['contact_info']=qs1_json[0]['fields']
        l.append(qs_json) 
        qs_json = json.dumps(l) 
    return HttpResponse(qs_json, content_type='application/json')