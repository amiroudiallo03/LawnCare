from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Service)
class Service(admin.ModelAdmin):
    list_display = ('icone','titre', 'date_add','date_update','status')

@admin.register(models.Conseil)
class Conseil(admin.ModelAdmin):
    list_display = ('titre', 'date_add','date_update','status')
    search_fields = ('titre', 'date_add','date_update','status')

@admin.register(models.Testimonial)
class Testimonial(admin.ModelAdmin):
    list_display = ('temoignage', 'nom', 'travail', 'date_add','date_update','status')
    search_fields = ('nom',)

@admin.register(models.Prestation)
class Prestation(admin.ModelAdmin):
    list_display = ('titre','date', 'date_add','date_update','status')
    search_fields = ('titre',)

@admin.register(models.Gallery)
class Prestation(admin.ModelAdmin):
    list_display = ('titre','sous_titre', 'date_add','date_update','status')
    search_fields = ('titre',)