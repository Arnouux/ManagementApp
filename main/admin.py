from django.contrib import admin

from .models import Tool, Reservation

class DatesInline(admin.StackedInline):
    model = Reservation
    extra = 1

class ToolAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields':['name']}),
    ]
    inlines = [DatesInline]

admin.site.register(Tool, ToolAdmin)