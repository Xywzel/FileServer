from django.contrib import admin
from . import models

admin.site.register(models.Profile)
admin.site.register(models.Organization)
admin.site.register(models.DownloadRecord)
admin.site.register(models.Upload)
