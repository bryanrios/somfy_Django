import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from google.cloud import datastore

@login_required()
@require_http_methods(["GET", "POST"])
def index(request):
    ds = datastore.Client()
    if request.method == 'POST':
        if 'name' in request.POST and 'state' in request.POST: 
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

