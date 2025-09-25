from django.db import models

class KhorasanRate(models.Model):
    currency = models.CharField(max_length=50)
    buying_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    selling_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    up = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    down = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    updated_time = models.CharField(max_length=20, null=True, blank=True)  # changed!
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.currency} - Buy: {self.buying_rate} Sell: {self.selling_rate} Up: {self.up} Down: {self.down} Last update: {self.updated_time}"
    

class SaraiRate(models.Model):
    currency = models.CharField(max_length=50)
    buying_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    selling_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    up = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    down = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    updated_time = models.CharField(max_length=20, null=True, blank=True)  # changed!
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.currency} - Buy: {self.buying_rate} Sell: {self.selling_rate} Up: {self.up} Down: {self.down} Last update: {self.updated_time}"    

class DaAfgRate(models.Model):
    currency = models.CharField(max_length=50)
    buying_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    selling_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    up = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    down = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    updated_time = models.CharField(max_length=20, null=True, blank=True)  # changed!
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.currency} - Buy: {self.buying_rate} Sell: {self.selling_rate} Up: {self.up} Down: {self.down} Last update: {self.updated_time}"