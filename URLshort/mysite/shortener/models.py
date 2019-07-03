from django.conf import settings
from django.db import models
from .uti import create_shortcode
# Create your models here.

SHORTCODE_MAX= getattr(settings, 'SHORTCODE_MAX', 15)
class shortURLmanager(models.Manager):

    def all(self,*args,**kwargs):
        qs_main=super(shortURLmanager, self).all(*args,**kwargs)
        qs=qs_main.filter(active=True)
        return qs
    
    def refresh_shortcode(self, items=None):

        qs =  shortURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs=qs.order_by('-id')[:items]

        new_codes=0
        for website in qs:
            website.shortcode=create_shortcode(website)
            website.save()
            new_codes += 1
        return "New codes made "+str(new_codes)
        
class shortURL(models.Model):

    url = models.CharField(max_length=200,)
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects= shortURLmanager()

    def save(self,*args,**kwargs):
        if self.shortcode is None or self.shortcode=='':
            self.shortcode=create_shortcode(self)
        super(shortURL,self).save(*args,**kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

    
