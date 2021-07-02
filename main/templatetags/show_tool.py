
from main.models import SelectedTool
from django import template
register = template.Library()

@register.inclusion_tag('main/current_tool.html')
def show_current_tool():
    return {'tool':SelectedTool.objects.all()[0].name}