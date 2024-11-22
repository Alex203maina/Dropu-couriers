from django.contrib import admin
from .models import Services, Feature, FeatureSection,LogisticsPrice

# Register your models here.
admin.site.register(Services)
admin.site.register(Feature)
admin.site.register(FeatureSection)
admin.site.register(LogisticsPrice)