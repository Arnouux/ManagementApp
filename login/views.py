from main.views import VideoCamera
from django.contrib.auth import authenticate
import django.contrib.auth
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import ConnexionForm
from django.http import HttpResponse

def login(request):
    request.session["name"] = None
    list_cam = list(VideoCamera._instances)
    if len(list_cam) > 0 :
        del list_cam[0]
    django.contrib.auth.logout(request)
    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            request.session["name"] = form.cleaned_data.get("name").upper()
            name = request.session.get("name")
            pwd = form.cleaned_data.get("password")
            user = authenticate(username=name, password=pwd)
            if user is not None and hash(pwd)==-4281904718209466055:
                django.contrib.auth.login(request, user)
                return HttpResponseRedirect('/main/')
            if name == "ADMIN":
                return HttpResponseRedirect('/control/')
    else:
        form = ConnexionForm()
    return render(request, 'login/login.html', {'form':form})