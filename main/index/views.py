from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.template.context import RequestContext

def home(request):
    return render_to_response("home.html", locals(), RequestContext(request))
