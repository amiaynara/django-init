# Create your views here.
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def dashboard_view(request):
    template = loader.get_template("dashboard/index.html")
    name = 'amiay'
    return HttpResponse(template.render({'name': name}, request))