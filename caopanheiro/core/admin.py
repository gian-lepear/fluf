from core.models import Animal
from django.contrib import admin


class AnimalAdmin(admin.ModelAdmin):
    pass


admin.site.register(Animal)
