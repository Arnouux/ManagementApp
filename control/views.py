from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from main.models import Tool
from .forms import CategoryForm, DeleteForm, RenameForm, NewUserForm
from django.contrib.auth.models import User

def control(request):
    context = {}
    for key, value in request.POST.items():
        print(f'Key: {key}')
        print(f'Value: {value}')
     
    if request.method == 'POST':
        if "rename" in request.POST :
            context['form_rename'] = RenameForm()
            request.session["current_id"] = request.POST["id"]
        elif "delete" in request.POST :
            context['form_delete'] = DeleteForm()
            request.session["current_id"] = request.POST["id"]
        
        if "btnYesOrNo" in request.POST :
            if request.POST["btnYesOrNo"] == "yes":
                tool_selected = Tool.objects.get(id=request.session.get("current_id"))
                tool_selected.delete()
                request.session["current_id"] = None
        
        elif "new_name" in request.POST :
            tool_selected = Tool.objects.get(id=request.session.get("current_id"))
            tool_selected.name = request.POST["new_name"]
            tool_selected.save()
        
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data.get("name")
            Tool.objects.create(name=category)
            
        form = NewUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            user = User.objects.create_user(username=username.upper(),
                                       first_name=form.cleaned_data.get("first_name"),
                                       last_name=form.cleaned_data.get("last_name"),
                                       email=form.cleaned_data.get("mail"),
                                       password=f"{username.lower()}{username.lower()}")
            user.save()
        
    
    tools_list = Tool.objects.order_by('name')
    form = CategoryForm()
    
    context['tools_list'] = tools_list
    context['form'] = form
    
    users_list = User.objects.all()
    context["users_list"] = users_list
    user_form = NewUserForm()
    context["user_form"] = user_form

    name = request.session.get("name")
    if name is None:
        return HttpResponseRedirect('/login/')
    context["name"] = name
    

    return render(request, 'control/control.html', context)