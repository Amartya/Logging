#Django imports
from django.template import RequestContext,Context
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

#Reese app imports
from reese.models import FrogPondLog

import json

def index(request):
    return HttpResponse(json.dumps({'REESE': 'frogpond'}), content_type="application/json")

@csrf_exempt
def reeselog(request):
    if request.method == "POST":
        try:
            #read request data as json from request body
            request_data = json.loads(request.body)

            #store the app_id and app_data payload
            app_id = request_data['app_id']
            app_data= request_data['app_data']
        except:
            app_id = "appID error"
            app_data = "appData error"
            return HttpResponse(json.dumps({'status': 'failed to saved data'}), content_type="application/json")
        print(request)
        #create a log object and save it in the database
        log_data = FrogPondLog(name=app_id, data=app_data)
        log_data.save()

        return HttpResponse(json.dumps({'status': 'data saved successfully'}), content_type="application/json")

    return HttpResponse("End point")