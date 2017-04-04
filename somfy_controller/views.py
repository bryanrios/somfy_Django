import datetime
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from google.cloud import datastore
import paho.mqtt.publish as publish
from django_somfy.settings import SETTINGS

@login_required()
@require_http_methods(["GET", "POST"])
def index(request):
    ds = datastore.Client()
    if request.method == 'POST':
        if 'name' in request.POST and 'state' in request.POST:
            # Send to MQTT
            publish.single("somfy/" + request.POST['name'],
                           payload=request.POST['state'],
                           hostname=SETTINGS['mqtt_host'],
                           port=SETTINGS['mqtt_port'],
                           auth={
                               'username': SETTINGS['mqtt_user'],
                               'password': SETTINGS['mqtt_pass']
                               }
                          )

            # Update GCP Datastore
            entity = ds.get(ds.key('Controller', request.POST['name']))
            entity['state'] = request.POST['state']
            entity['timestamp'] = datetime.datetime.utcnow()
            ds.put(entity)
    query = ds.query(kind='Controller', order=('sort',))
    controllers = []
    for result in query.fetch():
        new_dict = dict(result)
        new_dict['name'] = result.key.name
        controllers.append(new_dict)
    context = {'controllers': controllers}
    return render(request, "index.html", context=context)

@require_http_methods(["GET"])
def state(request):
    ds = datastore.Client()
    query = ds.query(kind='Controller', order=('sort',))
    json_dict = {result.key.name: result['state'] for result in query.fetch()}
    return JsonResponse(json_dict)
