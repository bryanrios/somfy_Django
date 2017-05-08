from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
import paho.mqtt.client as mqtt
from settings import SETTINGS
from .models import Controller


@login_required()
@require_http_methods(["GET", "POST"])
def index(request):
    if request.method == 'POST':
        if 'name' in request.POST and 'state' in request.POST:
            # Send to MQTT
            client = mqtt.Client()
            client.username_pw_set(SETTINGS['mqtt_user'], SETTINGS['mqtt_pass'])
            client.connect(SETTINGS['mqtt_host'], SETTINGS['mqtt_port'])
            client.publish(
                "somfy/" + request.POST['name'],
                payload=request.POST['state'],
                qos=0
                )
    context = {'controllers': Controller.objects.order_by('sort')}
    return render(request, "index.html", context=context)
