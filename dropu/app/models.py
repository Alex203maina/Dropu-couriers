from django.db import models

# Create your models here.

class Services(models.Model):
    service_title = models.CharField(max_length=255)
    service_description = models.TextField()
    service_image = models.ImageField(upload_to='services')
    
    def __str__(self):
        return self.service_title
    
class FeatureSection(models.Model):
    title = models.CharField(max_length=255)
    image =models.ImageField(upload_to='features')
    
    def __str__(self):
        return self.title
    
class Feature(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon_class = models.CharField(max_length=50)  
    order = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['order'] 
        
class LogisticsPrice(models.Model):
    location = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.location
class FactBox(models.Model):
    title = models.CharField(max_length=255)
    value = models.PositiveIntegerField()
    icon_class = models.CharField(max_length=50)  # e.g., "fa fa-users"
    background_class = models.CharField(max_length=50, default="bg-primary")  # e.g., "bg-primary"
    order = models.PositiveIntegerField(default=0)  # To manage the order of display

    def __str__(self):
        return self.title


class FactSection(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    contact_title = models.CharField(max_length=255, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    fact_boxes = models.ManyToManyField(FactBox, related_name="sections")

    def __str__(self):
        return self.title