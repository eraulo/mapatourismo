from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from . import models as tourismo_models

# Register your models here.
admin.site.register(tourismo_models.Tourismo, LeafletGeoAdmin)
