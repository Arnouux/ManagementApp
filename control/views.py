from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from main.models import Tool

def control(request):
    tools_list = Tool.objects.order_by('name')
    context = {
        'tools_list': tools_list,
    }
    
    name = request.session.get("name")
    if name is None:
        return HttpResponseRedirect('/login/')
    context["name"] = name

    return render(request, 'main/index.html', context)