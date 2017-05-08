from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
import paho.mqtt.publish as publish
from settings import SETTINGS
from .models import Controller


@login_required()
@require_http_methods(["GET", "POST"])
def index(request):
    if request.method == 'POST':
        if 'name' in request.POST and 'state' in request.POST:
            # Send to MQTT
            publish.single(
                "somfy/" + request.POST['name'],
                payload=request.POST['state'],
                hostname=SETTINGS['mqtt_host'],
                port=SETTINGS['mqtt_port'],
                auth={
                    'username': SETTINGS['mqtt_user'],
                    'password': SETTINGS['mqtt_pass'],
                })
    context = {'controllers': Controller.objects.order_by('sort')}
    return render(request, "index.html", context=context)
