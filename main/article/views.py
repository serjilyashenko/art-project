from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.template.context import RequestContext

def show(request):
    return render_to_response("show.html", locals(), RequestContext(request))
