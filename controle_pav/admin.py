
from django.contrib import admin
from .models import Esgoto, Pavimento, Pendencias

admin.site.register(Pavimento)
admin.site.register(Esgoto)
admin.site.register(Pendencias)

# Register your models here.
