from django.db import models

class Country(models.Model):
    class Meta:
        managed = False
        db_table = 'countries'

    valid_regions = ['Europe', 'Africa', 'Americas', 'Oceania', 'Asia']

    id = models.AutoField(primary_key=True)
    name = models.CharField()
    alpha2 = models.CharField()
    alpha3 = models.CharField()
    region = models.CharField()
