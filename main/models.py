from django.db import models
from django.utils.translation import gettext_lazy as _

class Portfolio(models.Model):
    CATEGORY_CHOICES = [
        ('app', _('Django')),
        ('product', _('Django REST API')),
        ('branding', _('Telegram bot')),
    ]
    name = models.CharField(max_length=255)    
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/')
    project_url = models.URLField(blank=True,null=True)
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name
    

