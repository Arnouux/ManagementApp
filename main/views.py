from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from .models import Tool
from django.forms import forms

class NameForm(forms.Form):
    name = forms.Form()

def index(request):
    tools_list = Tool.objects.order_by('name')
    context = {
        'tools_list': tools_list,
    }
    
    name = request.session.get("name")
    if name is None:
        return HttpResponseRedirect('/login/')
    context["name"] = name

    return render(request, 'main/index.html', context)

def reserve(request, tool_id):
    return HttpResponse("Reserving tool {}".format(tool_id))