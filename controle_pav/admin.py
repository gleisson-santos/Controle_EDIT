
from django.contrib import admin
from .models import Esgoto, Pavimento, Pendencias, Material, Lancamento

admin.site.register(Pavimento)
admin.site.register(Esgoto)
admin.site.register(Pendencias)
admin.site.register(Material)
admin.site.register(Lancamento)

# Register your models here.
