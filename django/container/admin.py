from django.contrib import admin
from container.models import Procedure, Receipe,ReceipeCategory,ReceipeIngredient,Ingredient,Unit,Review
admin.site.register(Receipe)

admin.site.register(ReceipeCategory)
admin.site.register(ReceipeIngredient)
admin.site.register(Ingredient)
admin.site.register(Unit)
admin.site.register(Review)
admin.site.register(Procedure)








# Register your models here.
