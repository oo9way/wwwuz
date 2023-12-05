from django.contrib import admin
from app import models


admin.site.register(models.Website)
admin.site.register(models.Data)
admin.site.register(models.Category)
admin.site.register(models.Visitor)