from django.http import JsonResponse
from home_automation.models import home_automation
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def initial(request):
    """
    Create initial rooms into home_automation(database)
    """
    if request.method == 'POST':
        try:
            record1 = home_automation(roomtype="bedroom", light_status=None, temperature_degree=None, thermostat_status=None)
            record1.save()
            record2 = home_automation(roomtype="livingroom", light_status=None, temperature_degree=None, thermostat_status=None)
            record2.save()
            record3 = home_automation(roomtype="bathroom", light_status=None, temperature_degree=None, thermostat_status=None)
            record3.save()
        except:
            return JsonResponse({'message': 'Error: can not initial the data to database'})

        result = [{'message': 'Success: initial the database'}]
        result.append(getdata())
        return JsonResponse(result, safe=False)
    else:
        return JsonResponse({'message': 'Error: Wrong command, should use POST'})

def addroom(request):
    """
    Create your own room, assign new unique id to the room
    """
    if request.method == 'POST':

        try:
            status = ["off", "cool", "heat", "fan-on", "auto"]
            newroomtype = request.headers['Roomtype']
            newlightstatus = None
            newtemperature = None
            newthermostatstatus = None
            if 'Lightstatus' in request.headers and (request.headers['Lightstatus'] == '1' or request.headers['Lightstatus'] == '0'):
                newlightstatus = request.headers['Lightstatus']
            if 'Temperature' in request.headers:
                newtemperature = float(request.headers['Temperature'])
            if 'Thermostatstatus' in request.headers and request.headers['Thermostatstatus'] in status:
                newthermostatstatus = request.headers['Thermostatstatus']
        except:
            return JsonResponse({'message': 'Error: input is not valid'})
        if newroomtype != None:
            record = home_automation(roomtype=newroomtype, light_status=newlightstatus,
                                     temperature_degree=newtemperature,
                                     thermostat_status=newthermostatstatus)
            record.save()
        else:
            return JsonResponse({'message': 'Error: you need to provide room type'})

        result = [{'message': 'Success: add the room info to the home_automation table'}]
        result.append(getdata())
        return JsonResponse(result, safe=False)
    else:
        return JsonResponse({'message': 'Error: Wrong command, should use POST'})

def cleardb(request):
    """
    Delete all data in the home_automation table
    """
    if request.method == 'DELETE':
        try:
            home_automation.objects.all().delete()
        except:
            return JsonResponse({'message': 'Error: can not clear all row for home_automation table'})

        result = [{'message': 'Success: rest the home_automation table'}]
        result.append(getdata())
        return JsonResponse(result, safe=False)
    else:
        return JsonResponse({'message': 'Error: Wrong command, should use DELETE'})


def light(request):
    """
    Change the light status for the room with id
    """
    if request.method == 'PUT':
        try:
            roomid = request.headers['Id']
            lightstatus = int(request.headers['Value'])
            if roomid == None or lightstatus == None or (lightstatus != 1 and lightstatus != 0):
                return JsonResponse({'message': 'Error: input is not valid'})
            else:
                # get the row whose id is the user input room id
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

            result = [{'message': 'Success: change the light status for the room (roomid is %s)'%roomid}]
            result.append(getdata())
            return JsonResponse(result, safe=False)
        except:
            return JsonResponse({'message': 'Error: input is not valid'})
    else:
        return JsonResponse({'message': 'Error: Wrong command, should use PUT'})


def temperature(request):
    """
    Change the temperature degree for the room with id
    """
    if request.method == 'PUT':
        # the value must be a float
        try:
            roomid = request.headers['Id']
            temperature  = float(request.headers['Value'])

            if roomid == None or temperature  == None:
                return JsonResponse({'message': 'Error: input is not valid'})
            else:
                # get the row whose id is the user input room id
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

            result = [{'message': 'Success: change the temperature degree for the room (roomid is %s)'%roomid}]
            result.append(getdata())
            return JsonResponse(result, safe=False)
        except:
            return JsonResponse({'message': 'Error: input is not valid'})
    else:
        return JsonResponse({'message': 'Error: Wrong command, should use PUT'})

def thermostat(request):
    """
    Change the thermostat status for the room with id
    """
    if request.method == 'PUT':
        try:
            roomid = request.headers['Id']
            thermostat = request.headers['Value']
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

            result = [{'message': 'Success: change the thermostat status for the room (roomid is %s)'%roomid}]
            result.append(getdata())
            return JsonResponse(result, safe=False)
        except:
            return JsonResponse({'message': 'Error: input is not valid'})
    else:
        return JsonResponse({'message': 'Error: Wrong command, should use PUT'})

def list(request):
    """
    Show all data in the home_automation table
    """
    if request.method == 'GET':
        result = []
        for record in home_automation.objects.values():
            result.append(record)
        return JsonResponse(result, safe=False)
    else:
        return JsonResponse({'message': 'Error: Wrong command, should use GET'})
def getdata():
    """
    Send all data in the home_automation table to other methods
    """
    result = []
    for record in home_automation.objects.values():
        result.append(record)
    return result

