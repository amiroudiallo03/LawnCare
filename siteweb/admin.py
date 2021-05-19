from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('titre', 'sous_titre', 'date_add', 'date_update', 'status')
    search_fields = ('titre',)

@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description', 'date_add', 'date_update', 'status')
    search_fields = ('titre',)

@admin.register(models.Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('titre','date_add', 'date_update', 'status')
    search_fields = ('titre',)

@admin.register(models.Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email','date_add', 'date_update', 'status')
    search_fields = ('email',)

@admin.register(models.ReseauSocial)
class ReseauSocial(admin.ModelAdmin):
    list_display = ('nom', 'lien','date_add', 'date_update', 'status')
    search_fields = ('nom',)

@admin.register(models.Horaire)
class HoraireAdmin(admin.ModelAdmin):
    list_display = ('jour_d_ouverture', 'heure_d_ouverture','date_add', 'date_update', 'status')
    search_fields = ('jour_d_ouverture',)

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image','date_add', 'date_update', 'status')

@admin.register(models.Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('titre_siteweb','siteweb', 'adresse', 'phone', 'email','date_add', 'date_update', 'status')

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name','email', 'sujet','date_add', 'date_update', 'status')