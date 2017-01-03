# -*- encoding: utf-8 -*-
from django.db import models


class Neighborhood(models.Model):
    """
    [P ] ID
    [P ] Name
    [P-] POST_ID
    [P ] LAST_UPDATE
    [P-] TIME_CACHE
    [P ] Adress
    [P ] Zoom
    [P ] Lat
    [P ] Lng
    [P ] SHOW_HOME
    [X ] SHOW_CONDOM
    [P ] SHOW_MAP_HOME
    [X ] SHOW_MAP_CONDOM
    [P ] SHOW_COLLECTION
    [M ] FOR_SALE / SELL
    [M ] RENT
    [M ] SALE_PRICE_MIN
    [M ] SALE_PRICE_MAX
    """

    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    zoom = models.FloatField()

    # BEGIN
    # Pasar a GeoDjango
    lat = models.FloatField()
    lng = models.FloatField()
    # END

    show_home = models.BooleanField()
    show_condom = models.BooleanField()
    show_map_home = models.BooleanField()
    show_map_condom = models.BooleanField()
    show_collection = models.BooleanField()

    registration_date = models.DateTimeField()
    modification_date = models.DateTimeField()

    class Meta:
        verbose_name = "Neighborhood"
        verbose_name_plural = "Neighborhoods"

    def __str__(self):
        if self.name:
            return self.name

        return 'Unnamed neighborhood'

    def save(self, *args, **kwargs):
        return super(Neighborhood, self).save(*args, **kwargs)

    # @models.permalink
    # def get_absolute_url(self):
    #     return ('/neighborhoods/{0}'.format(self.id))

    def _is_for_sale(self):
        # Ejemplo de implementacion
        # return self.properties_set.filter(is_for_sale=True).exists()
        raise(Exception('No yet implemented'))

    is_for_sale = property(_is_for_sale)

    # def _rent():
    #     raise(Exception('No yet implemented'))

    # def _sale_price_min():
    #     raise(Exception('No yet implemented'))

    # def _sale_price_max():
    #     raise(Exception('No yet implemented'))

class Property(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)

    neighborhood = models.ForeignKey(Neighborhood)

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"

    def __str__(self):
        if self.name:
            return self.name

        return 'Unnamed property'

    def save(self, *args, **kwargs):
        return super(Property, self).save(*args, **kwargs)

    # @models.permalink
    # def get_absolute_url(self):
    #     return ('')

    # TODO: Define custom methods here
