
from django.contrib import admin
from .models import Esgoto, Pavimento, Pendencias, Material

admin.site.register(Pavimento)
admin.site.register(Esgoto)
admin.site.register(Pendencias)
admin.site.register(Material)

# Register your models here.
