import json
from django.http import JsonResponse
from django.core import serializers
from home_automation.models import home_automation
# Create your views here.

def initial(request):
    try:
        record1 = home_automation(roomtype="bedroom", light_status=None, temperature_degree=None, thermostat_status=None)
        record1.save()
        record2 = home_automation(roomtype="livingroom", light_status=None, temperature_degree=None, thermostat_status=None)
        record2.save()
        record3 = home_automation(roomtype="bathroom", light_status=None, temperature_degree=None, thermostat_status=None)
        record3.save()
    except:
        return JsonResponse({'message': 'Error: can not initial the data to database'})
    return JsonResponse({'message': 'Success: initial the database'})

def addroom(request):

    newroomtype = request.GET.get('roomtype')
    if request.GET.get('roomtype') != None:
        record = home_automation(roomtype=newroomtype, light_status=request.GET.get('lightstatus'),
                                 temperature_degree=request.GET.get('temperature'),
                                 thermostat_status=request.GET.get('thermostatstatus'))
        record.save()
    else:
        return JsonResponse({'message': 'Error: you need to provide room type'})

    return JsonResponse({'message': 'Success: add the room info to the home_automation table'})

def cleardb(request):
    try:
        home_automation.objects.all().delete()
    except:
        return JsonResponse({'message': 'Error: can not clear all row for home_automation table'})
    return JsonResponse({'message': 'Success: rest the home_automation table'})


def light(request):
    roomid = request.GET.get('id')
    lightstatus = int(request.GET.get('value'))
    if roomid == None or lightstatus == None or (lightstatus != 1 and lightstatus != 0):
        return JsonResponse({'message': 'Error: input is not valid'})
    else:
        record = home_automation.objects.raw('SELECT * FROM home_automation WHERE id=%s',[roomid])
        if not record:
            return JsonResponse({'message': 'Error: can not find the roomid in the database'})
        else:
            record = record[0]
            if record.light_status == None or int(record.light_status) != int(lightstatus):
                record.light_status = lightstatus
                record.save()
            else:
                return JsonResponse({'message': 'Waring: the new light status is same as before, so no change'})

    return JsonResponse({'message': 'Success: change the light status for the room (roomid is %s)'%roomid})


def temperature(request):
    roomid = request.GET.get('id')
    temperature  = float(request.GET.get('value'))
    if roomid == None or temperature  == None:
        return JsonResponse({'message': 'Error: input is not valid'})
    else:
        record = home_automation.objects.raw('SELECT * FROM home_automation WHERE id=%s',[roomid])
        if not record:
            return JsonResponse({'message': 'Error: can not find the roomid in the database'})
        else:
            record = record[0]
            if record.temperature_degree  == None or float(record.temperature_degree) != float(temperature):
                record.temperature_degree = temperature
                record.save()
            else:
                return JsonResponse({'message': 'Waring: the new temperature degree is same as before, so no change'})

    return JsonResponse({'message': 'Success: change the temperature degree for the room (roomid is %s)'%roomid})

def thermostat(request):
    roomid = request.GET.get('id')
    thermostat = request.GET.get('value')
    if roomid == None or thermostat == None or (thermostat != 'off' and thermostat != 'cool' and thermostat != 'heat' and thermostat != 'fan-on' and thermostat != 'auto'):
        return JsonResponse({'message': 'Error: input is not valid'})
    else:
        record = home_automation.objects.raw('SELECT * FROM home_automation WHERE id=%s',[roomid])
        if not record:
            return JsonResponse({'message': 'Error: can not find the roomid in the database'})
        else:
            record = record[0]
            if record.thermostat_status  == None or record.thermostat_status != thermostat:
                record.thermostat_status = thermostat
                record.save()
            else:
                return JsonResponse({'message': 'Waring: the new thermostat status is same as before, so no change'})

    return JsonResponse({'message': 'Success: change the thermostat status for the room (roomid is %s)'%roomid})


def list(request):
    result = []
    for record in home_automation.objects.values():
        result.append(record)
    return JsonResponse(result, safe=False)


