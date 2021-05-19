from django.db import models


class Convention(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True 


class Service(Convention):
    icone = models.CharField(max_length= 200)
    titre = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.titre

class Conseil(Convention):
    image = models.ImageField()
    titre = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.titre

class Testimonial(Convention):
    temoignage = models.TextField()
    image = models.ImageField()
    nom = models.CharField(max_length=200)
    travail = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.nom

class Prestation(Convention):
    image = models.ImageField()
    date = models.DateField()
    titre = models.CharField(max_length=200)
    description_titre = models.TextField()

    class Meta:
        verbose_name = 'Prestation'
        verbose_name_plural = 'Prestations'

    def __str__(self):
        return self.titre

class Gallery(Convention):
    image = models.ImageField()
    titre = models.CharField(max_length=200)
    sous_titre = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery'

    def __str__(self):
        return self.titre

