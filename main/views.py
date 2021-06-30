from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
import openpyxl
from .models import Tool
from django.forms import forms
from decorator import decorator
from django.conf import settings
import datetime
from dateutil.relativedelta import relativedelta

class NameForm(forms.Form):
    name = forms.Form()

@decorator
def login_required(f, request, *args, **kwargs):
    """
    Makes sure the user connecting is known in the database.

    Args:
        f (function): the functio nto which this decorator is attached
        request: contains session variables, type of request, etc.

    Returns:
        f: calls the function to follow
        HttpResponseRedirect: redirect to login page if user is not connected.
    """
    name = request.session.get("name")
    if name is None:
        return HttpResponseRedirect('/login/')
    else :
        return f(request, *args, **kwargs)

@login_required
def index(request):
    """
    Search in 2 excel files infos about the connected user.

    Args:
        request: contains session variables, type of request, etc.

    Returns:
        render(function): Shows the index html page.
    """
    name = request.session.get("name")
    habilitations = settings.FILE_EXCEL_HABILITATION
    codes = settings.FILE_EXCEL_CODE_AFFAIRE
        
    context = {
        'name': name
    }

    wb = openpyxl.load_workbook(habilitations)
    ws = wb.active
    context['fullname'] = f"{request.user.first_name} {request.user.last_name.upper()}"
    for row in ws.iter_rows():
        if (row[0].value is not None and
            row[0].value.upper() == f"{request.user.last_name} {request.user.first_name}".upper()):
            
            dateElec = str(row[2].value)
            dateMedic = str(row[10].value)
            dateElec = datetime.datetime.strptime(dateElec, "%Y-%m-%d %H:%M:%S")
            dateMedic = datetime.datetime.strptime(dateMedic, '%Y-%m-%d %H:%M:%S')
            
            today = datetime.datetime(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day) 
            if (dateElec + relativedelta(months=36) < today) :
                elecIsOld = True
            else :
                elecIsOld = False
            if (dateMedic + relativedelta(months=24) < today) :
                medicIsOld = True
            else :
                medicIsOld = False
            context['elecIsOld'] = elecIsOld
            context['medicIsOld'] = medicIsOld
            
            dateElec = datetime.datetime.strftime(dateElec, "%d/%m/%Y")
            dateMedic = datetime.datetime.strftime(dateMedic, "%d/%m/%Y")
            context['dateElec'] = dateElec
            context['dateMedic'] = dateMedic
            
            break
    
    wb = openpyxl.load_workbook(codes)
    ws = wb.active
    
    codes = {}
    row_nb = -1
    for i, row in enumerate(ws.iter_rows()):
        if (row[0].value is not None and
            row[0].value.upper() == request.user.last_name.upper()):
            row_nb = i
            break
    
    if row_nb != -1:
        for col in ws.iter_cols():
            if col[row_nb].value is not None:
                codes[col[4].value] = True
            else :
                codes[col[4].value] = False
    codes.pop(None, None)
    codes.pop('D = Devis\nM = Mesures\nR = Rapport', None)
    if codes is not None :
        context['codes'] = codes
    
    return render(request, 'main/index.html', context)

@login_required
def reserve(request, tool_id):
    return HttpResponse("Reserving tool {}".format(tool_id))

@login_required
def materiel(request):
    context = {
        'name': request.session.get("name")
    }
    return render(request, 'main/materiel.html', context)

@login_required
def consultation(request):
    return HttpResponse("consultation")

@login_required
def sortie(request):
    tools_list = Tool.objects.order_by('name')
    context = {
        'tools_list': tools_list,
        'name': request.session.get("name")
    }
    return render(request, 'main/sortie.html', context)

@login_required
def retour(request):
    return HttpResponse("Retour")

@login_required
def pret(request):
    return HttpResponse("Prêt")