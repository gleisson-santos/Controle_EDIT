
from django.contrib import admin
from .models import Esgoto, Pavimento, Pendencias, Material, Lancamento
from .models import Fornecedor, Materiall, Compra, Produto

admin.site.register(Pavimento)
admin.site.register(Esgoto)
admin.site.register(Pendencias)
admin.site.register(Material)
admin.site.register(Lancamento)

# Register your models here.


class ProdutoAdmin(admin.TabularInline):

	model = Produto
	extra = 1

class FornecedorAdmin(admin.ModelAdmin):
	pass

class MateriallAdmin(admin.ModelAdmin):
	pass

class CompraAdmin(admin.ModelAdmin):

	date_hierarchy = 'data'
	list_filter = ['data', 'fornecedor']

	inlines = [ProdutoAdmin]
	list_display = ['data', 'nota_fiscal', 'fornecedor', 'valor_compra', 'imprimir']


admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(Compra, CompraAdmin)
admin.site.register(Materiall, MateriallAdmin)