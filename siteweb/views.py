from django.shortcuts import render, redirect
from . import models
from service import models as models_service

def index(request):
    banners = models.Banner.objects.filter(status=True).first()
    websites = models.Website.objects.filter(status=True).first()
    ReseauSociaux = models.ReseauSocial.objects.filter(status= True).all()
    abouts = models.About.objects.filter(status= True).first()
    options = models.Option.objects.filter(status= True).all()
    services = models_service.Service.objects.filter(status=True).all()
    Prestations = models_service.Prestation.objects.filter(status= True).order_by('-date_add')[:3]
    conseils = models_service.Conseil.objects.filter(status=True).all()
    Testimonials = models_service.Testimonial.objects.filter(status = True).all()
    return render(request, 'index.html', locals())

def about(request):
    abouts = models.About.objects.filter(status= True).first()
    banners = models.Banner.objects.filter(status=True).first()
    options = models.Option.objects.filter(status= True).all()
    services = models_service.Service.objects.filter(status=True).all()
    Testimonials = models_service.Testimonial.objects.filter(status = True).all()
    websites = models.Website.objects.filter(status=True).first()
    ReseauSociaux = models.ReseauSocial.objects.filter(status= True).all()
    images = models.Image.objects.filter(status=True).first()
    return render(request, 'about.html', locals())

def blog(request):
    Prestations = models_service.Prestation.objects.filter(status= True).all()
    ReseauSociaux = models.ReseauSocial.objects.filter(status= True).all()
    websites = models.Website.objects.filter(status=True).first()
    images = models.Image.objects.filter(status=True).first()
    return render(request, 'blog.html', locals())

def services(request):
    services = models_service.Service.objects.filter(status=True).all()
    websites = models.Website.objects.filter(status=True).first()
    conseils = models_service.Conseil.objects.filter(status=True).all()
    ReseauSociaux = models.ReseauSocial.objects.filter(status= True).all()
    websites = models.Website.objects.filter(status=True).first()
    images = models.Image.objects.filter(status=True).first()
    return render(request, 'services.html',locals())

def gallery(request):
    galleries = models_service.Gallery.objects.filter(status=True).all()
    ReseauSociaux = models.ReseauSocial.objects.filter(status= True).all()
    websites = models.Website.objects.filter(status=True).first()
    images = models.Image.objects.filter(status=True).first()
    return render(request, 'gallery.html', locals())

def contact(request):
    websites = models.Website.objects.filter(status=True).first()
    ReseauSociaux = models.ReseauSocial.objects.filter(status= True).all()
    images = models.Image.objects.filter(status=True).first()
    return render(request, 'contact.html',locals())

def blogsingle(request):
    websites = models.Website.objects.filter(status=True).first()
    ReseauSociaux = models.ReseauSocial.objects.filter(status= True).all()
    images = models.Image.objects.filter(status=True).first()
    Prestations = models_service.Prestation.objects.filter(status= True).order_by('-date_add')[:3]
    return render(request, 'blog-single.html',locals())

def newsletterpost(request):
    newMail = request.POST.get("email")
    new = models.Newsletter()
    new.email = newMail
    new.save()
    retour = request.META.get("HTTP_REFERER")
    return redirect(retour, "/")