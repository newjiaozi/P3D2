from django.contrib import admin

# Register your models here.
from .models import InterfaceModel,ResultModel,InterfaceTestResult

admin.site.register(InterfaceModel)
admin.site.register(ResultModel)
admin.site.register(InterfaceTestResult)