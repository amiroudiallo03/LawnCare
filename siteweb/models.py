from django.db import models

# Create your models here.


class Convention(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True 


class Banner(Convention):
    images = models.ImageField(upload_to= 'images_banner')
    titre = models.CharField(max_length=250)
    sous_titre = models.CharField(max_length= 250)
    message = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def __str__(self):
        return self.titre


class About(Convention):
    images = models.ImageField()
    titre = models.CharField(max_length=250)
    description = models.TextField()
    option = models.ForeignKey("Option", on_delete= models.CASCADE, related_name= "option_about")

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        return self.titre


class Option(Convention):
    titre = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Option'
        verbose_name_plural = 'Options'

    def __str__(self):
        return self.titre

class Newsletter(Convention):
    email = models.EmailField()
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'

    def __str__(self):
        return self.email

class ReseauSocial(Convention):
    nom = models.CharField(max_length=250)
    icone = models.CharField(max_length=250)
    lien = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'ReseauSocial'
        verbose_name_plural = 'ReseauSocials'

    def __str__(self):
        return self.nom

class Horaire(Convention):
    jour_d_ouverture = models.CharField(max_length= 20)
    heure_d_ouverture = models.CharField(max_length=  20)


    class Meta:
        verbose_name = 'Horaire'
        verbose_name_plural = 'Horaires'

    def __str__(self):
        return self.jour_d_ouverture

class Image(Convention):
    image = models.ImageField()

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        

class Website(Convention):
    titre_siteweb = models.CharField(max_length=100)
    siteweb = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    copyright = models.CharField(max_length=200)
    description_siteweb = models.TextField()
    vocation = models.TextField()
    titre_services = models.CharField(max_length=200)
    description_service = models.TextField()
    titre_testimonial = models.CharField(max_length=100)
    titre_prestation = models.CharField(max_length=50)
    website = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Website'
        verbose_name_plural = 'Websites'

    def __str__(self):
        return self.titre_siteweb

class Contact(Convention):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    sujet = models.CharField(max_length=200)
    messages = models.TextField()

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.titre_siteweb
