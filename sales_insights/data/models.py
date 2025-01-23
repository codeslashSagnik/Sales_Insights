from django.db import models

class SalesData(models.Model):
    date = models.DateField()
    price_per_unit = models.FloatField()
    units_sold = models.IntegerField()

    class Meta:
        db_table = 'data_salesdata'
def __str__(self):
        return f"{self.date} - {self.price_per_unit} - {self.units_sold}"
