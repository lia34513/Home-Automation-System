from django.db import models
# Create your models here.
class home_automation(models.Model):
    roomtype = models.TextField(default="roomtype")
    light_status = models.IntegerField(default="light_status",null=True)
    temperature_degree = models.FloatField(default="temperature_degree",null=True)
    thermostat_status = models.TextField(default="thermostat_status",null=True)

    class Meta:
        db_table = "home_automation"