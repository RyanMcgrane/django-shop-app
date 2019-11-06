from django.contrib.gis.db import models


# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    # Converts the name incidencess to incidences on the admin site
    class Meta:
        verbose_name_plural = "Shops"

