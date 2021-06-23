from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm
from django.http import HttpResponse

def login(request):
    request.session["name"] = None
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            request.session["name"] = form.cleaned_data.get("name").upper()
            if request.session.get("name") == "ADMIN":
                return HttpResponseRedirect('/admin/')
            else:
                return HttpResponseRedirect('/main/')
    else:
        form = NameForm()
    return render(request, 'login/login.html', {'form':form})