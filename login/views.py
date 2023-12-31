from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def login_view(request):
    template = loader.get_template("login/index.html")
    print('request', request.method)
    context = {}
    if request.method == 'POST':
        template = loader.get_template("dashboard/index.html")
        context['name'] = request.POST.get('username')
        context['friends_list'] = ['prince', 'sanjay', 'amiay', 'gandhi', 'einstein']
    return HttpResponse(template.render(context, request))

